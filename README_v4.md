# appFlask_v4.py — Modelo base com pastas separadas

Quarta versão: passa a usar `template_folder='t_templates'` (arquivos de template com prefixo `t_`), introduzindo arquivos `t_index.html` e `t_contato.html`.

## Rotas

| Rota | Template renderizado | Observação |
| --- | --- | --- |
| `/ola` | `homepage.html` | **Atenção:** o arquivo não está em `t_templates` nesta entrega |
| `/ola/<id>` | `homepage_nome.html` | Mesma observação acima |
| `/` | `t_index.html` | Também responde em `/index` |
| `/index` | `t_index.html` | |
| `/contato` | `t_contato.html` | |
| `/usuario` | `usuario.html` | Passa o dicionário `dados` (o arquivo disponível é `t_usuario.html`) |
| `/usuario/<p_nome>/<p_profissao>/<p_disciplina>` | `usuario.html` | Idem |

> **Importante:** a pasta de templates mudou para `t_templates`. Verifique se cada template realmente existe nessa pasta antes de executar (ex.: `homepage.html`, `homepage_nome.html` e `usuario.html` não estão listados em `t_templates/`; os arquivos disponíveis usam o prefixo `t_`).

## Como executar

```bash
pip install flask
python appFlask_v4.py
```

Porta **7000** (execução direta) ou **6000** (se importado).

Acesse `http://localhost:7000`.