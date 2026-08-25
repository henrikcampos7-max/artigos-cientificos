# Perfis editoriais de periódicos

Biblioteca reutilizável para adaptar, com revisão humana, artigos científicos de farmácia, assistência farmacêutica, saúde pública e oncologia às exigências de periódicos específicos.

Os perfis não são modelos para copiar frases. Cada um separa:

1. **regra oficial**, extraída da página do periódico;
2. **padrão observado**, inferido de uma amostra recente de publicações e identificado como tal;
3. **decisão autoral**, que deve ser tomada e aprovada pelos autores reais.

## Como usar

1. Consulte o [catálogo](CATALOGO.json) pelo nome completo, sigla ou alias da revista. No repositório, `python scripts/resolver_revista.py "SIGLA"` faz essa resolução de forma determinística.
2. Abra somente o perfil escolhido.
3. Confirme a página oficial de autores na data da preparação ou submissão.
4. Compare o tipo real do estudo com os tipos aceitos pelo periódico.
5. Aplique o [guia de voz autoral](GUIA_VOZ_AUTORAL.md) sem inventar dados, método ou interpretação.
6. Registre as regras verificadas e as decisões editoriais no diretório privado do manuscrito.
7. Submeta somente após revisão científica, clínica, ética, linguística e autoral humana.

Exemplo de pedido futuro:

> Prepare este manuscrito para a Revista Brasileira de Cancerologia, como artigo original. Primeiro faça uma análise de lacunas; não invente dados nem altere conclusões.

## Escopo da seleção

- `nacional/`: periódicos brasileiros de farmácia, oncologia e saúde coletiva;
- `internacional/`: periódicos internacionais de farmácia clínica, hospitalar, social e oncologia;
- `avaliadas/`: periódicos já usados ou solicitados pelo autor, mantidos com a diligência editorial correspondente. A presença nesta pasta não é endosso.

“Mais conceituada” não é tratada como ranking absoluto. A seleção considera aderência temática, vínculo com sociedade ou instituição científica, maturidade editorial, transparência das instruções e utilidade para farmacêuticos. Métricas, indexação, taxas e políticas mudam; devem ser confirmadas novamente.

Para uma revista ainda não catalogada, use o [modelo de perfil](../templates/PERFIL_REVISTA.md), pesquise fontes oficiais, acrescente o registro ao catálogo e valide o repositório. O perfil deve permanecer provisório até revisão humana.

## Limites

- Nenhum perfil garante aceitação.
- A biblioteca não autoriza submissão automática.
- Padrão observado em artigos não substitui instrução oficial.
- Não se usa “humanização” para ocultar IA ou burlar detector. Busca-se autoria real, proveniência, precisão e responsabilidade humana.
- Políticas de IA variam por periódico. O registro interno do uso permanece obrigatório conforme a [governança científica](../GOVERNANCA_CIENTIFICA.md).

Última revisão da biblioteca: **24 de agosto de 2026**.
