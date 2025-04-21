from flask import Flask, render_template, request
from mood_model import detect_mood, get_recommendation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    mood = None
    recommendation = None
    if request.method == 'POST':
        user_input = request.form['mood_input']
        mood = detect_mood(user_input)
        recommendation = get_recommendation(mood)
    return render_template('index.html', mood=mood, recommendation=recommendation)
