from flask import Flask, jsonify, request
import sys
sys.path.insert(0, "score_portugues")
import score


app = Flask(__name__)

@app.route('/score', methods=['GET', 'POST'])

def scores():
	if (request.method == 'POST'):
		json = request.get_json()
		frases = json['frases']
		return jsonify(score.score(frases))
	else:
		frase = [request.args.get('frase')]
		return jsonify(score.score(frase))

@app.route('/score/filtro', methods=['GET', 'POST'])

def filter():
	if (request.method == 'POST'):
		json = request.get_json()
		frases = json['frases']
		operador = json['operador']
		valor = json['valor']
		return jsonify(score.filtro(score.score(frases),operador,valor))

	else:
		frases = request.args.get('frases')
		operador = request.args.get('operador')
		valor = request.args.get('valor', type=float)
		return jsonify(score.filtro(score.score(frases.split("$$")),operador,valor))

@app.route('/score/sort', methods=['GET', 'POST'])

def sort():
	if (request.method == 'POST'):
		json = request.get_json()
		frases = json['frases']
		ordem = json['ordem']
		return jsonify(score.sort(score.score(frases),ordem))

	else:
		frases = request.args.get('frases')
		ordem = request.args.get('ordem')
		return jsonify(score.sort(score.score(frases.split("$$")),ordem))


if __name__ == '__main__':
	app.run(debug=True)
	# app.run(host= '0.0.0.0')