import os
import sys

from src.blockchaincode import BlockManager

from flask import Flask, redirect, url_for, render_template, request


root_folder = os.path.abspath(os.path.dirname(os.path.dirname((__file__))))
sys.path.append(root_folder)

app = Flask(__name__)
chain = []
blockchain = BlockManager(chain)


@app.route("/")
def index():
    return redirect(url_for('registrar'))

@app.route('/registrar', methods=['GET'])
def registrar():
    return render_template('registrar.html')

@app.route('/registro', methods=['POST', 'GET'])
def registro():
    if request.method == 'POST':
        email = request.form['email']
        motivo = request.form['motivo']
        archivo = request.form['archivo']
        
        print(email, motivo, archivo)
        return render_template('registro completo.html', email=email)
    
@app.route('/detalle')
def validar():
    return render_template('validacion.html')