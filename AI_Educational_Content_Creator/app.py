import os
import json
from flask import Flask, render_template, request, jsonify
import openai

# 1. Initialize the Flask App and OpenAI Client
app = Flask(__name__)
# It's best practice to use an environment variable for your API key.
# Replace "YOUR_OPENAI_API_KEY" with your key if not using one.
openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")
client = openai.OpenAI()

# 2. Define the System Prompt for the AI
# This is the core instruction that guides the AI's output.
# It explicitly asks for a JSON object and details the structure, including the Bloom's Taxonomy requirement.
SYSTEM_PROMPT = """
You are EduGenie, an expert AI instructional designer. Your task is to generate a comprehensive educational content plan for a given course title.
Your entire response MUST be a single, valid JSON object and nothing else.

The JSON object must have these exact keys: "objective", "syllabus", "learningOutcomes", "assessmentMethods", "recommendedReadings".

- "objective": A single, concise paragraph describing the course's primary goal.
- "syllabus": An array of 5 strings, representing key topics or modules for a sample syllabus.
- "learningOutcomes": An array of 3 strings. Each string must be a measurable learning outcome. You MUST align these outcomes with different levels of Bloom's Taxonomy and state the level in parentheses at the end of the sentence, like "(Apply)".
- "assessmentMethods": An array of 3-4 strings describing varied assessment methods (e.g., formative, summative).
- "recommendedReadings": An array of 3-4 strings, each listing a relevant book or academic article in a "Title by Author" format.
"""

# 3. Define the main route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# 4. Define the API endpoint for generating content
@app.route('/generate-content', methods=['POST'])
def generate_content():
    try:
        data = request.get_json()
        course_title = data.get('title')

        if not course_title:
            return jsonify({'error': 'Course title is missing.'}), 400

        # 5. Make the API call to OpenAI
        # We use gpt-4o and the new JSON mode for reliable JSON output.
        response = client.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Generate the educational plan for the course titled: '{course_title}'"}
            ]
        )
        
        # 6. Parse the JSON response and send it to the frontend
        # The content from the API is a string that needs to be loaded into a Python dictionary
        ai_response_content = json.loads(response.choices[0].message.content)
        return jsonify(ai_response_content)

    except openai.APIError as e:
        # Handle specific API errors (e.g., rate limits, server issues)
        return jsonify({'error': f'OpenAI API Error: {str(e)}'}), 500
    except Exception as e:
        # Handle other potential errors (e.g., network issues)
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

# 7. Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)