from database.db import db
from datetime import datetime

class HabitLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'))
    date = db.Column(db.Date, default=datetime.utcnow)

    habit = db.relationship('Habit', backref='logs')