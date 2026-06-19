import streamlit as st
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SymptomDatabase
from sentiment import analyze_sentiment

st.set_page_config(
    page_title="Log Mood",
    layout="wide"
)

st.header("🧠 AI Mental Wellness Assistant")

db = SymptomDatabase()


# -------------------------
# WELLNESS TIPS
# -------------------------

def get_wellness_tip(sentiment):

    if sentiment == "Negative":
        return (
            "Try deep breathing, take a short walk, "
            "or talk with someone you trust."
        )

    elif sentiment == "Positive":
        return (
            "Keep up the positive habits that are helping you feel good."
        )

    return (
        "Take a few minutes to reflect on your day and stay hydrated."
    )


# -------------------------
# UI
# -------------------------

col1, col2 = st.columns(2)

with col1:

    mood = st.selectbox(
        "😊 Current Mood",
        [
            "Happy",
            "Calm",
            "Neutral",
            "Motivated",
            "Stressed",
            "Sad",
            "Anxious"
        ]
    )

    stress_level = st.slider(
        "📊 Stress Level",
        1,
        10,
        5
    )

with col2:

    date_input = st.date_input(
        "📅 Date"
    )

    time_input = st.time_input(
        "⏰ Time"
    )

    timestamp = datetime.combine(
        date_input,
        time_input
    )

trigger = st.selectbox(
    "⚡ Main Trigger",
    [
        "Studies",
        "Exams",
        "Assignments",
        "Family",
        "Friends",
        "Health",
        "Finances",
        "Work",
        "Other"
    ]
)

journal_entry = st.text_area(
    "📝 Describe how you are feeling today",
    height=150,
    placeholder="Example: I feel stressed because of upcoming exams..."
)

if st.button(
    "💾 SAVE MOOD",
    type="primary"
):

    sentiment = analyze_sentiment(
        journal_entry
    )

    success = db.add_mood(
        mood=mood,
        stress_level=stress_level,
        trigger=trigger,
        journal_entry=journal_entry,
        sentiment=sentiment,
        timestamp=timestamp.strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )

    if success:

        st.success(
            "✅ Mood saved successfully!"
        )

        st.info(
            f"🧠 AI Sentiment Analysis Result: {sentiment}"
        )

        st.subheader(
            "🌿 Personalized Wellness Suggestion"
        )

        st.write(
            get_wellness_tip(
                sentiment
            )
        )

    else:

        st.error(
            "❌ Failed to save mood."
        )