from flask import Flask, request, jsonify, render_template
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Create model instance
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
chat = model.start_chat(history=[])

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # You must have templates/index.html

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message']
    try:
        response = chat.send_message(user_input)
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'reply': f"Error: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
