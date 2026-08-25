# Artigos científicos em farmácia oncológica

[![Qualidade do repositório](https://github.com/henrikcampos7-max/artigos-cientificos/actions/workflows/quality.yml/badge.svg)](https://github.com/henrikcampos7-max/artigos-cientificos/actions/workflows/quality.yml)

Repositório público de governança, auditoria e fluxos reprodutíveis para criação e revisão de artigos científicos. Ele não é um depósito automático de manuscritos em preparação nem substitui revisão metodológica, clínica, ética ou editorial humana.

## Estado verificado em 24 de agosto de 2026

- quatro publicações IJAERS únicas com Paulo Henrique Campos da Silva entre os coautores;
- 63 DOCX gerados em lote, classificados como **rascunhos não validados**, e não como artigos publicados;
- um manuscrito de revisão sistemática mais desenvolvido, ainda pendente de correções metodológicas, editoriais, de privacidade e de credenciais;
- uma biblioteca editorial com perfis nacionais e internacionais, regras de citação, estruturas, políticas de IA e amostras estilísticas recentes;
- uma skill versionada para resolver o nome da revista e conduzir uma análise de lacunas antes da adaptação;
- arquivos-fonte locais preservados fora deste repositório público até confirmação de autoria, licença, política de preprint e ausência de dados pessoais ou confidenciais.

Os achados completos estão na [auditoria do acervo](docs/AUDITORIA_ACERVO_2026-08-23.md) e na [diligência da IJAERS](docs/DILIGENCIA_IJAERS_2026-08-23.md).

## Princípios

1. IA não é autora e não substitui responsabilidade humana.
2. Não se oculta uso de IA nem se tenta burlar detectores; registra-se como a ferramenta foi usada e quem revisou o resultado.
3. Nenhum dado, resultado, busca bibliográfica, credencial, afiliação ou contribuição pode ser inventado.
4. Afirmações clínicas exigem fonte adequada e revisão de profissional qualificado.
5. Referência localizada não é referência validada: é preciso confirmar que o texto integral sustenta a alegação.
6. Manuscritos não são submetidos nem publicados automaticamente.
7. Dados de pacientes, pareceres confidenciais, segredos e documentos de terceiros não entram no Git.

## Navegação

- [Orientações editoriais](ORIENTACOES.md)
- [Governança científica](GOVERNANCA_CIENTIFICA.md)
- [Fluxo da squad](SQUAD.md)
- [Contribuição e revisão](CONTRIBUTING.md)
- [Auditoria do acervo](docs/AUDITORIA_ACERVO_2026-08-23.md)
- [Diligência da IJAERS](docs/DILIGENCIA_IJAERS_2026-08-23.md)
- [Inventário dos 63 rascunhos](docs/INVENTARIO_RASCUNHOS_2026-08-23.csv)
- [Modelos de trabalho](templates/)
- [Biblioteca de perfis editoriais](journal_profiles/)
- [Catálogo de revistas e aliases](journal_profiles/CATALOGO.json)
- [Guia de voz autoral autêntica](journal_profiles/GUIA_VOZ_AUTORAL.md)
- [Skill para preparação por revista](skills/preparar-artigo-para-revista/SKILL.md)
- [Esquema de metadados](schemas/article-metadata.schema.json)
- [Política de licenças](LICENSES/README.md)

## Estrutura prevista para artigos aprovados

```text
articles/<slug>/
  README.md
  metadata.json
  protocol/
  search/
  evidence/
  manuscript/
  reviews/
  publication/
```

O diretório `publication/` recebe apenas arquivos cuja redistribuição esteja autorizada. Quando a licença não permitir o PDF editorial, registra-se somente DOI, metadados, citação e link oficial.

## Revista-alvo

Nenhuma revista é alvo padrão. O [catálogo editorial](journal_profiles/CATALOGO.json) distingue referências temáticas, periódicos amplos, alvos aspiracionais de alta seletividade e revistas que exigem diligência reforçada. A classificação orienta a análise de aderência; não constitui ranking, endosso nem promessa de aceite.

A IJAERS permanece na categoria de diligência reforçada. Suas regras e limitações estão em perfil próprio e devem ser confirmadas novamente antes de qualquer submissão.

Pedidos futuros podem usar nome, sigla ou alias, por exemplo: “prepare para JOPP” ou “adapte para a Revista Brasileira de Cancerologia”. A primeira entrega deve ser uma análise de lacunas; nenhuma adaptação pode inventar etapas, dados ou credenciais.

## Validação local

```powershell
python scripts/validar_repositorio.py
```

Para auditar um acervo DOCX sem modificá-lo:

```powershell
python -m pip install -r requirements-audit.txt
python scripts/auditar_docx.py "C:\caminho\do\acervo" --csv auditoria.csv
```

O relatório automático é triagem. Ele não verifica sozinho a veracidade científica, o texto integral, retratações, autoria ou adequação clínica.
