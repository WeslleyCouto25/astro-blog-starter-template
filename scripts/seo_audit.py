#!/usr/bin/env python3
"""Auditoria SEO estática: títulos, metadados, indexação, links e Schema.org."""
from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
from urllib.parse import urlsplit,unquote
import json,re,sys,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent.parent
HOST="https://comprartccbrasil.com.br"
EXCLUDE={"obrigado/index.html"}
class Parser(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True);self.title=[];self.title_open=False;self.buffer="";self.h1=0;self.links=[];self.canonical=[];self.description=[];self.robots=[];self.script_open=False;self.script_buffer="";self.jsonld=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=="title":self.title_open=True;self.buffer=""
  if tag=="h1":self.h1+=1
  if tag=="a":self.links.append(a.get("href",""))
  if tag=="link" and a.get("rel")=="canonical":self.canonical.append(a.get("href",""))
  if tag=="meta":
   if a.get("name")=="robots":self.robots.append(a.get("content",""))
   if a.get("name")=="description":self.description.append(a.get("content",""))
  if tag=="script" and a.get("type")=="application/ld+json":self.script_open=True;self.script_buffer=""
 def handle_data(self,s):
  if self.title_open:self.buffer+=s
  if self.script_open:self.script_buffer+=s
 def handle_endtag(self,tag):
  if tag=="title" and self.title_open:self.title.append(self.buffer.strip());self.title_open=False
  if tag=="script" and self.script_open:self.jsonld.append(self.script_buffer);self.script_open=False
pages=sorted(ROOT.rglob("index.html"))
paths={str(x.relative_to(ROOT)).replace("\\","/") for x in pages}
errors=[];warnings=[];urlmap={};titles=[]
for p in pages:
 rel=str(p.relative_to(ROOT)).replace("\\","/")
 url=HOST+("/" if rel=="index.html" else "/"+rel[:-10])
 urlmap[url]=rel
 h=Parser();h.feed(p.read_text(encoding="utf-8"))
 if len(h.title)!=1:errors.append(f"{rel}: deve ter 1 title")
 else:
  titles.append((h.title[0],rel))
  if len(h.title[0])>72:warnings.append(f"{rel}: title >72 caracteres")
 if h.h1!=1:errors.append(f"{rel}: {h.h1} tags H1")
 if h.canonical!=[url]:errors.append(f"{rel}: canonical incorreto {h.canonical} esperado {url}")
 if len(h.description)!=1 or not h.description[0]:errors.append(f"{rel}: description ausente/duplicada")
 elif len(h.description[0])>185:warnings.append(f"{rel}: meta description extensa")
 if len(h.robots)!=1:errors.append(f"{rel}: robots meta ausente/duplicado")
 elif rel in EXCLUDE:
  if "noindex" not in h.robots[0]:errors.append(f"{rel}: deve ser noindex")
 elif "noindex" in h.robots[0] or "index" not in h.robots[0]:
  errors.append(f"{rel}: indexação bloqueada {h.robots[0]}")
 if not h.jsonld:errors.append(f"{rel}: JSON-LD ausente")
 for raw in h.jsonld:
  try:json.loads(raw)
  except Exception as e:errors.append(f"{rel}: JSON-LD inválido {e}")
 for href in h.links:
  if not href or href.startswith(("#","mailto:","tel:","javascript:","data:")):continue
  u=urlsplit(href)
  if u.scheme or u.netloc:continue
  target=(ROOT/unquote(u.path).lstrip("/")) if href.startswith("/") else (p.parent/unquote(u.path))
  if target.is_dir():target=target/"index.html"
  if not target.is_file():errors.append(f"{rel}: link interno quebrado {href}")
counts=Counter(x for x,_ in titles)
for title,rel in titles:
 if counts[title]>1:errors.append(f"{rel}: title duplicado ({title})")
expected={u for u,p in urlmap.items() if p not in EXCLUDE}
try:
 root=ET.fromstring((ROOT/"sitemap.xml").read_text(encoding="utf-8"))
 listed=[x.text for x in root.iter() if x.tag.endswith("loc")]
 if len(listed)!=len(set(listed)):errors.append("sitemap: URLs duplicadas")
 if set(listed)!=expected:errors.append(f"sitemap: faltando {len(expected-set(listed))}, excessos {len(set(listed)-expected)}")
except Exception as e:errors.append(f"sitemap inválido: {e}")
rob=(ROOT/"robots.txt").read_text()
if "Disallow: /" in rob:errors.append("robots.txt bloqueia o domínio")
if "Sitemap: "+HOST+"/sitemap.xml" not in rob:errors.append("robots.txt sem sitemap")
if len(list((ROOT/"estados").glob("*/index.html")))!=27:errors.append("estados incompletos")
if len(list((ROOT/"atendimento").glob("*/index.html")))!=27:errors.append("capitais incompletas")
if len(list((ROOT/"professores").glob("*/index.html")))!=8:errors.append("áreas dos professores incompletas")
report={"html_pages":len(pages),"eligible_for_indexing":len(expected),"noindex_utility":len(EXCLUDE),"schemas_validated_syntactically":len(pages),"errors":errors,"warnings":warnings}
print(json.dumps(report,ensure_ascii=False,indent=2))
sys.exit(1 if errors else 0)
