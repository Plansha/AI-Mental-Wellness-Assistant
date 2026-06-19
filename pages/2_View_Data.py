import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from database import SymptomDatabase

st.set_page_config(
    page_title="Mood History",
    layout="wide"
)

st.header("📊 Mood History")

db = SymptomDatabase()

df = db.get_all_moods()

if not df.empty:

    st.success(
        f"Found {len(df)} mood entries"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader("🗑️ Delete Mood Entry")

    entry_id = st.number_input(
        "Entry ID",
        min_value=1,
        value=1
    )

    if st.button("Delete Entry"):

        if db.delete_mood(entry_id):

            st.success(
                "Entry deleted successfully!"
            )

            st.rerun()

        else:

            st.error(
                "Entry not found."
            )

else:

    st.info(
        "No mood entries found yet."
    )
