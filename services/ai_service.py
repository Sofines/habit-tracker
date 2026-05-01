import random

tips = [
    "Small steps compound into systems.",
    "Consistency beats motivation.",
    "Your future self is watching 👀",
    "One habit at a time.",
    "Discipline > intensity"
]

def get_tip(habit):
    if habit.streak >= 7:
        return "You're on fire 🔥 This is your identity now."
    elif habit.streak >= 3:
        return "Momentum is building. Keep going."
    elif habit.streak >= 1:
        return "Consistency beats motivation."
    else:
        return "Start small. Just show up."