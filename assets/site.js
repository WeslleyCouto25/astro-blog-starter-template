(()=>{"use strict";
const m=document.querySelector(".menu-toggle"),nav=document.querySelector("#mobile-menu");
if(m&&nav){m.addEventListener("click",()=>{const on=m.getAttribute("aria-expanded")==="true";m.setAttribute("aria-expanded",String(!on));nav.hidden=on;m.setAttribute("aria-label",on?"Abrir menu":"Fechar menu")});nav.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>{nav.hidden=true;m.setAttribute("aria-expanded","false")}))}
const f=document.querySelector("#lead-form");
if(f){
 const notice=document.querySelector("#form-notice");
 const submit=f.querySelector("#whatsapp-submit");if(submit)submit.disabled=false;
 f.addEventListener("submit",event=>{
  event.preventDefault();
  if(!f.reportValidity())return;
  const data=new FormData(f);
  if(data.get("website"))return;
  if(data.get("aceite_privacidade")!=="sim"){if(notice)notice.textContent="Confirme a leitura da política de privacidade e a comunicação via WhatsApp.";return}
  const value=k=>String(data.get(k)||"").trim();
  const message=["Olá! Vim pelo site Comprar TCC Brasil e gostaria de solicitar uma análise de assessoria acadêmica.",
   "Nome: "+value("nome"),"E-mail: "+value("email"),
   "Telefone informado: "+(value("telefone")||"Não informado"),
   "Área: "+value("area"),"Serviço: "+value("servico"),
   "Prazo: "+(value("prazo")||"A definir"),"Descrição: "+value("descricao")].join("\n");
  if(notice)notice.textContent="Abrindo seu aplicativo de WhatsApp. A mensagem será enviada somente depois da sua confirmação no WhatsApp.";
  const phone="55"+"41"+"985015076"; // Configuração de contato — nunca publicar em Schema.org.
  window.location.assign("https://wa.me/"+phone+"?text="+encodeURIComponent(message));
 });
}
})();