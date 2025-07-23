This Repo Consist of Gen-AI Projects.

Python & OpenAI API: A Collection of Generative AI Projects
This repository contains a series of projects demonstrating the practical application of Python and the OpenAI API to build intelligent applications. From a simple command-line chatbot to a full-stack web application for generating educational content, these projects showcase a progression in complexity and functionality.

## About the Projects
This collection is designed to provide hands-on experience with OpenAI's powerful models (like GPT-3.5, GPT-4o, and DALL-E 3) through Python. Each project builds upon fundamental concepts, culminating in a full-featured capstone project.

## Technology Stack
Backend: Python, Flask

Frontend: HTML, CSS, JavaScript (for web projects)

AI/ML: OpenAI API (Chat Completions, Image Generation)

Core Libraries: openai, flask

## Getting Started
Follow these instructions to get the projects up and running on your local machine.

## Prerequisites
Python 3.8 or newer

A code editor (e.g., VS Code)

An active OpenAI API key

## Installation
Clone the repository:

git clone https://github.com/PriyanshPorwal999/GenAI_Projects.git
cd your-repository-name

Create and activate a virtual environment (recommended):

Windows:
python -m venv venv
.\venv\Scripts\activate

macOS / Linux:
python3 -m venv venv
source venv/bin/activate

Install the required dependencies:
A requirements.txt file should be included with the necessary packages.
pip install -r requirements.txt
(If a requirements.txt is not available, install manually: pip install openai flask)

## API Key Setup
The projects need your OpenAI API key to function. The most secure way to manage this is with an environment variable.

Windows (Command Prompt):
set OPENAI_API_KEY="your-api-key-here"

Windows (PowerShell):
$env:OPENAI_API_KEY="your-api-key-here"

macOS / Linux:
export OPENAI_API_KEY="your-api-key-here"

Project Details
1. Simple Chat Assistant
A command-line Python application that simulates a conversation with an AI assistant. This is a great starting point for understanding the fundamentals of the Chat Completions API.

Features:

Continuous chat session in the terminal.

Remembers conversation history for contextual responses.

Simple, text-based interaction.

How to Run:
Navigate to the project directory and run the script:

python chat_assistant.py

2. Interactive DALL-E Image Generator
A web application built with Flask that allows users to generate images from text descriptions using the DALL-E model. It features a dynamic frontend that updates without page reloads.

Features:

Web-based UI for easy interaction.

Generates images from user prompts.

Asynchronous requests (AJAX) allow for new images to be generated without refreshing the page.

Clean, responsive design.

How to Run:
Navigate to the project directory and run the Flask app:
python app.py
Open your web browser and go to http://127.0.0.1:5000.

3. EduGenie: AI Educational Content Creator (Capstone)
A full-stack web application that acts as an AI-powered tool for educators. Users can enter a course title, and EduGenie generates a comprehensive educational plan.

Features:

Structured Content Generation: Creates a course objective, sample syllabus, learning outcomes, assessment methods, and recommended readings.

Bloom's Taxonomy Alignment: Learning outcomes are explicitly tied to different cognitive levels of Bloom's Taxonomy.

Reliable JSON Output: Utilizes the OpenAI API's JSON mode for predictable and easy-to-parse data.

Dynamic Frontend: A polished and responsive UI that updates instantly.

Error Handling: Gracefully manages potential API or network errors.

