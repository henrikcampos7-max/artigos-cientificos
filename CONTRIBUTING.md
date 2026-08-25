# Como contribuir

## Antes de começar

Leia `AGENTS.md`, `GOVERNANCA_CIENTIFICA.md` e `ORIENTACOES.md`. Mudanças científicas devem ser pequenas, rastreáveis e revisáveis.

## Branch e pull request

1. crie uma branch temática;
2. não misture conteúdo científico, infraestrutura e arquivos binários sem necessidade;
3. execute `python scripts/validar_repositorio.py`;
4. execute `git diff --check` e revise o diff;
5. faça commit somente dos arquivos intencionais;
6. abra PR e aguarde revisão humana e CI.

## O PR deve informar

- problema corrigido;
- arquivos e artigos afetados;
- fontes ou evidências consultadas;
- se houve leitura do texto integral;
- impacto clínico/metodológico;
- dados pessoais/licenças revisados;
- uso de IA e revisão humana;
- testes executados e pendências.

## Não aceite no Git

- dados de pacientes ou identificadores;
- segredos, cookies, tokens ou arquivos `.env`;
- PDFs/DOCX de terceiros sem licença confirmada;
- pareceres ou cartas editoriais confidenciais;
- credenciais, afiliações ou contribuições não confirmadas;
- resultados, contagens ou buscas reconstruídos por suposição;
- arquivos temporários do Office.
