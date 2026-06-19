import streamlit as st
from database import SymptomDatabase
from analysis import MoodAnalyzer

st.set_page_config(
    page_title="AI Mental Wellness Assistant",
    layout="wide"
)

st.title("🧠 AI Mental Wellness Assistant")

st.markdown("""
### Welcome!

This AI-powered application helps users:

- 😊 Track daily moods
- 📊 Monitor stress levels
- 🧠 Analyze emotional trends
- 🌿 Receive wellness suggestions
- 📄 Export mood reports

Use the sidebar to navigate through the application.
""")

db = SymptomDatabase()

# Load mood data
df = db.get_all_moods()

if not df.empty:

    stats = MoodAnalyzer.analyze_overview(df)

    st.subheader("📈 Wellness Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Entries",
            stats["total_entries"]
        )

    with col2:
        st.metric(
            "Average Stress",
            stats["avg_stress_level"]
        )

    with col3:
        st.metric(
            "Most Common Mood",
            stats["most_common_mood"]
        )

    st.subheader("😊 Sentiment Summary")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            "Positive",
            stats["positive_entries"]
        )

    with col5:
        st.metric(
            "Neutral",
            stats["neutral_entries"]
        )

    with col6:
        st.metric(
            "Negative",
            stats["negative_entries"]
        )

else:

    st.info(
        "No mood entries found. Start by logging your mood from the sidebar."
    )

st.markdown("---")

st.success(
    "👈 Use the sidebar to log moods, view mood history, analyze trends, and export reports."
)