import os
import sys

from src.blockchaincode import BlockManager, Bloque

from flask import Flask, redirect, url_for, render_template, request


root_folder = os.path.abspath(os.path.dirname(os.path.dirname((__file__))))
sys.path.append(root_folder)

app = Flask(__name__)
chain = []
blockchain = BlockManager(chain)
blockchain._crear_bloque_genesis_()


@app.route("/")
def index():
    return redirect(url_for('registrar'))

@app.route('/registrar', methods=['GET'])
def registrar():
    return render_template('registrar.html')

@app.route('/registro', methods=['POST'])
def registro():
    if request.method == 'POST':
        email = request.form['email']
        motivo = request.form['motivo']
        archivo = request.form['archivo']
        
        bloque = Bloque(email, motivo, archivo)
        blockchain.agregar_nuevo(bloque)
        hash = bloque.hash

        return render_template('registro completo.html', email=email, hash=hash)
    
    return render_template('registro completo.html')

@app.route('/detalle/<hash>', methods=['GET'])
def detalle(hash):
    bloque = blockchain.busqueda_hash(hash)
    if bloque != "none":
        email = bloque.email
        motivo = bloque.motive
        fecha = bloque.timestamp
        #fecha = "2021-04-19 20:48"
        return render_template('validacion.html', email = email, motivo = motivo, fecha = fecha)
    return render_template('registrar.html')