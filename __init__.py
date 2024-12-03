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

@app.route('/decrypt/', methods=['POST'])
def decrypt():
    try:
        # Récupérer les données chiffrées depuis la requête
        encrypted_data = request.json.get('encrypted_data')
        if not encrypted_data:
            return jsonify({'error': 'Données chiffrées manquantes'}), 400

        # Déchiffrer les données
        decrypted_data = cipher_suite.decrypt(encrypted_data.encode()).decode()

        # Retourner les données déchiffrées
        return jsonify({'decrypted_data': decrypted_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
