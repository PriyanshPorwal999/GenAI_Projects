# 1. Import necessary libraries
import os
from flask import Flask, render_template, request, jsonify
import openai

# 2. Initialize the Flask app
app = Flask(__name__)

# 3. Set up your OpenAI API key
# It's best practice to use an environment variable.
# Replace "YOUR_OPENAI_API_KEY" with your actual key if not using an environment variable.
openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")

# Create the client instance
client = openai.OpenAI()

# 4. Define the main route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# 5. Define the route for image generation
@app.route('/generate-image', methods=['POST'])
def generate_image():
    # Get the JSON data sent from the JavaScript front-end
    data = request.get_json()
    prompt_text = data.get('prompt')

    if not prompt_text:
        return jsonify({'error': 'Prompt is missing.'}), 400

    try:
        # 6. Make the API call to DALL-E
        response = client.images.generate(
            model="dall-e-3",            # Or "dall-e-2"
            prompt=prompt_text,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        # 7. Extract the image URL and send it back as JSON
        image_url = response.data[0].url
        return jsonify({'image_url': image_url})

    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return jsonify({'error': str(e)}), 500

# 8. Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)