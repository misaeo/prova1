from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
@app.route("/", methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        idade = request.form['idade']
        try:
            idade = int(idade)
            if idade < 0:
                raise ValueError("A idade deve ser maior que 0.")
            # Redireciona para a página de resultado passando os dados
            return redirect(url_for('resultado', nome=nome, data_nascimento=data_nascimento, idade=idade))
        except ValueError:
            flash("Dados inválidos. Por favor, tente novamente.")
            return redirect(url_for('cadastro'))
    return render_template("cadastro.html")
@app.route("/resultado")
def resultado():
    nome = request.args.get('nome')
    data_nascimento = request.args.get('data_nascimento')
    idade = request.args.get('idade')
    return render_template("resultado.html", nome=nome, data_nascimento=data_nascimento, idade=idade)
@app.route("/sucesso")
def sucesso():
    return render_template("sucesso.html")
if __name__ == "__main__":
    app.run(debug=True)