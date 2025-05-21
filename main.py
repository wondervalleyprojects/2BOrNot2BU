import getpass
import google.generativeai as genai

def get_soliloquy(prompt, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-2.5-flash-preview-04-17')
    response = model.generate_content(prompt)
    return response.text

print("\nWelcome to 2BOrNot2BU: Your Personalized Soliloquy!\n")

user_profile = {}
user_profile['genre'] = input("Pick a genre/style (e.g., cyberpunk noir, fantasy, rom-com): ")
user_profile['music'] = input("Favorite musical artist or band: ")
user_profile['film'] = input("A movie or TV show you love: ")
user_profile['place'] = input("A setting or place that feels special to you: ")
user_profile['pov'] = input("Whose perspective would you like the soliloquy from? (Hamlet, Ophelia, Claudius, etc.): ")

soliloquy_theme = "To be, or not to be, that is the question... (existential crisis, mortality, and the human condition)"

prompt = f"""
Rewrite Hamlet's 'To Be or Not To Be' soliloquy as a {user_profile['genre']} piece, inspired by the music of {user_profile['music']} and the world/style of {user_profile['film']}. 
Set it in a place like {user_profile['place']}, and write it from the perspective of {user_profile['pov']}. 
Maintain the existential theme of grappling with life, death, and meaning, but express it in the voice and mood fitting your settings.

Here is the original theme for reference:
{soliloquy_theme}

Do not summarize. Write the soliloquy in full.
"""

api_key = getpass.getpass("\nEnter your Gemini API key: ")

print("\n----- GENERATING YOUR PERSONALIZED SOLILOQUY WITH GEMINI -----\n")
soliloquy = get_soliloquy(prompt, api_key)
print(soliloquy)
