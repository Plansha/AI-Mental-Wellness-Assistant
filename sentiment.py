from textblob import TextBlob


def analyze_sentiment(text):

    if not text.strip():
        return "Neutral"

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.1:
        return "Positive"

    elif polarity < -0.1:
        return "Negative"

    return "Neutral"
