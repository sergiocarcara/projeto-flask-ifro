# appFlask_v5.py — Página de login (visual)

Quinta versão: adiciona a **rota `/login`**, renderiza `t_index.html` com um parâmetro `nome` e mantém o dicionário em `t_usuario.html`.

## Rotas

| Rota | Template renderizado | Observação |
| --- | --- | --- |
| `/ola` | `homepage.html` | Apenas visual de demonstração |
| `/ola/<id>` | `homepage_nome.html` | Arquivos não presentes em `t_templates` nesta entrega |
| `/` | `t_index.html` | Passa `nome = "Turma 2025"`; também responde em `/index` |
| `/index` | `t_index.html` | |
| `/contato` | `t_contato.html` | |
| `/usuario` | `t_usuario.html` | Passa o dicionário `dados` |
| `/usuario/<p_nome>/<p_profissao>/<p_disciplina>` | `usuario.html` | Arquivo disponível é `t_usuario.html` |
| `/login` | `t_login.html` | Formulário de login (somente visual, sem funcionalidade) |

## Como executar

```bash
pip install flask
python appFlask_v5.py
```

Porta **7000** (execução direta) ou **6000** (se importado).

Acesse `http://localhost:7000`.