from extension import db
from sqlalchemy.sql import func


class Sticker(db.Model):
    __tablename__ = "trending_stickers"
    __table_args__ = {'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_unicode_ci'}
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    time_of_day = db.Column(db.DateTime, server_default=func.now(), nullable=False)
