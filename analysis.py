import pandas as pd
from collections import Counter
from typing import Dict


class MoodAnalyzer:

    @staticmethod
    def analyze_overview(df: pd.DataFrame) -> Dict:

        if df.empty:
            return {}

        return {
            "total_entries": len(df),
            "avg_stress_level": round(
                df["stress_level"].mean(),
                1
            ),
            "most_common_mood": (
                df["mood"].mode()[0]
                if not df["mood"].mode().empty
                else ""
            ),
            "positive_entries": (
                df["sentiment"] == "Positive"
            ).sum(),
            "negative_entries": (
                df["sentiment"] == "Negative"
            ).sum(),
            "neutral_entries": (
                df["sentiment"] == "Neutral"
            ).sum()
        }

    @staticmethod
    def get_mood_stats(df: pd.DataFrame):

        if df.empty:
            return pd.DataFrame()

        return (
            df.groupby("mood")["stress_level"]
            .agg(["mean", "count"])
            .round(1)
        )

    @staticmethod
    def get_trigger_insights(df: pd.DataFrame):

        if df.empty:
            return {}

        return dict(
            Counter(
                df["trigger"]
            ).most_common(10)
        )

    @staticmethod
    def get_sentiment_distribution(df: pd.DataFrame):

        if df.empty:
            return {}

        return (
            df["sentiment"]
            .value_counts()
            .to_dict()
        )