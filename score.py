from flask import jsonify, request
from flask_restful import Resource
import peso

class Score(Resource):


        def post(self):
                
                json = request.get_json()
                frases = json['frases']
                ordem = 'desc'
                operador = '='
                
                if 'ordem' in json and json['ordem']:
                        ordem = json['ordem']
                if 'valor' not in json or not json['valor']:
                        return jsonify(peso.sort(peso.score(frases),ordem))
                
                valor = json['valor']
                
                if 'operador' in json and json['operador']:
                        operador = json['operador']
                        
                return jsonify(peso.sort((peso.filtro(peso.score(frases),operador,valor)),ordem))


        def get(self):

                ordem = 'desc'
                operador = '='
                
                if 'frases' in request.args:
                        frases = request.args.get('frases').split('$$')
                        if 'ordem' in request.args:
                                ordem = request.args.get('ordem')
                        if 'valor' not in request.args:
                                return jsonify(peso.sort(peso.score(frases),ordem))
                        valor = float(request.args.get('valor'))
                        if 'operador' in request.args:
                                operador = request.args.get('operador')
                        
                        return jsonify(peso.sort((peso.filtro(peso.score(frases),operador,valor)),ordem))
                
                return ("Insira frase!")


        
                
                
