from flask import Blueprint
from controllers import score

bluePrint = Blueprint('index', __name__)

@bluePrint.route('/score', methods=['GET','POST'])
def index():
	return score.sentences()
