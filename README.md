# 🧠 AI Mental Wellness Assistant

An AI-powered Mental Wellness Assistant built using Streamlit, SQLite, TextBlob, Plotly, and Google Gemini AI.

The application helps users track moods, monitor stress levels, analyze emotional trends, receive AI-generated wellness guidance, and export wellness reports.

---

## 🚀 Features

### 😊 Mood Tracking
- Log daily moods
- Record stress levels (1–10)
- Track emotional triggers
- Maintain a personal wellness journal

### 🧠 NLP Sentiment Analysis
- Uses TextBlob for sentiment analysis
- Automatically classifies entries as:
  - Positive
  - Neutral
  - Negative

### 📊 Wellness Analytics Dashboard
- Mood distribution charts
- Stress level trends over time
- Sentiment analysis visualization
- Trigger insights and statistics

### 🤖 Gemini AI Wellness Coach
- Powered by Google Gemini
- Provides personalized wellness suggestions
- Helps users manage stress, motivation, and emotional wellbeing
- Interactive AI chat experience

### 📄 Wellness Report Export
- Download mood history as CSV
- Generate personal wellness summaries
- View recent mood entries

### 💾 Secure Data Storage
- SQLite database integration
- Local data storage
- Fast and lightweight

---

# 🖥️ Application Pages

### 🏠 Home Dashboard
Displays overall wellness statistics and sentiment summaries.

### 😊 Log Mood
Record:
- Current mood
- Stress level
- Trigger
- Journal entry

### 📊 View Data
Browse and manage all stored mood entries.

### 📈 Analysis
Visualize:
- Mood distribution
- Stress trends
- Sentiment statistics
- Trigger insights

### 📄 Export
Download wellness reports and summaries.

### 🤖 AI Wellness Coach
Ask questions such as:

> "I'm stressed about exams."

> "How can I improve my focus?"

> "I feel anxious and overwhelmed."

and receive AI-generated guidance powered by Google Gemini.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| Streamlit | Web Application Framework |
| SQLite | Database Storage |
| Pandas | Data Processing |
| Plotly | Data Visualization |
| TextBlob | NLP Sentiment Analysis |
| Google Gemini AI | AI Wellness Coach |
| Python Dotenv | API Key Management |

---

# 📂 Project Structure

```text
AI-Mental-Wellness-Assistant/
│
├── app.py
├── database.py
├── analysis.py
├── models.py
├── services.py
├── sentiment.py
├── gemini_helper.py
├── requirements.txt
├── .gitignore
│
├── pages/
│   ├── 1_Log_Mood.py
│   ├── 2_View_Data.py
│   ├── 3_Analysis.py
│   ├── 4_Export.py
│   └── 5_AI_Coach.py
│
└── moods.db
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Plansha/AI-Mental-Wellness-Assistant.git
cd AI-Mental-Wellness-Assistant
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Install TextBlob Corpora

```bash
python -m textblob.download_corpora
```

## Configure Gemini API

Create a file named:

```text
.env
```

Add:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Get a free Gemini API key from:

https://aistudio.google.com/apikey

---

# ▶️ Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 📱 Demo Screenshots

## Home Dashboard

<img width="769" height="418" alt="image" src="https://github.com/user-attachments/assets/560202bc-a2b3-4498-9c15-4e8ee0b76725" />


## Mood Logger

<img width="773" height="419" alt="image" src="https://github.com/user-attachments/assets/0a1a93f4-2e5a-4f19-a259-25f8cd0cb8d0" />


## Analytics Dashboard

<img width="771" height="417" alt="image" src="https://github.com/user-attachments/assets/33fd1b87-7aff-4666-8fb6-85a29c1d7cbd" />


## Export Report

<img width="772" height="416" alt="image" src="https://github.com/user-attachments/assets/b88bb1c4-bc51-4969-b27b-c364d4dddb00" />


## AI Wellness Coach

<img width="773" height="419" alt="image" src="https://github.com/user-attachments/assets/b0839917-93ce-425f-9bc7-02cc35e8855a" />


---

# 🎯 Future Enhancements

- Mood prediction using Machine Learning
- Personalized wellness recommendations
- PDF report generation
- Email wellness reports
- Multi-user authentication
- Chat history support
- Voice-based wellness assistant

---

# 🔒 Security

- API keys are stored in `.env`
- `.env` is excluded using `.gitignore`
- Local SQLite database storage

---

# 📄 License

This project is developed for educational, research, and internship purposes.

---

# 👨‍💻 Author

**Plansha**

GitHub:
https://github.com/Plansha

Project Repository:
https://github.com/Plansha/AI-Mental-Wellness-Assistant

