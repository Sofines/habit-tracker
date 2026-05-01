from database.db import db
from datetime import datetime

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    frequency = db.Column(db.String(50), nullable=False)

    # 🔥 NEW FIELDS
    last_completed = db.Column(db.DateTime, nullable=True)
    streak = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "frequency": self.frequency,
            "streak": self.streak,
            "last_completed": self.last_completed
        }