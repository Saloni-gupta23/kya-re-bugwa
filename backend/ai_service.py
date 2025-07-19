# ai_service.py

import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# --- FIX ---
# Load environment variables from .env file right at the start.
load_dotenv()
# --- END FIX ---

# Configure the Gemini API client
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        # This error will now correctly trigger only if the key is truly missing from the .env file
        raise ValueError("GOOGLE_API_KEY not found in environment variables. Make sure it's set in your .env file.")
    genai.configure(api_key=api_key)
    # Initialize the Generative Model
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"Error configuring Gemini client: {e}")
    model = None

def get_ai_analysis(code: str, ast_representation: str):
    """
    Analyzes the given code and its AST using the Google Gemini API.
    """
    if not model:
        return {"error": "Gemini client not initialized. Check your API key and configuration."}

    prompt = f"""
    You are an expert Python code analysis tool. Your task is to identify bugs in a given Python code snippet.
    Analyze the following Python code and its corresponding Abstract Syntax Tree (AST).

    Respond with a JSON array of objects. Each object represents a single bug and must have the following keys:
    - "line_number": (Integer) The line where the bug occurs.
    - "error_description": (String) A clear, concise explanation of the bug.
    - "suggested_fix": (String) A concrete code snippet suggesting how to fix the bug.

    If you find no bugs, you MUST return an empty JSON array: [].
    Do not include any text, explanations, or markdown formatting outside of the JSON array itself.

    Here is the code to analyze:
    ---
    CODE:
    ```python
    {code}
    ```
    ---
    AST:
    ```
    {ast_representation}
    ```
    ---
    JSON Response:
    """

    try:
        response = model.generate_content(prompt)
        ai_response_text = response.text.strip()
        
        if ai_response_text.startswith("```json"):
            ai_response_text = ai_response_text[7:]
        if ai_response_text.startswith("```"):
            ai_response_text = ai_response_text[3:]
        if ai_response_text.endswith("```"):
            ai_response_text = ai_response_text[:-3]
        
        ai_response_text = ai_response_text.strip()

        parsed_json = json.loads(ai_response_text)
        return parsed_json

    except json.JSONDecodeError:
        return {"error": "Failed to parse AI response as JSON.", "raw_response": response.text}
    except Exception as e:
        print(f"An error occurred with the Gemini API call: {e}")
        return {"error": f"An error occurred with the Gemini API: {str(e)}"}

