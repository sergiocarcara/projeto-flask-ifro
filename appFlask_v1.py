from flask import Flask

sergio_app = Flask(__name__)

@sergio_app.route('/')
@sergio_app.route('/ola')
def raiz():   #esta função está vinculada a rota raiz e a rota /ola
    return 'Olá, Turma 2025!'

@sergio_app.route('/contato')
def contato():
    return 'e-mail:mariela@ifro.edu.br'

@sergio_app.route('/rota2')
def rota2():
    resposta = "<H3>Olá, Turma 2025! </H3>" 
    resposta += "<H4> sou a rota 2 </H4>"  #concatena string com o operador += montando uma resposta em HTML
    return resposta


#esta função não está vinculado a rota, mas pode ser usada dentro de uma rota ou outra função ou invocada de fora
def saudacaoes(nome): 
    return f"Boa noite, {nome}!. Tudo bem?"

#maiores detalhes nos slides que estão no AVA.
if __name__ == '__main__':  #verifica se o arquivo está sendo executado diretamente, e não importado
    sergio_app.run(port=7000)

sergio_app.run( port=6000)    #executa caso o o arquivo seja importado, mas não é uma boa prática, pois pode gerar conflito de portas