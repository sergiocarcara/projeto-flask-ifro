from flask import Flask, render_template
from flask import request   #para trabalhar com os métodos GET e POST
from flask import flash     #para msgs popup
from flask import redirect  #para redirecionar páginas


# os templates coloca em outra pasta. 
# Por padrão, fica na pasta templates e não precisa informar no template_folder,
# mas se quiser armazenar em outra pasta indique nesse parâmetro.
sergio_app = Flask(__name__, template_folder='t_templates') 
# no caso de usar flash pede a configuração de uma chave secreta
sergio_app.config['SECRET_KEY'] = "palavra-secreta-IFRO"


@sergio_app.route("/")       #se no navegador digitar / ou /index
@sergio_app.route("/index")  
def index():
    return render_template ("t_index.html") #optei por prefixar com t_ os nomes dos arquivos que usam template

@sergio_app.route("/contato")
def contato():
    return render_template("t_contato.html") 

#rota /usuarios COM passagem de argumentos
@sergio_app.route("/usuario/<nome_usuario>;<nome_profissao>")
#rota /usuarios SEM passagem de argumentos --> definir valor padrão com defaults
@sergio_app.route("/usuario", defaults={"nome_usuario":"usuário?","nome_profissao":""})  

def dados_usuario (nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina":"Desenvolvimento Web III"}
    return render_template ("t_usuario.html", nome=nome_usuario, dados = dados_usu)  

#new
@sergio_app.route("/login")
def login():
    return render_template("t_login_flash_js_cadastro.html")
    
#new
"""++++
Para poder recuperar os argumentos passados nos parâmetros na URL precisa importar o pacote
from flask import request

Também precisa colocar que essa página aceita requisições de tipo GET ou POST
O GET é padrão, mas no caso do POST altere no html method="POST"
"""
@sergio_app.route("/autenticar", methods=['GET', 'POST']) 
def autenticar():
    #método POST - pega nos fields (campos) do formulário
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('senha')
    
    if usuario == "admin" and senha == "ifro":
        return f"usuario: {usuario} e senha: {senha}"
    else:
        #para não dar msg. na outra página, vamos manter na própria página com flash
        #adicionar import flash
        flash("Dados inválidos!")
        flash("Login ou senha inválidos!")
        return redirect ('/login') #adicionar import redirect


if __name__ == "__main__": 
     sergio_app.run(port = 8000) 
     