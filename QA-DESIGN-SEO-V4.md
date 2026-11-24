# Validação técnica e editorial — Comprar TCC Brasil V4
Data: 24 de novembro de 2026
Branch: comprartccbrasil-v4-design-editorial

## O que foi aplicado
- Hero comercial substituído por layout editorial e formulário integrado.
- H1, title, descrição, WebSite.name e Organization.name consistentes com Comprar TCC Brasil.
- Marca gráfica BR substituiu o antigo ícone abstrato.
- Formulários da home e /orcamento/ compartilham validação de campos e destino de WhatsApp, sem backend de armazenamento de solicitações.
- Novo sistema visual documentado em DESIGN.md, inspirado metodologicamente em Onlook, OpenDesign e GitHub Replica, sem copiar código ou layout desses projetos.
- Quadro de critérios e cobertura substituiu os mockups ornamentais da home.
- Textos principais de professores, FAQ, estados, capitais e monografia corrigidos para remover afirmações antigas.
- 96 descrições de especialidades específicas reescritas nas oito áreas do diretório.
- Sitemap da base de produção permanece com 100 URLs canônicas.

## Testes realizados na leitura do GitHub
1. Home: exatamente um H1, título de 53 caracteres, descrição de 126 caracteres, canonical HTTPS da home, meta index e três blocos JSON-LD parseáveis.
2. Páginas monografia, professores, perguntas frequentes, atendimento, estados, avaliações e orçamento: títulos, descrições, H1, canonicals e JSON-LD conferidos; nenhum link interno inexistente na amostra verificada.
3. Professores: atualização confirmada para 12 especialidades de cada uma das oito áreas; verificação amostral das páginas Administração, Direito e Tecnologia da Informação sem repetição da frase anterior.
4. Auditoria de texto no main das 101 páginas: zero ocorrências do conjunto pesquisado de avisos antigos de pré-lançamento, diretórios em validação, perfis em cadastro e bloqueios editoriais de indexação. Trata-se de uma varredura por padrões, não de revisão humana linha a linha das 101 páginas.
5. Sitemap: 100 URLs distintas; a única página utilitária excluída é /obrigado/.
6. CSS e JavaScript: presença das classes do formulário e dos dois seletores de formulários confirmada por inspeção estática. Workflow foi ajustado para incluir node --check, dependente de execução do GitHub Actions.

## O que ainda exige teste real
- Layout renderizado nas resoluções 360, 390, 430, 768 e 1280 px, contrastes, zoom e acessibilidade.
- Teste ponta a ponta do encaminhamento WhatsApp em navegadores iOS/Android e desktop.
- Core Web Vitals, Lighthouse mobile, LCP, INP e CLS com o site publicado.
- Validação de dados estruturados em Rich Results Test pela URL real, HTTPS/DNS/301, Google Search Console, indexação e ranqueamento.
- Disponibilidade e registro dos domínios propostos para o site de estágios no Registro.br e busca de marca no INPI.
- Nomes, títulos e depoimentos reais que o proprietário ainda fornecerá. Não inventar profissionais ou avaliações.

## Conclusão
A versão V4 está pronta para conferência editorial e publicação técnica com os arquivos no repositório. A auditoria estática dos itens testados não encontrou falhas. Isso não equivale a certificação de produção ao vivo nem a garantia de ranqueamento no Google.
