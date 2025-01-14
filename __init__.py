from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/') #a
def hello_world(): 
    return render_template('hello.html')

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        token_bytes = token.encode()  # Conversion str -> bytes
        valeur = f.decrypt(token_bytes)  # Décrypte le token
        return f"Valeur décryptée : {valeur.decode()}"  # Retourne la valeur en str
    except Exception as e:
        return f"Erreur de décryptage : {str(e)}"
                                                                                                                  
if __name__ == "__main__":
  app.run(debug=True)


@app.route('/ex1') #a
def ex1(): 
    return render_template('ex1.html')
@app.route('/ex2') #a
def ex2(): 
    return render_template('ex2.html')
@app.route('/ex3') #a
def ex3(): 
    return render_template('Ex3.html')
@app.route('/ex4') #a
def ex4(): 
    return render_template('ex4.html')
@app.route('/ex5') #a
def ex5(): 
    return render_template('ex5.html')
@app.route('/sommaire') #a
def sommaire(): 
    return render_template('sommaire.html')
@app.route('/accueil') #a
def accueil(): 
    return render_template('accueil.html')
@app.route('/svg') #a
def svg(): 
    return render_template('svg.html')
@app.route('/maison_svg') #a
def maison_svg(): 
    return render_template('maison_svg.html')
