# Projeto Flask — Desenvolvimento Web III

Repositório do projeto da disciplina **Desenvolvimento Web III** (IFRO), com um aplicativo web em **Flask** desenvolvido em **7 versões evolutivas** — da primeira página de texto até um fluxo de login funcional com mensagens flash.

## Sobre a aplicação

O projeto acompanha o aprendizado de Flask passo a passo:

1. **v1** — rotas respondendo com texto puro e HTML em string;
2. **v2** — introdução ao `render_template`;
3. **v3** — rotas dinâmicas com parâmetros na URL;
4. **v4** — organização dos templates em pasta própria (`t_templates`);
5. **v5** — página de login (visual);
6. **v6** — recebimento de dados de formulário (GET/POST);
7. **v7** — versão final: login com validação, mensagens `flash`, `redirect` e `SECRET_KEY`.

## Estrutura do projeto

```text
appFlask_v1.py ... appFlask_v7.py   # versões da aplicação
importando.py                       # exemplo de importação
static/                             # CSS e JavaScript (inclui busca de clima via OpenWeatherMap)
templates/                          # templates das primeiras versões (v1-v3)
t_templates/                        # templates das versões com prefixo t_ (v4-v7)
README_v1.md ... README_v7.md       # documentação individual de cada versão
```

## Requisitos

- **Python 3**
- **Flask**

```bash
pip install flask
```

## Como executar

```bash
python appFlask_v7.py        # versão final — acesse http://localhost:8000
```

Para testar as outras versões, execute o arquivo correspondente (a porta pode variar por versão — verifique o `README_vN.md`):

| Versão | Porta | Destaque |
| --- | --- | --- |
| v1 | 7000 | rotas de texto |
| v2 | 7000 | templates |
| v3 | 7000 | parâmetros na URL |
| v4 | 7000 | pasta `t_templates` |
| v5 | 7000 | página de login |
| v6 | 7000 | formulário GET/POST |
| v7 | 8000 | login com flash e redirect |

## Créditos e observações

- Projeto acadêmico — IFRO (4º Período, Desenvolvimento Web III).
- A chave da API do OpenWeatherMap foi **removida** do código público; substitua `SUA_CHAVE_API_AQUI` em `static/js/script2.js` pela sua chave.
- Usuário/senha da versão v7 são para demonstração (ver `README_v7.md`).