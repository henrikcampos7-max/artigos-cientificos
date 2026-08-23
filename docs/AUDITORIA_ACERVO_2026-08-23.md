# Auditoria do acervo científico — 23 de agosto de 2026

## Conclusão executiva

O acervo local contém publicações reais, referências de terceiros e um grande lote de rascunhos gerados. Esses grupos estavam misturados e não podiam ser tratados como um único conjunto de “artigos publicados”. A prioridade é preservar os originais, corrigir a classificação, reconstruir a trilha metodológica dos manuscritos escolhidos e submeter somente após revisão humana.

Não foi feita tentativa de ocultar uso de IA. O critério adotado foi autoria responsável: decisões intelectuais rastreáveis, fontes lidas, método executado, revisão especializada e declaração de ferramentas.

## Escopo e método da auditoria

Fonte local analisada em modo somente leitura: pasta `ARTIGOS PUBLICADOS` no computador do autor. Nenhum arquivo-fonte foi alterado ou enviado ao GitHub.

Foram usados:

- inventário por extensão, tamanho e hash;
- extração de texto e metadados de PDF e DOCX;
- inspeção visual das 33 páginas dos cinco PDFs de conteúdo único;
- auditoria automática dos 63 DOCX quanto a palavras, referências estimadas, DOI, anos, seções, limitações e metadados;
- leitura aprofundada do artigo de câncer de próstata, do manuscrito sistemático e de amostras dos rascunhos;
- comparação com instruções oficiais da IJAERS e boas práticas de IA e revisão sistemática.

Dois DOCX estavam bloqueados por outro processo e não puderam ser abertos: o manual de publicação na IJAERS e o manuscrito sobre estabilidade pós-reconstituição/pós-diluição. A renderização visual dos DOCX também não pôde ser concluída porque o LibreOffice não estava disponível; a auditoria estrutural e textual foi mantida. Esses limites impedem uma conclusão final sobre o layout de Word.

## Inventário

| Tipo | Quantidade | Classificação |
|---|---:|---|
| PDF | 7 | 5 conteúdos únicos; quatro publicações IJAERS do usuário e um artigo Springer de terceiros |
| DOCX | 68 | 63 rascunhos em lote, três documentos principais e dois arquivos do fluxo de verificação |
| Markdown | 6 | registros de execução, pesquisa, rascunho e verificações |
| JSON | 1 | estado de execução da squad |
| **Total** | **82** |  |

## Publicações IJAERS identificadas

Quatro conteúdos únicos têm Paulo Henrique Campos da Silva entre os coautores:

