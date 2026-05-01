from flask import Blueprint, request, jsonify, render_template
from models.habit import Habit
from database.db import db
from datetime import datetime, timedelta
from services.ai_service import get_tip
from flask import redirect, url_for
from models.habit_log import HabitLog
from datetime import datetime

habit_bp = Blueprint("habit_bp", __name__)

@habit_bp.route("/habits", methods=["POST"])
def create_habit():
    data = request.get_json(silent=True) or request.form

    name = data.get("name")
    frequency = data.get("frequency")

    if not name or not frequency:
        return "Missing data", 400

    new_habit = Habit(
        name=name,
        frequency=frequency
    )

    db.session.add(new_habit)
    db.session.commit()

    return redirect(url_for("habit_bp.dashboard"))

@habit_bp.route("/habits/<int:habit_id>/complete", methods=["POST"])
def complete_habit(habit_id):
    habit = Habit.query.get_or_404(habit_id)

    now = datetime.utcnow()

    if habit.last_completed:
        diff = now - habit.last_completed

        if diff <= timedelta(days=1):
            habit.streak += 1
        else:
            habit.streak = 1
    else:
        habit.streak = 1

    habit.last_completed = now

    # ✅ ADD THIS PART HERE
    from models.habit_log import HabitLog

    today = now.date()

    log = HabitLog(
        habit_id=habit.id,
        date=today
    )

    db.session.add(log)

    # ✅ THEN commit everything together
    db.session.commit()

    return redirect(url_for("habit_bp.dashboard"))


@habit_bp.route("/habits", methods=["GET"])
def get_habits():
    habits = Habit.query.all()
    return jsonify([h.to_dict() for h in habits])

@habit_bp.route("/dashboard")
def dashboard():
    from datetime import date

    # Get all habits
    habits = Habit.query.all()

    # Calculate today's date
    today = date.today()

    # Count how many habits were completed today
    completed_today = sum(
        1 for h in habits
        if h.last_completed and h.last_completed.date() == today
    )

    # Optional: sort habits by streak (highest first)
    habits = sorted(habits, key=lambda h: h.streak, reverse=True)

    # Render dashboard
    return render_template(
        "dashboard.html",
        habits=habits,
        get_tip=get_tip,
        completed_today=completed_today
    )
    

@habit_bp.route("/habits/<int:habit_id>/delete", methods=["POST"])
def delete_habit(habit_id):
    habit = Habit.query.get_or_404(habit_id)

    from models.habit_log import HabitLog

    # ✅ delete all logs linked to this habit
    HabitLog.query.filter_by(habit_id=habit.id).delete()

    # then delete the habit itself
    db.session.delete(habit)

    db.session.commit()

    return redirect(url_for("habit_bp.dashboard"))