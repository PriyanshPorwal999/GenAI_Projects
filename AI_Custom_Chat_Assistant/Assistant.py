# # 1. Import the necessary library
# import openai
# import os
# from dotenv import load_dotenv
# load_dotenv()

# # 2. Set up your API key
# # It's best practice to use an environment variable for your key.
# # Replace "YOUR_OPENAI_API_KEY" with your actual key if not using environment variables.
# # openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # Create the client instance
# client = openai.OpenAI()

# # 3. Initialize the conversation history
# # The 'system' message sets the AI's persona or instructions.
# messages = [
#     {"role": "system", "content": "You are a helpful assistant."}
# ]

# print("🤖 Chat Assistant is ready! Type 'quit' to exit.")

# # 4. Start the conversation loop
# while True:
#     # Get user input
#     user_input = input("You: ")
    
#     # Check for exit command
#     if user_input.lower() == 'quit':
#         print("🤖 Goodbye!")
#         break
    
#     # Add user's message to the history
#     messages.append({"role": "user", "content": user_input})
    
#     try:
#         # 5. Make the API call to OpenAI
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",  # You can use other models like "gpt-4"
#             messages=messages
#         )
        
#         # 6. Extract the assistant's reply
#         assistant_message = response.choices[0].message.content
#         print(f"Assistant: {assistant_message}")
        
#         # 7. Add the assistant's reply to the history
#         messages.append({"role": "assistant", "content": assistant_message})
        
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         # Remove the last user message if the API call fails
#         messages.pop()


import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# if not api_key or api_key:
#     print("❌ ERROR: Gemini API key is missing or not set properly in the .env file.")
#     exit(1)

# 2. Configure Gemini
genai.configure(api_key=api_key)

# 3. Create the model instance
# model = genai.GenerativeModel("gemini-1.5-flash")
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# 4. Start chat session
chat = model.start_chat(history=[])

print("🤖 Gemini Chat Assistant is ready! Type 'quit' to exit.")

# 5. Main chat loop
while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("👋 Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        print(f"Assistant: {response.text}")
    except Exception as e:
        print(f"⚠️ Error: {e}")
