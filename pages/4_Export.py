import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd

from database import SymptomDatabase
from analysis import MoodAnalyzer

st.set_page_config(
    page_title="Export Wellness Report",
    layout="wide"
)

st.header("📄 Wellness Report Export")

db = SymptomDatabase()

df = db.get_all_moods()

if not df.empty:

    # CSV Download

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="📥 Download Wellness Report (CSV)",
        data=csv,
        file_name=f"wellness_report_{pd.Timestamp.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

    st.markdown("---")

    # Summary Statistics

    st.subheader(
        "📊 Wellness Summary"
    )

    stats = MoodAnalyzer.analyze_overview(
        df
    )

    summary_df = pd.DataFrame(
        {
            "Metric": [
                "Total Entries",
                "Average Stress Level",
                "Most Common Mood",
                "Positive Entries",
                "Neutral Entries",
                "Negative Entries"
            ],
            "Value": [
                stats["total_entries"],
                stats["avg_stress_level"],
                stats["most_common_mood"],
                stats["positive_entries"],
                stats["neutral_entries"],
                stats["negative_entries"]
            ]
        }
    )

    st.dataframe(
        summary_df,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "📝 Recent Mood Entries"
    )

    recent_entries = df.head(5)

    st.dataframe(
        recent_entries,
        use_container_width=True
    )

    st.markdown("---")

    st.success(
        "Report ready for download."
    )

else:

    st.info(
        "No mood data available. Log some moods first."
    )