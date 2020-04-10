from flask import Flask
from routes import blueprints

app = Flask(__name__)
app.app_context().push()

blueprints.register(app)


if __name__ == '__main__':
    app.run(debug=True)
