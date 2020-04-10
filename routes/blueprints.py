from routes import score

def register(app):
	app.register_blueprint(score.bluePrint)