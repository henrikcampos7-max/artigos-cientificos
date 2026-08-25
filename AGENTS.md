# Instruções para agentes

Estas regras se aplicam a todo o repositório.

## Missão

Apoiar criação, auditoria e edição científica reprodutível em farmácia oncológica sem fabricar evidência, ocultar uso de IA ou publicar material confidencial.

## Regras obrigatórias

- Trabalhar em branch temática e entregar mudanças por pull request; não editar `main` diretamente.
- Ler `GOVERNANCA_CIENTIFICA.md`, `ORIENTACOES.md` e `SQUAD.md` antes de alterar conteúdo científico.
- Nunca inventar busca, número de registros, resultado, citação, DOI, credencial, autoria, afiliação, aprovação ética ou dado clínico.
- Usar apenas dados fictícios em exemplos e testes. Não copiar prontuários, prescrições, nomes, identificadores ou datas de pacientes.
- Não submeter artigo, aceitar termos, pagar taxa, enviar e-mail editorial ou publicar manuscrito sem ação humana explícita.
- Não usar detector de IA ou “humanizador” como critério de qualidade.
- Não declarar uma referência “validada” somente porque o DOI existe; verificar o apoio da fonte à alegação.
- Manter PDFs e DOCX de terceiros fora do Git até confirmar licença e direitos.
- Preservar arquivos originais. Para artigo publicado, produzir errata separada; não substituir silenciosamente o PDF editorial.
- Não incluir e-mail pessoal, endereço residencial, credenciais não confirmadas, tokens, cookies ou segredos.

## Tarefas por periódico

Quando o usuário indicar uma revista-alvo:

1. ler `skills/preparar-artigo-para-revista/SKILL.md`;
2. resolver o nome ou alias com `python scripts/resolver_revista.py "REVISTA"`;
3. ler somente o perfil indicado e `journal_profiles/GUIA_VOZ_AUTORAL.md`;
4. verificar as instruções oficiais atuais antes de considerar o manuscrito pronto;
5. começar por uma análise de lacunas e manter separadas regras oficiais, padrões observados e decisões autorais.

## Fluxo Git

1. `git status --short --branch`
2. criar ou usar branch temática;
3. fazer mudanças pequenas e auditáveis;
4. executar `python scripts/validar_repositorio.py`;
5. revisar `git diff --check` e o diff completo;
6. adicionar somente arquivos intencionais, nunca `git add -A` em checkout misto;
7. abrir PR para revisão humana e verificar CI.

## Portão científico

Mudanças de conteúdo clínico ou metodológico exigem no PR:

- origem da afirmação;
- status de leitura do texto integral;
- impacto da mudança;
- revisor humano responsável;
- limitações e pendências.

Se qualquer item estiver ausente, manter o conteúdo como rascunho não validado.
