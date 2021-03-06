"""Handles the HTTP routing."""

from flask import Flask
# noinspection PyUnresolvedReferences
from flask_cors import CORS, cross_origin  # pylint: disable=unused-import

from cookomatic_api.db.cook_event import db_cook_event
from cookomatic_api.db.dish import db_dish
from cookomatic_api.db.meal import db_meal
from cookomatic_api.db.step import db_step

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

# Register API endpoints stored in other files
app.register_blueprint(db_cook_event)
app.register_blueprint(db_dish)
app.register_blueprint(db_meal)
app.register_blueprint(db_step)


@app.errorhandler(404)
def page_not_found(_):
    """Return a 404 error."""
    return '', 404
