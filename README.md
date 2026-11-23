# Comprar TCC Brasil — V3 em construção

Esta branch mantém a V2 e acrescenta fluxo de orçamento com destino ao WhatsApp, locais físicos informados pelo responsável, 96 linhas de especialização de professores e textos de pesquisa para estados e capitais. **Nenhuma página está liberada para indexação.**

Consulte [SEO-AUDITORIA-V3.md](SEO-AUDITORIA-V3.md) para requisitos de publicação. Telefone em JavaScript não é sigiloso no repositório público; não está incluído no HTML de contato nem no Schema.

# Comprar TCC Brasil — V2 SEO e experiência

V2 com novo posicionamento, melhorias na experiência mobile, marcação semântica, páginas de monografia e avaliações, professores próprios e arquitetura territorial.

**PRÉVIA NÃO INDEXÁVEL**: o formulário não envia dados; professores e depoimentos aguardam cadastro real; todas as páginas possuem noindex. Consulte SEO-AUDITORIA-V2.md antes do lançamento.

# Comprar TCC Brasil — protótipo completo v1

Site estático responsivo, em português, criado após estudo público de MyStudyBay e Comprar TCC e Monografia. Projeto completamente independente do EiPassei; nenhum post foi migrado.

## Abrir localmente

Abra `index.html` no navegador. As ligações internas apontam para arquivos `index.html` das respectivas pastas, permitindo navegar sem servidor. Para testar via HTTP: `python -m http.server 8000` e entre em `http://localhost:8000/`.

## Estrutura

- Página inicial com posicionamento comercial e explicação da assessoria ética.
- 7 serviços, 8 áreas, 27 capitais, 4 guias e páginas institucionais.
- Diretório de professores sem nomes inventados; CSV com 12 cadastros por área (96 espaços).
- FAQ, termos, política de privacidade, integridade, candidatura e formulário de orçamento demonstrativo.
- SEO por página: títulos, descrições, canonicals de domínio final, Open Graph, BreadcrumbList e dados Organization / WebSite / Service / Article quando pertinentes.
- sitemap.xml pronto para produção. Cada capital: noindex até conteúdo realmente diferenciado.

## IMPORTANTE — PRÉ-LANÇAMENTO

**TODAS as páginas estão em `noindex,follow` e `robots.txt` está com `Disallow: /`**. Isto é intencional: a razão social, CNPJ, titulares de perfis, contato, infraestrutura de formulário e práticas de privacidade ainda não foram confirmados. **Nunca publique para indexação sem resolver esse checklist.**

### Checklist para ficar operacional

1. Confirmar propriedade/registro do domínio e configurar HTTPS, www → apex 301 e DNS.
2. Inserir nome legal, CNPJ, contato e canais reais em institucional, LGPD, termos e dados estruturados.
3. Validar equipe, qualificações e autorização específica de foto/bio; preencher CSV. Só então publicar `Person` Schema em páginas individuais reais.
4. Implementar canal de recebimento seguro (Netlify Forms, backend ou CRM sob contrato LGPD), confirmar retenção, anti-spam e destinatário; `assets/site.js` bloqueia envio na demo. Não inclua documentos sensíveis sem infraestrutura apropriada.
5. Documentar e verificar operacionalmente o compromisso de **produção acadêmica sem IA generativa** com fornecedores/professores.
6. Verificar contratos, entregáveis e jurídico de assessoria ética. Não vender autoria terceirizada nem prometer aprovação.
7. Adicionar conteúdo editorial realmente singular por capital: dados locais verificados, atividades regionais e páginas úteis. Elas estão marcadas noindex até revisão; não prometer escritórios locais.
8. Em deploy de produção, retirar noindex **somente das páginas aprovadas**, trocar robots para Allow, revisar sitemap, verificar Rich Results Test e Search Console, testar envio e CWV mobile.
9. Configurar e medir Google Search Console, GA4 somente após definição de privacidade e consentimento aplicável; evitar depoimentos/métricas fictícias.

## Desempenho

Sem framework JS e fontes externas. Um CSS e um JS minúsculo, HTML pré-renderizado, responsividade e acessibilidade (skip-link, navegação teclado, reduced-motion, labels).

## Contagem de arquivos

70 arquivos na entrega inicial, incluindo este README.

## Referências examinadas

- https://mystudybay.com.br/
- https://www.comprartccemonografia.com/
- https://developers.google.com/search/docs/essentials/spam-policies
- https://developers.google.com/search/docs/appearance/structured-data/organization
- https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- https://www.gov.br/anpd/
