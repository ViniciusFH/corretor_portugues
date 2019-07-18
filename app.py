from flask import Flask, request
from flask_restful import Resource, Api
import main

app = Flask(__name__)
api = Api(app)

api.add_resource(main.Score, '/score')
api.add_resource(main.Filter, '/score/filter')

if __name__ == '__main__':
    app.run()
