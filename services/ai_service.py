import random
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_advice(habit):
    prompt = f"""
    Habit: {habit.name}
    Streak: {habit.streak}

    Give:
    - one short suggestion
    - one fun fact

    Style:
    - very short
    - cyber/terminal tone
    - no long explanations
    - use normal sentence capitalization (no ALL CAPS words)
    - do not use markdown like ** or __
    - keep it clean and readable
    - max 2 short lines
    """

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant"
        )

        return response.choices[0].message.content

    except Exception as e:
        print("AI error:", e)
        return "> system_fallback: stay consistent and keep going"

tips = [
    "Small steps compound into systems.",
    "Consistency beats motivation.",
    "Your future self is watching ",
    "One habit at a time.",
    "Discipline > intensity"
]

def get_tip(habit):
    if habit.streak >= 7:
        return "You're on fire! This is your identity now."
    elif habit.streak >= 3:
        return "Momentum is building. Keep going."
    elif habit.streak >= 1:
        return "Consistency beats motivation."
    else:
        return "Start small. Just show up."