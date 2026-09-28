# appFlask_v7.py — Versão final (login com flash e redirect)

Sétima e última versão: implementa o **login funcional** com mensagens **flash**, redirecionamento e chave secreta. É a versão mais completa do projeto.

## Destaques

- Pasta de templates em `t_templates/`.
- `SECRET_KEY` configurada — obrigatória para usar mensagens `flash`.
- Rota `/usuario` com **valores padrão** (`defaults`) para quando a URL não tiver argumentos.
- Login que valida usuário/senha e usa `flash` + `redirect` para manter a mensagem na própria página.

## Rotas

| Rota | Métodos | Comportamento |
| --- | --- | --- |
| `/` e `/index` | GET | Template `t_index.html` |
| `/contato` | GET | Template `t_contato.html` |
| `/usuario/<nome_usuario>;<nome_profissao>` | GET | Template `t_usuario.html` com os parâmetros da URL |
| `/usuario` (sem argumentos) | GET | Mesmo template usando os **valores padrão** (`usuário?` e `""`) |
| `/login` | GET | Template `t_login_flash_js_cadastro.html` (formulário com validação JS) |
| `/autenticar` | GET e POST | Valida o login; retorna usuário/senha se forem `admin`/`ifro`, senão exibe mensagens flash e redireciona para `/login` |

## Credenciais de teste

```text
usuário: admin
senha:   ifro
```

> **Importante:** usuário e senha estão fixos no código apenas para demonstração em sala de aula. Em produção, nunca deixe credenciais no código-fonte — use variáveis de ambiente e uma base de dados segura.

## Como executar

```bash
pip install flask
python appFlask_v7.py
```

Roda na porta **8000**.

Acesse `http://localhost:8000`.