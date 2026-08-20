# Orientações para Geração de Artigos Científicos

> Documento consolidado para orientar a produção dos próximos artigos científicos
> da farmácia oncológica, revisado em 2026-08-19 após reorientação do processo.
> Autor: Paulo Henrique Campos da Silva — FACIMED — Cacoal, RO, Brasil.
> Revista-alvo padrão: IJAERS (ISSN 2349-6495/2456-1908, Qualis A2).

---

## 1. Princípio de autoria

O objetivo é gerar artigos **cientificamente defensáveis e com autoria perceptível** —
não "textos que enganam detector de IA". Um texto com resultado, interpretação e
consequência clínica reais é a melhor resposta a qualquer detector.

- O texto deve conter **resultado + interpretação + consequência clínica**.
- Frases genéricas ("A atuação do farmacêutico oncológico é de extrema importância...")
  não têm autoria: poderiam estar em qualquer manuscrito. Evitar.
- O opencode estrutura, organiza e revisa; a interpretação, os dados e as decisões
  metodológicas são do autor.

**Exemplo de redação autoral:**

> "No período analisado, as intervenções relacionadas à dose e ao esquema terapêutico
> concentraram a maior proporção das inconformidades identificadas antes da manipulação.
> Esse achado sugere que a validação farmacêutica exerce função particularmente relevante
> na etapa prévia ao preparo do antineoplásico, quando ainda é possível corrigir a
> prescrição sem exposição do paciente ao erro."

## 2. Referências

1. **Todas reais e verificadas**: DOI confirmado via CrossRef API
   (`api.crossref.org/works/{DOI}`) OU localização confirmada via PubMed/base de origem.
   Nenhuma referência sem status VERIFICADA/CORRIGIDA entra no artigo.
2. **Atualidade**: mínimo **60% das referências de 2021–2026**. Obras clássicas
   (pré-2020) apenas para contextualização histórica de conceitos fundamentais.
3. **Metadados completos**: autores (sobrenome + iniciais), ano, título exato,
   periódico, volume(número):páginas, DOI.
4. **Autoridade**: priorizar revisões sistemáticas, meta-análises, diretrizes de
   sociedades (NCCN, ASCO, ISOPP, CPIC) e documentos oficiais (WHO, Anvisa, MS).
5. **Cobertura**: 15–40 referências por artigo; todas citadas no texto; sem
   referências "fantasma" (na lista sem citação) e sem citações sem referência.

## 3. Metodologia honesta

A seção de métodos descreve **exatamente o que foi feito**, sem parecer mais
rigorosa do que é:

- Revisão narrativa: bases consultadas (PubMed, SciELO, LILACS/BVS, Google Scholar),
  palavras-chave/descritores DeCS/MeSH, período, critérios de inclusão/exclusão e
  total de trabalhos selecionados.
- **SEM** fluxograma PRISMA, avaliação de risco de viés ou contagens de
  triagem/duplicatas — a menos que o processo sistemático tenha sido realmente
  executado e documentado.
- Exemplo: "Foi realizada revisão narrativa da literatura com busca nas bases
  PubMed, SciELO e LILACS, priorizando publicações dos últimos cinco anos. Estudos
  anteriores foram utilizados quando considerados referências fundamentais."

## 4. Discussão e considerações

- Comparar achados/argumentos com **estudos específicos** (autor, ano, desenho,
  achado principal) — nunca "diversos estudos demonstram".
- Números e intervalos com origem indicada (de qual estudo cada valor foi extraído).
- **Sem superlativos insustentáveis**: evitar "a intervenção de maior custo-benefício
  disponível"; usar "importante estratégia de segurança passível de implementação".
- Toda afirmação precisa de referência correspondente. Afirmação sem fonte
  ("Estudos brasileiros relatam...") = corrigir ou remover.
- Incluir **limitações reais e proporcionais** ao desenho do estudo.

## 5. Redação — o que evitar (padrões de texto genérico)

Frases que não devem aparecer (ou no máximo uma vez, com contexto):

- "Esses achados convergem para a recomendação de que..."
- "Diante desse cenário, este artigo teve como objetivo..."
- "A literatura analisada confirma que..."
- "A atuação do farmacêutico é de extrema importância para garantir a segurança e a eficácia..."

Também evitar:

- Padrão mecânico repetido em parágrafos sucessivos:
  "estudo A mostrou X → estudo B mostrou Y → esses achados demonstram → recomendação".
