from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
import crud
import graficos # type: ignore

app = Flask(__name__)


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="instituto_tamandua"
    )

@app.route('/')
def index():
    return render_template('../frontend/formulario.html')

@app.route('/', methods=['POST'])
def cadastrar():
    dados = {
        "nome": request.form['nome'],
        "data_nascimento": request.form['data_nascimento'],
        "email": request.form['email'],
        "telefone": request.form['telefone'],
        "instagram": request.form['instagram']
    }
    crud.inserir_inscricao(dados)
    return redirect(url_for('listar'))

@app.route('/listar')
def listar():
    registros = crud.listar_inscricoes()
    return render_template('listar.html', inscricoes=registros)

@app.route('/deletar/<int:id>')
def deletar(id):
    crud.deletar_inscricao(id)
    return redirect(url_for('listar'))

@app.route('/grafico')
def grafico():
    graficos.gerar_grafico()
    return '<h2>Gráfico gerado! Veja o arquivo grafico.png no diretório backend.</h2>'

if __name__ == '__main__':
    app.run(debug=True)

