from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

# Set your Gemini API key as an environment variable for security
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_soliloquy(prompt):
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('models/gemini-2.5-flash-preview-04-17')
    response = model.generate_content(prompt)
    return response.text

@app.route('/', methods=['GET', 'POST'])
def home():
    soliloquy = None
    if request.method == 'POST':
        genre = request.form.get('genre')
        music = request.form.get('music')
        film = request.form.get('film')
        place = request.form.get('place')
        pov = request.form.get('pov')
        soliloquy_theme = "To be, or not to be, that is the question... (existential crisis, mortality, and the human condition)"
        prompt = f"""
        Rewrite Hamlet's 'To Be or Not To Be' soliloquy as a {genre} piece, heavily inspired by the music of {music} and the world/style of {film}. 
        Set it in a place like {place}, and write it from the perspective of {pov}. Do not write it from the perspective of an AI, but rather as a human character.
        Maintain the existential theme of grappling with life, death, and meaning, but express it in the voice and mood fitting the inputted settings.

        Here is the original theme for reference:
        {soliloquy_theme}

        Do not summarize. Write the soliloquy in full.
        """
        soliloquy = get_soliloquy(prompt)
    return render_template('index.html', soliloquy=soliloquy)

if __name__ == '__main__':
    app.run(debug=True)

