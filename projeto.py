from flask import Flask, render_template, request, redirect , session, flash

app = Flask(__name__)
app.secret_key="alura"

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('warframe', 'rpg', 'ps4')
jogo2 = Jogo('rocket league', 'futebol de carro', 'ps4')
jogo3 = Jogo('war thunder', 'guerra com veiculos', 'ps4')
lista = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    return render_template('lista.html', titulo='jogo', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='adicionar novo jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    
    novo_jogo = Jogo(nome, categoria, console)
    lista.append(novo_jogo)  
    
    return redirect ("/")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if "a"== request.form["senha"]:
        session["usuario logado"]= request.form["usuario"]
        flash( session["usuario logado"] + " logado com sucesso")
        return redirect("/novo")
    
    else:
        flash("usuario nao logado")
        return redirect("/login")


@app.route('/logout')
def logout():
    session["usuario logado"]=None
    flash("logout feito")
    return redirect("/")






if __name__ == '__main__':
    app.run()
