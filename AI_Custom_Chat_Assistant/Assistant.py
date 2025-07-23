# 1. Import the necessary library
import openai
import os

# 2. Set up your API key
# It's best practice to use an environment variable for your key.
# Replace "YOUR_OPENAI_API_KEY" with your actual key if not using environment variables.
openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")

# Create the client instance
client = openai.OpenAI()

# 3. Initialize the conversation history
# The 'system' message sets the AI's persona or instructions.
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("🤖 Chat Assistant is ready! Type 'quit' to exit.")

# 4. Start the conversation loop
while True:
    # Get user input
    user_input = input("You: ")
    
    # Check for exit command
    if user_input.lower() == 'quit':
        print("🤖 Goodbye!")
        break
    
    # Add user's message to the history
    messages.append({"role": "user", "content": user_input})
    
    try:
        # 5. Make the API call to OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can use other models like "gpt-4"
            messages=messages
        )
        
        # 6. Extract the assistant's reply
        assistant_message = response.choices[0].message.content
        print(f"Assistant: {assistant_message}")
        
        # 7. Add the assistant's reply to the history
        messages.append({"role": "assistant", "content": assistant_message})
        
    except Exception as e:
        print(f"An error occurred: {e}")
        # Remove the last user message if the API call fails
        messages.pop()