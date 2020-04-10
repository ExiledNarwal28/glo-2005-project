from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_cors import CORS

from app.forms import GeneralSearchForm
from app.practice_centers.views import practice_centers_blueprint
from app.shops.views import shops_blueprint
from app.sports.views import sports_blueprint
from app.users.views import users_blueprint
from app.views import root_blueprint

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

bcrypt = Bcrypt(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
Bootstrap(app)

app.register_blueprint(root_blueprint)
app.register_blueprint(sports_blueprint)
app.register_blueprint(practice_centers_blueprint)
app.register_blueprint(shops_blueprint)
app.register_blueprint(users_blueprint)


@app.errorhandler(400)
def page_bad_request():
    return render_template('400.html'), 400


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404
