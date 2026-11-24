# Comprar TCC Brasil — edição editorial V4

Branch: comprartccbrasil-v4-design-editorial

Esta versão evolui a produção RC1 sem alterar o EiPassei ou o domínio hospedado. Os 100 endereços canônicos indexáveis e a página utilitária /obrigado/ noindex permanecem na arquitetura.

## Identidade
- Home: título Comprar TCC Brasil | Assessoria para TCC e Monografia.
- Nome visível no H1: COMPRAR TCC BRASIL.
- WebSite.name e Organization.name: Comprar TCC Brasil; alternateName: Comprar TCC BR.
- Orçamento integrado à primeira dobra, em vez de direcionar todas as pessoas para outro URL.
- Um único encaminhamento de formulário para o WhatsApp fornecido, sem registrar mensagens no servidor estático.
- Unidade de Curitiba, São Paulo e Rio de Janeiro conforme confirmação do proprietário.

## Redesenho
- Tipografia, espaçamentos e cores tratados por sistema de design documentado em DESIGN.md.
- Foram removidos os painéis flutuantes, órbitas decorativas e visuais genéricos da primeira dobra.
- A home usa uma composição editorial de proposta comercial + formulário; seções posteriores mostram critérios e cobertura por quadros técnicos.
- CSS sem novas dependências ou fontes externas; regras responsivas para telas menores.
- Menu mobile, CTA de orçamento e formulário compartilham a mesma identidade.

## Validação técnica
- HTML e JSON-LD nas páginas alteradas verificados em leitura do código.
- Links de navegação relativos preservados; contato encaminhado ao WhatsApp 55 41 985015076.
- A home e /orcamento/ usam o mesmo script de envio, validação nativa e aceite LGPD.
- O número no script não aparece no conteúdo visível nem em Schema.org, mas é acessível a qualquer pessoa com acesso ao código, portanto não é um segredo técnico.
- Dados estruturados não garantem escolha do nome pelo Google nem estrelas nas buscas; dependem do rastreamento e da interpretação do Google.

## Publicação e medições
O repositório contém os arquivos para a próxima implantação. Não houve publicação no domínio, envio ao Search Console nem teste real Lighthouse.
Testar no navegador resoluções 360/390/430/768/1280, menu, foco, campos, consentimento, envio WhatsApp e métricas LCP/INP/CLS antes de considerar a operação validada em produção.

Docs consultados: https://developers.google.com/search/docs/appearance/site-names
