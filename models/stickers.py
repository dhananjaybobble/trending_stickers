from datetime import datetime

from sqlalchemy import desc

from models.models import Sticker
from flask import jsonify


def get_trending_sticker():

    now = datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        time_of_day = 'morning'
    elif 12 <= hour < 17:
        time_of_day = 'afternoon'
    elif 17 <= hour < 21:
        time_of_day = 'evening'
    else:
        time_of_day = 'night'

    stickers = Sticker.query.filter(Sticker.time_of_day == time_of_day).order_by(Sticker.priority).all()
    # sorted_by_priority = sorted(stickers, key=lambda x: x.priority)
    #print(stickers)
    return stickers
