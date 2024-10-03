from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route("/", methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        idade = request.form['idade']
        
        try:
            datetime.strptime(data_nascimento, "%d/%m/%Y")  # Valida a data de nascimento
            idade = int(idade)  # Converte a idade para inteiro
            if idade < 0:
                raise ValueError("A idade deve ser maior que 0.")
        except ValueError:
            flash("Data de nascimento inválida. Use o formato DD/MM/AAAA.")
            return redirect(url_for('cadastro'))
        
    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)