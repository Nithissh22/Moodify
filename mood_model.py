from textblob import TextBlob
import random

def detect_mood(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.3:
        return "Happy"
    elif polarity < -0.3:
        return "Sad"
    else:
        return "Neutral"

def get_recommendation(mood):
    playlist = {
        "Happy": ["Happy - Pharrell", "On Top of the World - Imagine Dragons"],
        "Sad": ["Someone Like You - Adele", "Fix You - Coldplay"],
        "Neutral": ["Let It Be - Beatles", "Wake Me Up - Avicii"]
    }
    return random.choice(playlist[mood])
