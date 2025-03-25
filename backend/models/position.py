from backend.core.extensions import db


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    score_threshold = db.Column(db.Integer, nullable=False)
