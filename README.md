# Artigos científicos em farmácia oncológica

[![Qualidade do repositório](https://github.com/henrikcampos7-max/artigos-cientificos/actions/workflows/quality.yml/badge.svg)](https://github.com/henrikcampos7-max/artigos-cientificos/actions/workflows/quality.yml)

Repositório público de governança, auditoria e fluxos reprodutíveis para criação e revisão de artigos científicos. Ele não é um depósito automático de manuscritos em preparação nem substitui revisão metodológica, clínica, ética ou editorial humana.

## Estado verificado em 23 de agosto de 2026

- quatro publicações IJAERS únicas com Paulo Henrique Campos da Silva entre os coautores;
- 63 DOCX gerados em lote, classificados como **rascunhos não validados**, e não como artigos publicados;
- um manuscrito de revisão sistemática mais desenvolvido, ainda pendente de correções metodológicas, editoriais, de privacidade e de credenciais;
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

Nenhuma revista é alvo padrão. A IJAERS pode ser considerada somente após diligência atualizada de escopo, indexação, revisão, custos, preservação, direitos e política de IA. As instruções atuais da revista exigem seções de método, resultados, discussão e conclusão e referências em APA; essas regras podem mudar e devem ser consultadas novamente antes de cada submissão.

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
