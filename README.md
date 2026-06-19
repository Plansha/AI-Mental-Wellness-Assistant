# 🧠 AI Mental Wellness Assistant

An AI-powered Streamlit web application that helps users track moods, monitor stress levels, analyze emotional trends, and generate wellness reports.

---

## 🚀 Quick Start

### Install Dependencies

```bash
pip install streamlit pandas plotly
```

### Run the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

The application automatically creates a local SQLite database to store mood records.

---

## ✨ Features

### 😊 Mood Tracking

* Log daily moods
* Record stress levels (1–10)
* Add mood triggers
* Maintain a personal wellness journal

### 🧠 Sentiment Analysis

* Automatically classifies journal entries as:

  * Positive
  * Neutral
  * Negative

### 📊 Analytics Dashboard

* Mood distribution charts
* Sentiment analysis visualization
* Stress level trends over time
* Trigger insights

### 📄 Wellness Reports

* Export mood history as CSV
* Generate personal wellness summaries
* View recent mood entries

### 🌿 Wellness Suggestions

* Provides personalized wellness recommendations based on detected sentiment.

---

## 📂 Project Structure

```text
AI-Mental-Wellness-Assistant/
│
├── app.py
├── database.py
├── models.py
├── services.py
├── analysis.py
├── utils.py
├── requirements.txt
│
├── pages/
│   ├── 1_Log_Mood.py
│   ├── 2_View_Data.py
│   ├── 3_Analysis.py
│   └── 4_Export.py
│
└── moods.db
```

---

## 🛠️ Tech Stack

* Streamlit
* Python
* Pandas
* Plotly
* SQLite

---

## 📈 Application Modules

### Home Dashboard

Overview of wellness statistics and sentiment summaries.

### Mood Logger

Capture mood, stress level, triggers, and journal reflections.

### Mood History

View and manage all recorded entries.

### Analytics Dashboard

Visualize emotional patterns and stress trends.

### Report Export

Download mood history and wellness summaries.

---

## 🎯 Future Enhancements

* AI Chatbot Integration
* Gemini/OpenAI-powered Wellness Coach
* Advanced NLP Sentiment Analysis
* Personalized Mental Wellness Recommendations
* PDF Report Generation

---

## 📄 License

This project is developed for educational and internship purposes.
