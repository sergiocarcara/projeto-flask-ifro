# appFlask_v1.py — Primeira versão (respostas de texto)

Primeira versão do projeto Flask: o servidor responde com **texto simples e HTML montado em string**, sem usar templates.

## Rotas

| Rota | Método | Retorno |
| --- | --- | --- |
| `/` | GET | `Olá, Turma 2025!` |
| `/ola` | GET | `Olá, Turma 2025!` |
| `/contato` | GET | `e-mail:sergiocarcara@gmail.com` |
| `/rota2` | GET | Página com `<H3>Olá, Turma 2025!</H3>` e `<H4>sou a rota 2</H4>` (HTML em string) |

## Funções auxiliares

- `saudacaoes(nome)` — função sem rota que retorna `Boa noite, {nome}!. Tudo bem?` (pode ser invocada de outras rotas).

## Como executar

```bash
pip install flask
python appFlask_v1.py
```

- Executado **diretamente**: roda na porta **7000**.
- Executado **importado** (ex.: `import appFlask_v1`): roda na porta **6000** (não é boa prática — pode conflitar com o servidor de desenvolvimento).

Acesse `http://localhost:7000`.
