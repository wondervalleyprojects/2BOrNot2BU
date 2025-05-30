from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import google.generativeai as genai
import os
os.makedirs('static/uploads', exist_ok=True)
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Set your Gemini API key as an environment variable for security
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_soliloquy(prompt):
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('models/gemini-2.5-flash-preview-04-17')
    response = model.generate_content(prompt)
    return response.text

# Video Upload Functionality
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'mp4', 'webm', 'mov'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
        Rewrite Hamlet's 'To Be or Not To Be' soliloquy as a {genre} piece.
        Channel the *lyrical style, wordplay, and emotional tone* of {music}. Use imagery, rhythm, or phrasing reminiscent of their songs.
        Also, *mimic the visual and narrative style, mood, and atmosphere* of {film}—use cinematic descriptions, references, or metaphors that would evoke this movie or show.
        Set the soliloquy in a place like {place}, and write it from the perspective of {pov}. 

        Do NOT write from the perspective of an AI or mention digital existence. Write it as the POV human character.

        Make both the music and film influences *strongly* felt—let their style and mood permeate every line. Use references, metaphors, or motifs drawn directly from them if you can.

        Retain the existential theme of grappling with life, death, and meaning, but make the soliloquy read as if it could be a {music} lyric and a scene in {film}, all while fitting the {genre} setting and {pov} perspective.

        Here is the original theme for reference:
        {soliloquy_theme}

        Do not summarize. Write the soliloquy in full and do not include any additional commentary or explanation.
        """
        soliloquy = get_soliloquy(prompt)
    return render_template('index.html', soliloquy=soliloquy)

@app.route('/upload', methods=['POST'])
def upload():
    if 'video_file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['video_file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        import uuid
        ext = file.filename.rsplit('.', 1)[1].lower()
        unique_id = uuid.uuid4().hex
        filename = secure_filename(f"{unique_id}.{ext}")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Save the soliloquy text and nickname
        with open('gallery.txt', 'a') as f:
            f.write(f"{filename}|{request.form['nickname']}|{request.form['soliloquy_text']}\n")
        return redirect(url_for('gallery'))
    flash('Invalid file format.')
    return redirect(url_for('home'))

@app.route('/gallery')
def gallery():
    performances = []
    if os.path.exists('gallery.txt'):
        with open('gallery.txt') as f:
            for line in f:
                # Skip empty lines or malformed lines
                if '|' not in line:
                    continue
                parts = line.strip().split('|', 2)
                if len(parts) == 3:
                    filename, nickname, soliloquy = parts
                    performances.append({'video': filename, 'name': nickname, 'text': soliloquy})
    return render_template('gallery.html', performances=performances)

if __name__ == '__main__':
    app.run(debug=True)
