"""Handles the HTTP routing."""

from flask import Flask
from flask_cors import CORS

from cookomatic_api.api.login import api_login
from cookomatic_api.api.scheduling import api_schedule
from cookomatic_api.db.dish import db_dish
from cookomatic_api.db.meal import db_meal
from cookomatic_api.db.step import db_step

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

# Register API endpoints stored in other files
app.register_blueprint(api_login)
app.register_blueprint(api_schedule)
app.register_blueprint(db_dish)
app.register_blueprint(db_meal)
app.register_blueprint(db_step)


@app.errorhandler(404)
def page_not_found(_):
    """Return a 404 error."""
    return '', 404
