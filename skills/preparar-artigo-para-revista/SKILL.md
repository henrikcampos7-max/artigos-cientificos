---
name: preparar-artigo-para-revista
description: Analisa lacunas e adapta manuscritos científicos de farmácia, saúde pública ou oncologia a um periódico catalogado, sem inventar evidências nem ocultar uso de IA.
---

# Preparar artigo para revista

Use esta skill quando o usuário indicar uma revista-alvo ou pedir adequação editorial de um artigo científico nas áreas catalogadas.

## Roteamento

1. Resolva o nome, sigla ou alias com `python scripts/resolver_revista.py "REVISTA"` ou consulte `journal_profiles/CATALOGO.json`.
2. Leia o perfil indicado pelo campo `profile` e o `journal_profiles/GUIA_VOZ_AUTORAL.md`.
3. Para regras que possam ter mudado, confira a página oficial antes de apresentar a versão como pronta para submissão.
4. Se a revista não estiver catalogada, crie primeiro uma ficha provisória baseada em fontes oficiais e identifique claramente o que ainda precisa ser confirmado.

## Resultado esperado

Comece por uma análise de lacunas entre o manuscrito real e o tipo de artigo escolhido. Depois, quando autorizado, adapte estrutura, resumo, terminologia, citações, declarações e arquivos.

Preserve conteúdo científico e alterações autorais existentes. Não transforme revisão narrativa em sistemática, nem estudo descritivo em avaliação de impacto, sem método e dados reais.

## Limites obrigatórios

- Não invente dados, busca, seleção, estatística, aprovação ética, registro, afiliação, ORCID, autoria, contribuição, conflito, financiamento ou referência.
- Não use “humanizador”, erro proposital, paráfrase evasiva ou detector de IA como critério de autoria.
- Não afirme que uma referência apoia a alegação sem verificação do texto integral por pessoa responsável.
- Registre internamente o uso de IA e siga a política vigente do periódico para a declaração externa.
- Não submeta o manuscrito, aceite termos, pague taxas ou envie dados a terceiros sem autorização específica.
- Mantenha dados de pacientes, pareceres e manuscritos confidenciais fora do repositório público.

## Entrega

Informe:

- regras oficiais aplicadas e data da consulta;
- padrões observados usados apenas como orientação;
- alterações realizadas;
- pendências científicas, clínicas, éticas, linguísticas e documentais;
- revisão humana necessária antes da submissão.
