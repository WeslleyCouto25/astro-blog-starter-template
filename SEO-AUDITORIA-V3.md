# Comprar TCC Brasil — Checklist de construção V3
Revisão em 23/11/2026. **Projeto não publicado no domínio definitivo; páginas continuam noindex.**

## Contato por WhatsApp
- O formulário utiliza validação nativa de campos obrigatórios, autorização do usuário e JavaScript para preparar uma mensagem de orçamento.
- O destino configurado é 55 (Brasil) + 41 (DDD) + número fornecido pelo responsável. Não incluímos o número no JSON-LD nem na redação visível.
- **Não é segredo técnico:** o destino fica legível no JavaScript do repositório público. Ocultação real requer serviço intermediário no servidor, com controle de acesso e políticas próprias.
- O usuário é redirecionado para wa.me e confirma o envio no aplicativo. Dados digitados podem ser processados pelo WhatsApp/Meta conforme seus próprios termos; não são armazenados pelo nosso site estático.
- Com JavaScript desativado o botão permanece desabilitado para evitar POST acidental.

## Endereços
- Organização: três endereços recebidos do responsável e visíveis na rota /unidades/.
- Home: propriedades Organization.address (PostalAddress) para Curitiba, São Paulo e Rio de Janeiro.
- Páginas das três cidades: tipo Place com PostalAddress, sem telefone, sem horários inventados e sem simulação de credenciamento Google.
- **Google Business Profile/LocalBusiness** condicionado a atendimento real com pessoal presente e regras oficiais de elegibilidade. A existência dos imóveis não comprova elegibilidade da empresa.
- Referência: https://support.google.com/business/answer/3038177 e https://developers.google.com/search/docs/appearance/structured-data/local-business

## Avaliações e perfis
- Diretório com 96 posições associadas a linhas de especialidade, sem criar nomes ou títulos fictícios; preencher /data/modelo-professores-96-slots.csv apenas após comprovação.
- Depoimentos seguem /data/modelo-depoimentos-verificados.csv; nunca importar ratings ou textos de uma empresa terceira e atribuí-los à nova marca.
- Review/aggregateRating self-serving de Organization e LocalBusiness não é elegível a estrelas no Google, mesmo com avaliações reais. Não usar marcação de estrela para simular elegibilidade.
- Referência: https://developers.google.com/search/docs/appearance/structured-data/review-snippet

## Páginas territoriais
- 27 estados/DF e 27 capitais, com roteiro de investigação específico armazenado em data/territorial-editorial.json.
- Projetos de pesquisa nas páginas são exemplos, não trabalhos completos ou resultados empíricos.
- Diferenças em temas e método ajudam o conteúdo, mas **não eliminam automaticamente** risco de doorway pages se proposta comercial e conteúdo principal continuarem repetitivos.
- Recomendo adicionar informações verificáveis locais, documentação de atividades reais, dúvidas recorrentes da região e serviços distintos onde existirem, antes de qualquer liberação de indexação.
- Política: https://developers.google.com/search/docs/essentials/spam-policies

## Verificação e lançamento (não realizado)
1. Verificar titularidade do domínio, HTTPS, redirecionamentos 301 (www), identidade legal, CNPJ, atendimento e dados jurídicos.
2. Validar os locais e endereços como escritórios operacionais, com elegibilidade local quando cabível. Não publicar horários não confirmados.
3. Cadastrar professores reais, seus currículos e consentimentos; publicar perfis e somente depois criar Person/ProfilePage.
4. Testar formulário no celular e desktop; confirmar dados e envio no WhatsApp; adicionar controles antispam se necessário.
5. Executar auditoria estática (scripts/seo_audit.py), testar Rich Results Test e validação Schema.org no domínio real.
6. Testar Lighthouse móvel, LCP, INP, CLS e acessibilidade. Métricas reais ainda não foram medidas.
7. Retirar noindex apenas das páginas aprovadas, atualizar sitemap apenas com URLs indexáveis e enviar ao Search Console.

## Auditoria de similaridade editorial (amostral)
Método de diagnóstico: extrair o texto visível da tag main de cada página, normalizar para minúsculas e calcular interseção/união de sequências únicas de 5 palavras (Jaccard de 5-gramas). Não é uma métrica do algoritmo do Google.

Medição na V3 após revisão do texto repetitivo:
- Fortaleza × Manaus: 0,457.
- Acre × Paraná: 0,490.
- Paraná × São Paulo (estados): 0,503.
- Curitiba × São Paulo (capitais): 0,581.

**Decisão:** não afirmar que as 54 páginas territoriais estão prontas para SEO. Elas permanecem noindex. O uso de tópicos regionais próprios ajuda, mas é necessário acrescentar evidências reais de atendimento, conteúdo local verificável, contexto de cursos e orientação genuína. O abuso de páginas de entrada é definido por função e conteúdo, não por limiar de similaridade.

## QA de amostra V3
Foram verificados na amostra a presença de H1 único, canonical autorreferente, noindex, JSON-LD parseável e tipos de marcação adequados nas páginas de home, formulário, unidades, capitais, estados e professores. Nas 12 URLs examinadas durante a rodada não foram encontrados erros nesses critérios. Isso não substitui auditoria integral nem testes de navegador.

**Não realizado:** Lighthouse mobile real, Rich Results Test online, teste real de envio por WhatsApp em navegador, verificação do endereço no Google Business Profile, validação de titularidade do domínio e contagem de avaliações reais.
