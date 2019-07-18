from flask import jsonify, request
from flask_restful import Resource
import peso

class Score(Resource):

        def get(self):
                if 'frases' in request.args:
                        frases = request.args.get('frases').split("$$")
                        if 'ordem' in request.args:
                                ordem = request.args.get('ordem')
                                return jsonify(peso.sort(peso.score(frases),ordem))
                        return jsonify(peso.score(frases))
                
                return ("Insira frase!")

        def post(self):
                json = request.get_json()
                frases = json['frases']
                if 'ordem' in json:
                        ordem = json['ordem']
                        return jsonify(peso.sort(peso.score(frases),ordem))
                return jsonify(peso.score(frases))

class Filter(Resource):

        def get(self):
                if len({'frases','operador','valor'}-set(request.args))==0:
                        frases = request.args.get('frases').split("$$")
                        operador = request.args.get('operador')
                        valor = request.args.get('valor', type=float)
                        if 'ordem' in request.args:
                                ordem = request.args.get('ordem')
                                return jsonify(peso.sort(peso.filtro(peso.score(frases),operador,valor),ordem))
                        return jsonify(peso.filtro(peso.score(frases),operador,valor))
                return ("Faltam parâmetros!")

        def post(self):
                json = request.get_json()
                frases = json['frases']
                operador = json['operador']
                valor = json['valor']
                if 'ordem' in json:
                        ordem = json['ordem']
                        return jsonify(peso.sort((peso.filtro(peso.score(frases),operador,valor)),ordem))
                return jsonify(peso.filtro(peso.score(frases),operador,valor))
