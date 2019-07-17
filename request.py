from flask import Flask, jsonify, request
from score import *
from corretor import *

app = Flask(__name__)

@app.route('/score', methods=['GET', 'POST'])

def scores():
	if (request.method == 'POST'):
		json = request.get_json()
		frases = json['frases']
		return jsonify(score(frases, identifica, corretor_frase))
	else:
		frase = [request.args.get('frase')]
		return jsonify(score(frase, identifica, corretor_frase))

@app.route('/score/filtro', methods=['GET', 'POST'])

def filter():
	if (request.method == 'POST'):
		json = request.get_json()
		frases = json['frases']
		operador = json['operador']
		valor = json['valor']
		return jsonify(filtro(score(frases, identifica, corretor_frase),operador,valor))

	else:
		frases = request.args.get('frases')
		operador = request.args.get('operador')
		valor = request.args.get('valor', type=float)
		return jsonify(filtro(score(frases.split("$$"), identifica, corretor_frase),operador,valor))



if __name__ == '__main__':
	app.run(debug=True)