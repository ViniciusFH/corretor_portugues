from flask import Flask, jsonify
from score import *
from corretor import *

app = Flask(__name__)

@app.route('/<frases>', methods=['GET'])

def request_score(frases):
	return jsonify(score(frases.split("+"), identifica, corretor_frase))

@app.route('/filtro/<operador>/<float:valor>/<frases>', methods=['GET'])

def request_filtro(frases, operador, valor):
	return jsonify(filtro(score(frases.split("+"), identifica, corretor_frase),operador,valor))


app.run()