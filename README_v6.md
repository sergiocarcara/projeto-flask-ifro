# appFlask_v6.py — Recebendo dados do formulário (GET/POST)

Sexta versão: adiciona a rota **`/autenticar`** que recebe os campos `nome_usuario` e `senha` do formulário de login, tanto por **POST** (formulário) quanto por **GET** (query string), e devolve os valores recebidos como texto.

## Rotas

| Rota | Métodos | Comportamento |
| --- | --- | --- |
| `/ola` | GET | Template `homepage.html` (demonstração) |
| `/ola/<id>` | GET | Template `homepage_nome.html` |
| `/` e `/index` | GET | Template `t_index.html` com `nome = "Turma 2025"` |
| `/contato` | GET | Template `t_contato.html` |
| `/usuario` | GET | Template `t_usuario.html` com o dicionário `dados` |
| `/usuario/<p_nome>/<p_profissao>/<p_disciplina>` | GET | Template `usuario.html` |
| `/login` | GET | Template `t_login.html` (formulário de login) |
| `/autenticar` | GET e POST | Lê `nome_usuario` e `senha` e retorna: `usuario: ... e senha: ... recebidos com sucesso!` |

> O formulário de login (`t_login.html`) envia os dados para `/autenticar`; o valor é apenas ecoado de volta na tela (validação só chega na v7).

## Como executar

```bash
pip install flask
python appFlask_v6.py
```

Porta **7000** (execução direta) ou **6000** (se importado).

Acesse `http://localhost:7000`.