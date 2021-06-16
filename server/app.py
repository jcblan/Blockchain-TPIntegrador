import os
import sys

from flask import Flask, redirect, url_for, render_template

root_folder = os.path.abspath(os.path.dirname(os.path.dirname((__file__))))
sys.path.append(root_folder)

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('registrar'))

@app.route('/registrar')
def registrar():
    return render_template('registrar.html')