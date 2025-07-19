# main.py

import os
import ast
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Import our AI service function (the file name doesn't change)
from ai_service import get_ai_analysis

# Load environment variables from the .env file
load_dotenv()

# Check if the GOOGLE_API_KEY is set
if not os.getenv("GOOGLE_API_KEY"):
    print("Warning: GOOGLE_API_KEY environment variable not set.")

class CodeSnippet(BaseModel):
    code: str

app = FastAPI(
    title="AI Pair Programmer",
    description="The backend server for the AI Pair Programmer VS Code extension.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "Hello, World! The AI Pair Programmer backend is running."}

@app.post("/analyze")
def analyze_code(snippet: CodeSnippet):
    """
    Receives code, parses it, and sends it to the AI for analysis.
    """
    try:
        # 1. Parse the code into an AST
        parsed_ast = ast.parse(snippet.code)
        ast_representation = ast.dump(parsed_ast, indent=4)

        # 2. Send the code and AST to the AI service for analysis
        ai_result = get_ai_analysis(snippet.code, ast_representation)

        # 3. Return the AI's response
        return {
            "status": "success",
            "analysis": ai_result
        }
    except SyntaxError as e:
        # Handle syntax errors from the user's code
        raise HTTPException(
            status_code=400,
            detail=f"Syntax Error: {e.msg} at line {e.lineno}, offset {e.offset}",
        )
    except Exception as e:
        # Handle other potential errors during the process
        raise HTTPException(
            status_code=500,
            detail=f"An internal error occurred: {str(e)}"
        )
