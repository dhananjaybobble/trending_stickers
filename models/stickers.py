from datetime import datetime
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

    stickers = Sticker.query.filter(Sticker.time_of_day == time_of_day).all()
    sorted_by_priority = sorted(stickers, key=lambda x : x.priority)
    return sorted_by_priority
