const {chromium}=require("playwright");
const {spawn}=require("node:child_process");
const fs=require("node:fs");
const assert=require("node:assert/strict");
const BASE="http://127.0.0.1:8765/";
const server=spawn("python3",["-m","http.server","8765","--bind","127.0.0.1"],{stdio:"ignore"});
const sizes=[360,390,430,768,1280];const results=[];let browser;
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function check(url, page, label) {
 const resp=await page.goto(BASE+url,{waitUntil:"networkidle",timeout:30000});
 assert.equal(resp.status(),200,"HTTP 200: "+url);
 const r=await page.evaluate(()=>{
   const e=document.documentElement;
   return {w:innerWidth,scroll:e.scrollWidth,h1:document.querySelectorAll("h1").length,
   title:document.title,form:!!document.querySelector("#home-lead-form"),brand:document.body.innerText.includes("COMPRAR TCC BRASIL")};
 });
 assert(r.scroll<=r.w+2,"horizontal overflow "+label+": "+JSON.stringify(r));
 assert.equal(r.h1,1,"H1 count "+label);return r;
}
(async()=>{
 for(let n=0;n<30;n++){try{const r=await fetch(BASE);if(r.ok)break;}catch{}await sleep(300)}
 browser=await chromium.launch({headless:true,args:["--no-sandbox"]});
 fs.mkdirSync("qa-screenshots",{recursive:true});
 for(const width of sizes){
  const page=await browser.newPage({viewport:{width,height:800},deviceScaleFactor:1});
  const errors=[];page.on("pageerror",x=>errors.push(x.message));
  const r=await check("index.html",page,"home "+width);
  assert(r.form,"form in home "+width);assert(r.brand,"brand visible "+width);
  if(width===390||width===1280)await page.screenshot({path:"qa-screenshots/home-"+width+".png",fullPage:true});
  if(width<=430){
   const button=page.locator(".menu-toggle");await button.click();
   assert.equal(await button.getAttribute("aria-expanded"),"true");
   assert(await page.locator("#mobile-menu").isVisible());
  }
  assert.equal(errors.length,0,"JS errors "+width+": "+errors.join(";"));
  results.push({page:"home",width,status:"PASS",...r});await page.close();
 }
 const page=await browser.newPage({viewport:{width:390,height:844}});
 for(const url of ["orcamento/index.html","professores/direito/index.html","atendimento/salvador/index.html","privacidade/index.html"]){
  let r=await check(url,page,url);
  results.push({page:url,status:"PASS",...r});
 }
 await check("index.html",page,"lead-test");
 await page.route("https://wa.me/**",route=>route.fulfill({status:200,contentType:"text/plain",body:"QA placeholder, do not send"}));
 const form=page.locator("#home-lead-form");
 await form.locator("input[name=nome]").fill("Cliente Teste");
 await form.locator("select[name=area]").selectOption({label:"Direito"});
 await form.locator("select[name=servico]").selectOption({label:"Metodologia científica"});
 await form.locator("input[name=aceite_privacidade]").check();
 const reqPromise=page.waitForRequest(req=>req.url().startsWith("https://wa.me/"),{timeout:15000});
 await form.locator("button[type=submit]").click();
 const req=await reqPromise;
 const u=new URL(req.url());assert.equal(u.pathname,"/5541985015076");
 assert(u.searchParams.get("text").includes("Cliente Teste"));
 assert(u.searchParams.get("text").includes("Metodologia científica"));
 results.push({test:"form-submit",status:"PASS",destination:"wa.me/5541985015076",content:"nome/serviço preenchidos"});
 await page.close();await browser.close();
 fs.writeFileSync("qa-screenshots/results.json",JSON.stringify(results,null,2));
 console.log("VISUAL_QA_PASS",JSON.stringify(results));
})().catch(async e=>{console.error("VISUAL_QA_FAIL",e.stack||e);if(browser)await browser.close();process.exitCode=1}).finally(()=>server.kill("SIGTERM"));
