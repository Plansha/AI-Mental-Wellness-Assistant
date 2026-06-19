import streamlit as st
from gemini_helper import get_wellness_advice

st.title("🧠 AI Wellness Coach")

st.write(
    "Ask the AI about stress, motivation, study pressure, wellness habits, or emotional wellbeing."
)

user_input = st.text_area(
    "How are you feeling today?"
)

if st.button("✨ Get AI Advice"):

    if user_input.strip():

        with st.spinner("Thinking..."):

            try:
                response = get_wellness_advice(
                    user_input
                )

                st.success("AI Response")

                st.write(response)

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )

    else:

        st.warning(
            "Please enter a message."
        )