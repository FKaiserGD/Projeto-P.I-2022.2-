from app import app
from app.models import User
from flask_login import login_user, logout_user
from flask import render_template, request, redirect, url_for, flash


@app.route("/", methods=["GET"])
def home():
    return render_template("testeHome.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        CPF = request.form['CPF']
        Nome = request.form['Nome']
        Sobrenome = request.form['Sobrenome']
        Email = request.form['Email']
        Telefone = request.form['Telefone']
        Senha = request.form['Senha']
        Usuario = User(CPF, Nome, Sobrenome, Email, Telefone, Senha)
        Usuario.adicionarBanco()

        return redirect(url_for('login'))

    return render_template("teste.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        Email = request.form['EmailLogin']
        Senha = request.form['SenhaLogin']

        if not User.verificarEmail(Email) or not User.validarSenha(Email, Senha):
            return redirect(url_for('login'))
        else:
            DadosUsuario = User.buscarUsuarioPorEmail(Email)
            Usuario = User(DadosUsuario[0], DadosUsuario[1], DadosUsuario[2], DadosUsuario[3], DadosUsuario[4], DadosUsuario[5])
            login_user(Usuario)
            return redirect(url_for('home'))

    return render_template("testeLogin.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

app.run(debug=True)