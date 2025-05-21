import getpass
import google.generativeai as genai

api_key = getpass.getpass("\nEnter your Gemini API key: ")
genai.configure(api_key=api_key)

print("Available models:")
for m in genai.list_models():
    print(m.name, m.supported_generation_methods)
