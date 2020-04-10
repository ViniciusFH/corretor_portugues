from flask import request
from analyzer import score

def sentences():

	if request.method == 'GET':

		if 'sentences' not in request.args:
			return ('Try: url/score?sentences=one sentence$$another sentence$$etc')
			
		sentences = request.args.get('sentences').split('$$')

		if 'order' in request.args:
			order = request.args.get('order')

		if 'value' in request.args:
		    value = float(request.args.get('value'))

		if 'operator' in request.args:
			operator = request.args.get('operator')
			


	if request.method == 'POST':

		json = request.get_json()

		if 'sentences' not in json or not json['sentences']:
			return {'success': False, 'errorMessage': 'I need a JSON with a non empty array of sentences.'}

		sentences = json['sentences']

		if 'order' in json and json['order']:
		    order = json['order']

		if 'value' in json and json['value']:
			value = json['value']

		if 'operator' in json and json['operator']:
		    operator = json['operator']



	scores = score(sentences, order='desc', operator='=', value=None)

	return {'success': True, 'scores': scores}