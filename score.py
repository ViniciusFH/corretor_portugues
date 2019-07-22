from flask import jsonify, request
from flask_restful import Resource
import peso

class Score(Resource):


        def post(self):
                
                json = request.get_json()
                frases = json['frases']
                if 'ordem' in json:
                        ordem = json['ordem']
                else:
                        ordem = 'desc'
                if 'valor' not in json:
                        return jsonify(peso.sort(peso.score(frases),ordem))
                valor = json['valor']
                if 'operador' in json:
                        operador = json['operador']
                else:
                        operador = '='
                        
                return jsonify(peso.sort((peso.filtro(peso.score(frases),operador,valor)),ordem))


        def get(self):
                
                if 'frases' in request.args:
                        frases = request.args.get('frases').split('$$')
                        if 'ordem' in request.args:
                                ordem = request.args.get('ordem')
                        else:
                                ordem = 'desc'
                        if 'valor' not in request.args:
                                return jsonify(peso.sort(peso.score(frases),ordem))
                        valor = float(request.args.get('valor'))
                        if 'operador' in request.args:
                                operador = request.args.get('operador')
                        else:
                                operador = '='
                        
                        return jsonify(peso.sort((peso.filtro(peso.score(frases),operador,valor)),ordem))
                
                return ("Insira frase!")


        
                
                
