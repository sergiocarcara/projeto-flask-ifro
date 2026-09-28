# appFlask_v3.py — Parâmetros dinâmicos na URL

Terceira versão: adiciona **rotas dinâmicas** (valores passados na própria URL), além dos templates da v2.

## Rotas

| Rota | Template renderizado | Observação |
| --- | --- | --- |
| `/` | `homepage.html` | Também responde em `/ola` |
| `/ola` | `homepage.html` | |
| `/ola/<id>` | `homepage_nome.html` | Passa o valor `id` da URL para o campo `{{campoNome}}` do template |
| `/index` | `index.html` | |
| `/contato` | `contato.html` | |
| `/usuario` | `usuario.html` | Passa o dicionário `dados` fixo |
| `/usuario/<p_nome>/<p_profissao>/<p_disciplina>` | `usuario.html` | Passa os 3 valores da URL como dicionário `dados` |
| `/rota2` | `rota2.html` | **Atenção:** este arquivo não existe na pasta `templates/` nesta entrega |

> Exemplo: acessar `/ola/Maria` exibe a homepage com o nome "Maria".

## Como executar

```bash
pip install flask
python appFlask_v3.py
```

Porta **7000** (execução direta) ou **6000** (se importado).

Acesse `http://localhost:7000`.