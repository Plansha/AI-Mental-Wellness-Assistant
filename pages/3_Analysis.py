import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import plotly.express as px
import pandas as pd

from database import SymptomDatabase
from analysis import MoodAnalyzer

st.set_page_config(
    page_title="Mood Analysis",
    layout="wide"
)

st.header("📈 Mood Analytics Dashboard")

db = SymptomDatabase()

df = db.get_all_moods()

if not df.empty:

    stats = MoodAnalyzer.analyze_overview(df)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Entries",
        stats["total_entries"]
    )

    col2.metric(
        "Average Stress",
        stats["avg_stress_level"]
    )

    col3.metric(
        "Most Common Mood",
        stats["most_common_mood"]
    )

    st.markdown("---")

    # Mood Distribution

    col1, col2 = st.columns(2)

    with col1:

        mood_counts = (
            df["mood"]
            .value_counts()
            .reset_index()
        )

        mood_counts.columns = [
            "Mood",
            "Count"
        ]

        fig1 = px.bar(
            mood_counts,
            x="Mood",
            y="Count",
            title="Mood Distribution"
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    with col2:

        sentiment_counts = (
            df["sentiment"]
            .value_counts()
            .reset_index()
        )

        sentiment_counts.columns = [
            "Sentiment",
            "Count"
        ]

        fig2 = px.pie(
            sentiment_counts,
            names="Sentiment",
            values="Count",
            title="Sentiment Distribution"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.markdown("---")

    # Stress Trend

    df["timestamp"] = pd.to_datetime(
        df["timestamp"]
    )

    fig3 = px.line(
        df.sort_values("timestamp"),
        x="timestamp",
        y="stress_level",
        markers=True,
        title="Stress Level Over Time"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "📊 Mood Statistics"
        )

        mood_stats = (
            df.groupby("mood")["stress_level"]
            .agg(["mean", "count"])
            .round(1)
        )

        st.dataframe(
            mood_stats,
            use_container_width=True
        )

    with col2:

        st.subheader(
            "🔥 Top Stress Triggers"
        )

        trigger_counts = (
            df["trigger"]
            .value_counts()
            .reset_index()
        )

        trigger_counts.columns = [
            "Trigger",
            "Count"
        ]

        st.dataframe(
            trigger_counts,
            use_container_width=True
        )

else:

    st.warning(
        "📝 Log some moods first to generate analytics."
    )