# ai_service.py

import os
from openai import OpenAI
import json

# Initialize the OpenAI client
# The client automatically looks for the OPENAI_API_KEY in environment variables.
try:
    client = OpenAI()
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    # In a real app, you might want to handle this more gracefully
    client = None

def get_ai_analysis(code: str, ast_representation: str):
    """
    Analyzes the given code and its AST using the OpenAI API.

    Args:
        code: The user's Python code as a string.
        ast_representation: The string representation of the code's AST.

    Returns:
        A dictionary containing the AI's analysis or an error message.
    """
    if not client:
        return {"error": "OpenAI client not initialized. Check your API key."}

    # This is the prompt from your project plan!
    # We are instructing the AI on its role, the task, and the desired output format (JSON).
    prompt = f"""
    You are an expert Python programmer acting as a code debugger. Analyze
    the following Python code and its Abstract Syntax Tree (AST). Identify any
    bugs, logical errors, or potential exceptions. Do not comment on style.

    For each error found, provide a JSON object with the following keys:
    - "line_number": The line where the error occurs.
    - "error_description": A clear explanation of the bug.
    - "suggested_fix": A concrete code suggestion to fix the bug.

    Respond ONLY with a valid JSON array of these error objects.
    If no errors are found, respond with an empty array [].

    Code:
    ```python
    {code}
    ```

    AST:
    ```
    {ast_representation}
    ```
    """

    try:
        # Make the API call to the chat completions endpoint
        response = client.chat.completions.create(
            model="gpt-4-turbo",  # Or "gpt-3.5-turbo" for a faster, cheaper option
            messages=[
                {"role": "system", "content": "You are a helpful Python code analysis assistant that responds in JSON."},
                {"role": "user", "content": prompt}
            ],
            # This ensures the model tries to output valid JSON
            response_format={"type": "json_object"}
        )

        # Extract the content from the response
        ai_response_content = response.choices[0].message.content

        # The response content should be a JSON string, so we parse it.
        # It's good practice to wrap this in a try-except in case the AI
        # doesn't return perfect JSON, despite our instructions.
        try:
            # The model might return a JSON object with a key, e.g. {"errors": [...]}.
            # We need to find the array.
            parsed_json = json.loads(ai_response_content)
            # Find the first key in the parsed JSON that holds a list (our array of suggestions)
            for key, value in parsed_json.items():
                if isinstance(value, list):
                    return value
            # If no list is found, return the raw parsed content
            return parsed_json

        except (json.JSONDecodeError, TypeError):
            # If parsing fails, return the raw text content
            return {"error": "Failed to parse AI response as JSON", "raw_response": ai_response_content}

    except Exception as e:
        # Handle potential API errors (e.g., network issues, invalid key)
        print(f"An error occurred with the OpenAI API call: {e}")
        return {"error": f"An error occurred with the OpenAI API: {e}"}

