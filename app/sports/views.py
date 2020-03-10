from flask import render_template, Blueprint

from app.sports.exceptions import SportNotFoundException
from app.queries import SportQuery

sports_blueprint = Blueprint('sports', __name__)


# TODO : Make sports query params for search
#        Use Sport.query.filter(Sport.x == x, ...).order_by...
@sports_blueprint.route('/sports/')
def sports():
    all_sports = SportQuery().get_all()
    return render_template('sports.html', sports=all_sports)


@sports_blueprint.route('/sports/<sport_id>')
def sport_details(sport_id):
    # TODO : 404 if not found
    try:
        sport = SportQuery().get(sport_id)
    except SportNotFoundException:
        return render_template('404.html'), 404

    return render_template('sport_details.html', sport=sport)
