# appFlask_v2.py — Introdução ao render_template

Segunda versão: passa a usar **templates HTML** (pasta `templates/`) por meio de `render_template`, em vez de retornar strings.

## Rotas

| Rota | Template renderizado | Observação |
| --- | --- | --- |
| `/` | `homepage.html` | Também responde em `/ola` |
| `/ola` | `homepage.html` | |
| `/index` | `index.html` | |
| `/contato` | `contato.html` | |
| `/usuario` | `usuario.html` | Passa o dicionário `dados` (nome, profissão, disciplina) para o template |
| `/rota2` | `rota2.html` | **Atenção:** este arquivo não existe na pasta `templates/` nesta entrega |

## Como executar

```bash
pip install flask
python appFlask_v2.py
```

Porta **7000** (execução direta) ou **6000** (se importado).

Acesse `http://localhost:7000`.