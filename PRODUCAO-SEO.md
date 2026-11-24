# Comprar TCC Brasil — release candidate de produção (24/11/2026)

Esta branch foi preparada para indexação **quando publicada no domínio definitivo**. Não houve publicação automática, envio ao Google nem modificação do EiPassei.

## Arquitetura e indexação
- 101 páginas HTML: 100 URLs indexáveis e uma URL utilitária /obrigado/ (noindex).
- 27 unidades federativas (26 estados e DF), 27 capitais e oito diretórios de especialidades.
- Canonical HTTPS autorreferente; meta robots index,follow,max-image-preview:large nas páginas indexáveis.
- Sitemap com 100 URLs canônicas; robots.txt com Allow: / e referência ao sitemap.
- netlify.toml opcional para hospedagem Netlify e redirecionamento www → domínio principal.
- Validação estática pelo script scripts/seo_audit.py e workflow GitHub Actions.

## Três unidades próprias conforme confirmação pelo proprietário
- Curitiba: Rua XV de Novembro, 120, apartamento 41; Paraná, Brasil.
- São Paulo: Praça da Sé, 120; São Paulo, Brasil.
- Rio de Janeiro: Praia de Botafogo, 300; Rio de Janeiro, Brasil.
A confirmação do proprietário não equivale a verificação externa de titularidade ou validação no Perfil da Empresa do Google. Reuniões presenciais mediante agendamento.

## Dados estruturados e ética
- Organization/WebSite na home; WebPage, CollectionPage, BreadcrumbList, Service, Article, Place e ItemList em páginas pertinentes.
- Sem AggregateRating fictício; estrelas autogerenciadas por Organization/LocalBusiness não geram snippet de avaliação no Google.
- Especialidades dos professores descritas, mas sem inventar nomes e currículos individuais; publicar Person/ProfilePage só depois de perfis reais autorizados.
- A promessa de atendimento sem IA generativa refere-se à produção acadêmica contratada, não à tecnologia empregada para construir o site.
- Página local deve oferecer conteúdo útil de fato; a repetição de ofertas pode ser considerada doorway abuse mesmo com textos distintos. A criação e indexação por si só não garantem ranking.

## Validações que dependem do site efetivamente online
- DNS, domínio próprio, HTTPS, 301 www e resposta HTTP 200 por URL.
- Rich Results Test de URLs, Search Console, indexação efetiva e métricas de tráfego.
- Lighthouse/PSI e Core Web Vitals mobile: LCP, INP, CLS.
- Teste real do formulário e encaminhamento ao WhatsApp com usuário.
- Confirmação de dados legais/CNPJ, termos, políticas e detalhes de atendimento.
- Elegibilidade de cada unidade para Perfil da Empresa Google (presença, sinalização e equipe).

## Comandos
Execute python3 scripts/seo_audit.py na raiz do projeto para testar estrutura SEO.

## Próximos passos da publicação
1. Conectar domínio à hospedagem e configurar HTTPS/301.
2. Executar auditoria e validar jurídico, identidade empresarial, professores, atendimento e navegação.
3. Testar Google Rich Results Test, Core Web Vitals e formulário no domínio.
4. Submeter https://comprartccbrasil.com.br/sitemap.xml ao Google Search Console.

Fontes oficiais:
https://developers.google.com/search/docs/essentials/spam-policies
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag
https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
https://developers.google.com/search/docs/appearance/structured-data/review-snippet
https://support.google.com/business/answer/3038177