| DOI | Tema resumido | Data | Observação |
|---|---|---|---|
| [10.22161/ijaers.91.31](https://doi.org/10.22161/ijaers.91.31) | cuidado na atenção primária a pessoas com diabetes e hipertensão | jan. 2022 | publicação identificada |
| [10.22161/ijaers.92.33](https://doi.org/10.22161/ijaers.92.33) | papel dos profissionais no câncer de próstata | fev. 2022 | três cópias locais idênticas |
| [10.22161/ijaers.95.39](https://doi.org/10.22161/ijaers.95.39) | atuação de enfermagem em central de material esterilizado | maio 2022 | publicação identificada |
| [10.22161/ijaers.99.50](https://doi.org/10.22161/ijaers.99.50) | assistência em pré-eclâmpsia/eclâmpsia | set. 2022 | incoerência grave entre título e resumo |

O PDF sobre N-acetilcisteína e lesão hepática induzida por quimioterapia é de Nilgun Eroglu e colaboradores, publicado pela Springer, e não é uma publicação do usuário. Ele deve permanecer apenas como referência privada ou link bibliográfico, salvo autorização de redistribuição.

### Duplicatas

Os três arquivos locais do artigo de câncer de próstata têm o mesmo SHA-256:

```text
79c9c1c8bde0b6e5c0d89b9069ceeaaf4d235be54e848d0b990d18d680f53ed5
```

A duplicação deve ser resolvida fora do Git, preservando uma cópia canônica e um inventário. Nenhum PDF foi apagado nesta auditoria.

## Artigo de câncer de próstata

Página oficial: [The role of health professionals in the care of patients with prostate cancer: Literature review](https://ijaers.com/detail/the-role-of-health-professionals-in-the-care-of-patients-with-prostate-cancer-literature-review/).

### Problemas científicos e editoriais

- O título promete uma revisão específica sobre câncer de próstata, mas partes extensas discutem quimioterapia, envelhecimento, câncer do colo do útero, vacinação e outros temas sem conexão clara com a pergunta.
- O resumo alterna um estudo concluído com linguagem de futuro e descreve uma “população” de homens idosos apesar de o desenho ser bibliográfico.
- O método informa análise de 14 artigos, mas não apresenta estratégias por base, datas exatas, deduplicação, seleção, extração, tabela dos estudos, avaliação crítica ou protocolo.
- A lista tem 14 referências, porém inclui documentos que não são artigos científicos, em tensão com a descrição do método.
- Há citações no texto sem correspondência clara na lista e referências incompletas.
- O texto contém afirmações factualmente impossíveis e problemas de edição/tradução que deveriam ter sido interceptados.
- Não há seções próprias de resultados e discussão, embora as instruções atuais da IJAERS as listem.
- A conclusão faz recomendações sem mostrar como foram derivadas dos estudos, sem força da evidência e sem limitações proporcionais.
- Há 25 autores e nenhuma declaração de contribuição no PDF. A autoria precisa ser documentada com critérios e CRediT.
- O HTML da revista exibe nomes com codificação quebrada; o depósito Crossref também apresenta inconsistências nos nomes.

### Ação recomendada

Preservar o PDF e criar errata separada. Solicitar à revista correção de metadados, nomes e erros factuais; não substituir silenciosamente o artigo publicado. O artigo não deve ser usado como modelo metodológico para novos trabalhos.

## Outras publicações

O PDF `10.22161/ijaers.99.50` apresenta incoerência editorial importante: o título e o corpo tratam de pré-eclâmpsia/eclâmpsia, enquanto o resumo, o objetivo e as palavras-chave falam de diabetes e hipertensão na atenção primária. O cabeçalho indica tradução por serviço automático. Recomenda-se errata formal e revisão dos metadados.

Os demais PDFs IJAERS também exigem checagem individual de citações, autoria e qualidade; a publicação anterior não comprova que todos os elementos científicos foram corretamente revisados.

## Lote de 63 rascunhos DOCX

### Resultado automático

| Indicador | Resultado |
|---|---:|
| Documentos | 63 |
| Palavras totais | 178.969 |
| Palavras por arquivo | 2.303–3.548; mediana 2.867 |
| Referências estimadas | 957 |
| Referências por arquivo | 8–22; mediana 15 |
| DOI únicos por documento, somados | 449 |
| Documentos sem DOI na lista | 21 |
| Tabelas | 0 |
| Documentos que mencionam limitações | 13 |
| Documentos sem menção identificável de limitações | 50 |
| Documentos que afirmam revisão narrativa | 62 |
| Documentos que também usam a expressão “revisão sistemática” | 8 |
| Metadado de autor | `python-docx` nos 63 |

O estimador de referências recentes encontrou proporções de 0% a 55,6%, mediana de 11,1%. Esse indicador é apenas triagem: anos podem ser ambíguos e atualidade não deve ser reduzida a uma cota fixa. O achado relevante é a incompatibilidade entre a afirmação repetida de que 2021–2026 foi priorizado e as bibliografias predominantemente anteriores, sem estratégia ou seleção arquivada.

### Riscos do lote

- Os documentos foram produzidos em lote com arquitetura, extensão e parágrafo metodológico quase padronizados.
- Não há, no repositório, consultas completas, exportações, deduplicação, decisões de inclusão ou matrizes de evidência que comprovem as buscas descritas.
- Vários títulos prometem desenvolvimento, validação, prevalência, impacto, modelo preditivo ou avaliação institucional, mas o método é revisão narrativa. Isso pode induzir o leitor a acreditar que houve estudo empírico.
- Há números e recomendações clínicas que precisam ser rastreados até o texto integral e revisados por especialista.
- Os metadados internos usam `python-docx`, data fixa de 2013, título/assunto vazios e e-mail pessoal. Isso não prova falta de autoria, mas revela geração automatizada e metadados inadequados para submissão.
- Parte das referências contém anotações “verificar”, que devem permanecer como pendências privadas, não como bibliografia final.
- A repetição textual reduz voz autoral e pode mascarar ausência de decisão científica específica por tema.

### Classificação

Todos os 63 arquivos permanecem `rascunho_nao_validado`. O [inventário completo](INVENTARIO_RASCUNHOS_2026-08-23.csv) documenta as métricas por arquivo. Não se recomenda publicar os DOCX no repositório público ou submetê-los em lote.

## Manuscrito `ARTIGO-REVISAO-SISTEMATICA-JHPHS.docx`

É o manuscrito mais desenvolvido, com cerca de 7.485 palavras, duas tabelas, uma figura e aproximadamente 40 referências. Ainda não está pronto:

- o rótulo “Original Article” conflita com revisão sistemática;
- resumo, palavras-chave e blocos de autoria aparecem duplicados;
- a numeração final contém duplicações;
- a busca e o processo de seleção não demonstram dois revisores independentes;
- o protocolo não foi registrado e a avaliação de risco de viés é descrita como adaptada;
- há endereço completo, e-mail, ORCID pendente e credenciais a validar;
- afirmações de estabilidade de antineoplásicos são clinicamente sensíveis e exigem revisão farmacêutica humana e fontes primárias atuais.

## Relatório de plágio do fluxo anterior

O arquivo usa amostra de frases na web e comparação local por n-gramas. Isso não sustenta as conclusões “não apresenta plágio” ou “inferior a 1%”. Também classifica incorretamente o acervo ao atribuir ao usuário o artigo Springer. O relatório deve ser tratado como inválido para submissão e substituído por avaliação de similaridade apropriada com interpretação humana.

## Plano priorizado

### P0 — integridade e segurança

1. separar publicados, rascunhos e referências de terceiros;
2. remover duplicatas somente após cópia de segurança e confirmação humana;
3. não publicar os 63 DOCX nem o PDF Springer;
4. revisar autoria, afiliação, titulação, ORCID, endereço, e-mail e consentimento;
5. manter dados de pacientes e documentos confidenciais fora do Git;
6. usar branch e PR com revisão humana.

### P1 — recuperação científica

1. escolher um único manuscrito piloto;
2. alinhar título, pergunta e desenho;
3. reconstruir ou executar a busca com registro completo;
4. montar matriz de evidência e alegações;
5. revisar todas as afirmações clínicas e quantitativas;
6. documentar limitações, autoria, conflitos, financiamento e uso de IA.

### P2 — publicação

1. avaliar revistas por escopo e credibilidade, sem alvo automático;
2. adaptar formato somente após estabilizar o conteúdo;
3. confirmar licença e política de preprint;
4. obter aprovação de todos os autores;
5. realizar submissão manual.

## Limites desta auditoria

A auditoria não substitui revisão sistemática de cada tema, validação clínica de cada recomendação, software institucional de similaridade, confirmação de autoria pelos coautores, parecer jurídico sobre direitos autorais ou revisão ética. Nenhum artigo foi corrigido ou submetido nesta etapa.
