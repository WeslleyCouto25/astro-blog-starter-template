#!/usr/bin/env python3
"""Static SEO auditor — runs without dependencies or external calls."""
from __future__ import annotations
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json, re, sys
ROOT = Path(__file__).resolve().parent.parent
BASE = "https://comprartccbrasil.com.br"
class Inspect(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.titles=[];self.h1=0;self.metas=[];self.links=[];self.scripts=[];self.canonical=[];self.open_script=False;self.buff=""
        self.open_title=False;self.tbuf=""
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=="title":self.open_title=True;self.tbuf=""
        if tag=="h1":self.h1+=1
        if tag=="meta":self.metas.append(a)
        if tag=="link" and a.get("rel")=="canonical":self.canonical.append(a.get("href",""))
        if tag=="a":self.links.append(a.get("href",""))
        if tag=="script" and a.get("type")=="application/ld+json":self.open_script=True;self.buff=""
    def handle_data(self,data):
        if self.open_script:self.buff+=data
        if self.open_title:self.tbuf+=data
    def handle_endtag(self,tag):
        if tag=="script" and self.open_script:self.scripts.append(self.buff);self.open_script=False
        if tag=="title" and self.open_title:self.titles.append(self.tbuf.strip());self.open_title=False
def expected_url(path):
    return BASE+("/" if path==ROOT/"index.html" else "/"+str(path.relative_to(ROOT).parent).replace("\\","/")+"/")
pages=sorted(ROOT.rglob("index.html"))
errors=[];warn=[];infos=[];titles=[];page_urls=set()
for path in pages:
    raw=path.read_text(encoding="utf-8")
    d=Inspect()
    try:d.feed(raw)
    except Exception as e:errors.append(f"{path.relative_to(ROOT)}: HTML parser error {e}");continue
    name=str(path.relative_to(ROOT));canonical=expected_url(path);page_urls.add(canonical)
    if len(d.titles)!=1:errors.append(f"{name}: expected one title; found {len(d.titles)}")
    else:titles.append((d.titles[0],name))
    if d.h1!=1:errors.append(f"{name}: expected one H1; found {d.h1}")
    if len(d.canonical)!=1 or d.canonical[0]!=canonical:errors.append(f"{name}: missing/mismatched self-canonical: {d.canonical} != {canonical}")
    descriptions=[m.get("content","") for m in d.metas if m.get("name")=="description"]
    if len(descriptions)!=1 or not descriptions[0].strip():errors.append(f"{name}: missing/duplicate meta description")
    if len(descriptions)==1 and len(descriptions[0])>180:warn.append(f"{name}: long meta description ({len(descriptions[0])})")
    robots=[m.get("content","") for m in d.metas if m.get("name")=="robots"]
    if len(robots)!=1 or "noindex" not in robots[0]:errors.append(f"{name}: staging noindex missing")
    if not d.scripts:warn.append(f"{name}: no JSON-LD")
    for block in d.scripts:
        try:json.loads(block)
        except Exception as e:errors.append(f"{name}: invalid JSON-LD: {e}")
    for href in d.links:
        if not href or href[0]=="#" or href.startswith(("mailto:","tel:","javascript:","data:")):continue
        parts=urlsplit(href)
        if parts.scheme or parts.netloc:continue
        if href.startswith("/"): target=ROOT/href.lstrip("/")
        else:target=path.parent/unquote(parts.path)
        if target.is_dir():target=target/"index.html"
        if not target.resolve().is_file():
            errors.append(f"{name}: broken relative link: {href}")
counts=Counter(t for t,_ in titles)
for title,n in titles:
    if counts[title]>1:errors.append(f"{n}: duplicate title {title}")
    if len(title)>73:warn.append(f"{n}: title length {len(title)}")
smap=(ROOT/"sitemap.xml").read_text(encoding="utf-8")
for u in re.findall(r"<loc>([^<]+)</loc>",smap):
    if u not in page_urls:errors.append(f"sitemap: URL missing from source files: {u}")
statepages=list((ROOT/"estados").glob("*/index.html"))
citypages=list((ROOT/"atendimento").glob("*/index.html"))
area_pages=list((ROOT/"professores").glob("*/index.html"))
if len(statepages)!=27:errors.append(f"Expected 27 state routes; found {len(statepages)}")
if len(citypages)!=27:errors.append(f"Expected 27 capital routes; found {len(citypages)}")
if len(area_pages)!=8:errors.append(f"Expected 8 specialist directories; found {len(area_pages)}")
print("=== SEO STATIC AUDIT ===")
print(json.dumps({"html_pages":len(pages),"states":len(statepages),"capitals":len(citypages),"specialist_directories":len(area_pages),"titles":len(titles),"warning_count":len(warn),"error_count":len(errors)},ensure_ascii=False,indent=2))
for v in errors:print("ERROR:",v)
for v in warn[:50]:print("WARN:",v)
if len(warn)>50:print(f"... plus {len(warn)-50} other warnings")
sys.exit(1 if errors else 0)
