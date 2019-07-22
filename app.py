from flask import Flask, request
from flask_restful import Resource, Api
import score

app = Flask(__name__)
api = Api(app)

api.add_resource(score.Score, '/score')

if __name__ == '__main__':
    app.run(debug=True)
