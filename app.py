from flask import Flask, render_template, request, redirect, session, flash



app = Flask(__name__)
app.secret_key = 'Senai'
class cadinfluecer:
    def __init__(self, nome, plataforma, seguidores, areas):
        self.nome = nome
        self.plataforma = plataforma
        self.seguidores = seguidores
        self.areas = areas
lista = []



@app.route('/influ')
def influ():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('influ.html', Titulo="Influenciers: ", Listainflu=lista)


@app.route('/cadastro')
def cadastro():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('cadastro.html', Titulo= "Cadastro Influencers")

@app.route("/criar", methods= ['POST'])
def criar():
    if 'salvar' in request.form:
        nome = request.form['nome']
        plataforma = request.form['plataforma']
        seguidores = request.form['seguidores']
        areas = request.form['areas']
        obj= cadinfluecer( nome, plataforma, seguidores, areas)
        lista.append(obj)
        return redirect('/influ')
    elif 'deslogar' in request.form:
        session.clear()
        return redirect('/')

@app.route('/excluir/<influencers>', methods=['GET', 'DELETE'])
def excluir(influencers):
    for i, inf in enumerate(lista):
        if inf.nome == influencers:
            lista.pop(i)
            break
    return redirect('/influ')

@app.route('/editar/<influencers>', methods= ['GET'])
def editar(influencers):
    for i, inf in enumerate (lista):
        if inf.nome == influencers:
            return render_template("Editar.html", influ= inf, Titulo= "Alterar Influenciador ")


@app.route('/alterar', methods= ['POST', 'PUT'])
def alterar():
    nome = request.form['nome']
    for i, inf in enumerate(lista):
        if inf.nome == nome:
            inf.plataforma = request.form['plataforma']
            inf.seguidores = request.form['seguidores']
            inf.areas = request.form['areas']
        return redirect('/influ')

@app.route('/')
def login():
    session.clear()
    return render_template('Login.html', Titulo='Faça Login')

@app.route('/autenticar', methods= ['POST'])
def autenticar():
    if request.form['usuario']== 'Bruno' and request.form ['senha']=='123':
        session ['Usuario_Logado'] = request.form['usuario']
        flash ('Usuario Logado com Sucesso')
        return redirect('/cadastro')
    else:
        flash('Usuario não encontrado')
        return redirect('/')

if __name__ == '__main__':
    app.run()