- Resumo excessivamente "perfeito" e previsível (períodos de tamanho e construção
  muito semelhantes).
- Afirmações categóricas sem demonstrar de onde os valores foram construídos.

**NUNCA**: usar ferramentas de "humanizar IA", trocar palavras aleatoriamente ou
introduzir erros propositais.

## 6. Declaração de uso de IA

Se a revista ou instituição exigir, declarar o uso conforme a política editorial.
O uso de IA para estruturação e revisão é declarado; o conteúdo, a interpretação e
as decisões metodológicas são do autor.

## 7. Estrutura padrão (IJAERS)

1. Título (claro, direto) + versão em inglês
2. Autor: Paulo Henrique Campos da Silva (único) — FACIMED — Cacoal, RO, Brasil
3. Resumo (180–260 palavras, fluxo contínuo) + Palavras-chave (3–6)
4. ABSTRACT + Keywords
5. I. INTRODUÇÃO (3–4 parágrafos; último parágrafo com objetivo explícito)
6. II. MATERIAIS E MÉTODOS (revisão: bases, descritores, janela 2021–2026, critérios)
7. III. REVISÃO DE LITERATURA (3–5 subseções temáticas, texto crítico-analítico)
8. IV. CONSIDERAÇÕES FINAIS (síntese, implicações práticas, perspectivas)
9. AGRADECIMENTOS (se houver)
10. REFERÊNCIAS (numeradas em ordem alfabética, Vancouver/ABNT adaptado com DOI/URL)

Formatação IJAERS: margens 1" sup/inf e 0,64" esq/dir; título 24 pt; autor 16 pt;
afiliação 10 pt; espaçamento 1,15. Plágio < 10% (IJAERS rejeita > 30%).

## 8. Aprendizados do lote de 63 artigos (verificação de 957 referências)

Resultado da verificação CrossRef + PubMed:

| Categoria | Quantidade | Ação |
|---|---|---|
| Verificadas OK no CrossRef | 700 | Nenhuma |
| Confirmadas no PubMed | 76 | Conferir volume/páginas |
| Documentos reais sem DOI (livros, guidelines, RDC, bulas) | 166 | Confirmar URL/acesso |
| Exigem correção manual | 15 | Corrigir título/periódico/ano |

Lições aplicadas:

1. **15 referências precisaram correção manual** (título/DOI trocados). Sempre
   conferir título oficial no CrossRef antes de citar.
2. **Artigos clássicos dominavam a bibliografia** de vários temas (2001–2018) —
   daí a regra de 60% de referências 2021–2026.
3. Documentos oficiais (ISOPP Standards, NCCN, CTCAE, bulas, RDC) existem e são
   verificáveis por URL, mesmo sem DOI CrossRef.
4. Cada artigo deve trazer **NOTA METODOLÓGICA** (não publicar) listando qualquer
   dado incerto que exija verificação antes da submissão.

## 9. Fluxo de produção (squad artigos-cientificos)

1. **Foco** — tema, tipo (revisão/original), idioma, restrição de período.
2. **Pesquisa** — 4+ bases, descritores DeCS/MeSH, ≥60% refs 2021–2026.
3. **Verificação** — 100% das referências via CrossRef/PubMed (VERIFICADA/CORRIGIDA/NÃO LOCALIZADA).
4. **Redação** — aplicando as orientações deste documento.
5. **Aprovação** — revisão do usuário (aprovar/feedback/abortar).
6. **Consolidação** — formatação IJAERS + checklist de submissão + declaração de IA.

## 10. Checklist de submissão (IJAERS)

- [ ] Plágio < 10% (software de plágio antes de enviar)
- [ ] Todas as referências citadas no texto e verificadas (CrossRef/PubMed)
- [ ] ≥60% das referências de 2021–2026
- [ ] Metodologia honesta (sem aparência de sistemática em revisão narrativa)
- [ ] Discussão com comparações a estudos específicos
- [ ] Limitações reais presentes
- [ ] Sem frases genéricas de IA e sem superlativos insustentáveis
- [ ] Formato IJAERS (margens, fontes, espaçamento, seções)
- [ ] Resumo + palavras-chave (PT/EN)
- [ ] Declaração de uso de IA (se exigida pela política editorial)
- [ ] Autor correspondente: Paulo Henrique Campos da Silva (henrikcampos7@gmail.com)
- [ ] Arquivo em .doc/.docx/.pdf
- [ ] Copyright form após aceite
- [ ] Submissão: editor.ijaers@gmail.com / https://ijaers.com/submit-paper/