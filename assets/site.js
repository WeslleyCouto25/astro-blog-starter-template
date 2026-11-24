(()=>{"use strict";
const toggle=document.querySelector(".menu-toggle"),nav=document.querySelector("#mobile-menu");
if(toggle&&nav){toggle.addEventListener("click",()=>{const opened=toggle.getAttribute("aria-expanded")==="true";toggle.setAttribute("aria-expanded",String(!opened));toggle.setAttribute("aria-label",opened?"Abrir menu":"Fechar menu");nav.hidden=opened;});nav.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>{nav.hidden=true;toggle.setAttribute("aria-expanded","false");}));}
const phone=["55","41","985015076"].join("");
document.querySelectorAll("#lead-form, form[data-whatsapp-form]").forEach(form=>{
const button=form.querySelector("#whatsapp-submit,[data-whatsapp-submit]"),status=form.querySelector("[role='status']")||document.getElementById("form-notice");
if(button)button.disabled=false;
form.addEventListener("submit",event=>{
event.preventDefault();if(!form.reportValidity())return;
const data=new FormData(form);if(data.get("website"))return;
if(data.get("aceite_privacidade")!=="sim"){if(status)status.textContent="Confirme a política de privacidade.";return;}
const v=k=>String(data.get(k)||"").trim().slice(0,k==="descricao"?1000:160);
const parts=[["Nome",v("nome")],["E-mail",v("email")],["Contato",v("telefone")],["Curso ou área",v("area")],["Serviço",v("servico")],["Prazo",v("prazo")],["Descrição",v("descricao")]]
.filter(([,value])=>value).map(([name,value])=>name+": "+value);
const message=["Olá! Vim pelo site Comprar TCC Brasil e gostaria de um orçamento de assessoria acadêmica.","",...parts].join("\n");
if(status)status.textContent="Abrindo o WhatsApp. Confirme o envio no aplicativo.";
window.location.assign("https://wa.me/"+phone+"?text="+encodeURIComponent(message));
});});
})();