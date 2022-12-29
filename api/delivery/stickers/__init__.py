from flask import Blueprint

from api.delivery.stickers import sticker

blueprint = Blueprint('stickers', __name__, url_prefix='/api/stickers')

blueprint.add_url_rule('/v1/get_trending_stickers',
                       view_func=sticker.get_trending_stickers, methods=["GET"])
