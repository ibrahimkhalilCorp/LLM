from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
result = model.generate_content( "What is 81 divided by 9?")
print(result.text)