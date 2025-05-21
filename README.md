# 2BOrNot2BU

**2BOrNot2BU** is a creative web app that generates a personalized version of Hamlet’s “To Be or Not To Be” soliloquy using Google Gemini AI.  
You choose the genre, favorite music, film, setting, and character perspective—your soliloquy is instantly reimagined just for you.

- [screenshot of the app](Screenshot.png)
- [Live demo version](https://twobornot2bu.onrender.com)

---

## 🌟 Features

- **Personalized Soliloquy Generation**  
  Input your style, music, film, setting, and point of view character.
- **Powered by Google Gemini AI**  
  Your creativity meets the world’s most advanced language model.
- **Secure & Easy**  
  Your API key is never stored or shared.

---

## 🚀 Getting Started

1. **Clone the repo:**
    ```bash
    git clone https://github.com/<yourusername>/2BOrNot2BU.git
    cd 2BOrNot2BU
    ```

2. **Set up your environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Get a [Google Gemini API Key](https://aistudio.google.com/app/apikey) and save it in a `.env` file:**
    ```
    GEMINI_API_KEY=your_gemini_api_key
    ```

4. **Run the app:**
    ```bash
    python app.py
    ```
    Open your browser to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📝 Example Prompt

> *Genre:* cyberpunk noir  
> *Music:* Radiohead  
> *Film:* Blade Runner  
> *Place:* rain-soaked neon city  
> *POV:* Ophelia

**Result:**  
> *A soliloquy full of neon, longing, and existential shadow—Ophelia’s voice as you’ve never heard it before.*

---

## 🏛️ License

- MIT License.
- Attribution to Shakespeare and Google Gemini.

---

## 💡 Inspiration
This project was created by Japhy Grant as a showcase for AI-powered creative storytelling and adaptive narrative.

---

## 📦 Dependencies

- Python 3.8+
- Flask
- google-generativeai
- python-dotenv

Install them with:
```bash
pip install Flask google-generativeai python-dotenv

