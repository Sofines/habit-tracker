from flask import Flask, jsonify
from database.db import db
from routes.habit_routes import habit_bp
from models.habit_log import HabitLog
from datetime import datetime, timedelta

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cyber_habit.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Register routes
app.register_blueprint(habit_bp)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return jsonify({
        "message": "Cyber Habit Tracker API is running 🧠⚡"
    })


if __name__ == "__main__":
    app.run(debug=True)