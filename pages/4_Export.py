import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
import pandas as pd
from database import SymptomDatabase
from analysis import SymptomAnalyzer

st.set_page_config(page_title="Export", layout="wide")
st.header("📤 Export & Reports")

db = SymptomDatabase()
df = db.get_all_symptoms()

if not df.empty:
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Full Report (CSV)",
        data=csv,
        file_name=f'symptom_report_{pd.Timestamp.now().strftime("%Y%m%d")}.csv',
        mime='text/csv'
    )
    
    st.subheader("📋 Quick Summary")
    stats = SymptomAnalyzer.analyze_overview(df)
    
    summary_df = pd.DataFrame([stats]).T
    summary_df.columns = ['Value']
    st.dataframe(summary_df)
    
    st.subheader("📋 Last 5 Entries")
    recent = df.head()
    st.dataframe(recent)
    
else:
    st.info("📝 No data to export. Log symptoms first!")
