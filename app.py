from flask import Flask, render_template, request
import requests as req
import json

app = Flask(__name__)

@app.route('/', methods=['GET',"POST"])
def index():

    if request.form == 'POST':

        cnpj = request.form['cnpj']
        nome = request.form['nome']
        
        retorno = req.get(f'https://viacep.com.br/ws/{cnpj}/json/')
        json.loads(retorno.text)

    return render_template('index.html', nome, cnpj)

if __name__ == '__main__':
    app.run(debug=True)