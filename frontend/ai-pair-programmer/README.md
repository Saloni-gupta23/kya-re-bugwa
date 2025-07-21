ai-pair-programmer README
This is the README for your extension "ai-pair-programmer". An intelligent, real-time coding assistant integrated directly into Visual Studio Code. This tool acts as an AI-powered pair programmer, enhancing developer productivity by providing context-aware suggestions, automated error detection, and intelligent refactoring options.
Features
Real-time Code Analysis
Send your current Python file to a powerful AI backend with a single command. The analysis is not just text-based - the system uses Abstract Syntax Trees (AST) to give the AI deep, structural context about the code's intent.
![feature X](images/feature-x.png)
AST-Powered Context
The system uses Abstract Syntax Trees (AST) to give the AI deep, structural context about the code's intent, providing more accurate suggestions than text-based analysis alone.
GraphQL API Integration
Communication between the VS Code extension and the backend is handled by a modern, efficient GraphQL API for optimal performance.
Integrated UI Experience
Suggestions and errors are displayed directly in the VS Code editor with native squiggly underlines and hover-over diagnostics, not just in a plain text log.

Tip: The extension provides seamless integration with VS Code's native UI elements for the best user experience.

Requirements
Before using this extension, you need to have the following dependencies installed and configured:
Backend Server Requirements

Python 3.8+ - Required for the backend server
FastAPI - High-performance web framework for the API
Google Gemini API Key - Required for AI analysis capabilities

Development Requirements

Node.js and npm - For VS Code extension development
Visual Studio Code - For development and testing

Installation Steps

Backend Setup:
bashcd backend
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.\.venv\Scripts\activate   # Windows
pip install -r requirements.txt

Environment Configuration:
Create a .env file and add your Google API key:
GOOGLE_API_KEY=your_api_key_here

Start the Backend Server:
bashuvicorn main:app --reload

Frontend Setup:
bashcd frontend/ai-pair-programmer
npm install


Extension Settings
This extension contributes the following settings:

aiPairProgrammer.enable: Enable/disable the AI Pair Programmer extension
aiPairProgrammer.backendUrl: Set the backend server URL (default: http://localhost:8000)
aiPairProgrammer.autoAnalyze: Automatically analyze code on file save
aiPairProgrammer.showInlineErrors: Display errors directly in the editor with squiggly underlines

Technology Stack
ComponentTechnologyPurposeClientVS Code Extension (TypeScript)The frontend that lives in the user's editorBackend ServerPython & FastAPIA high-performance web framework for the APIAI CoreGoogle Gemini API & Python ast moduleThe "brain" that analyzes the code and its structureAPI LayerGraphQL (with Strawberry)An efficient and flexible query language for the API
Known Issues

Currently supports Python files only - support for other languages is planned for future releases
Requires active internet connection for AI analysis
Large files (>1000 lines) may take longer to analyze

Release Notes
1.0.0
Initial release of AI Pair Programmer

Real-time Python code analysis
AST-powered context understanding
GraphQL API integration
Native VS Code UI integration

1.0.1
Fixed issue with backend connection timeout

Improved error handling for network issues
Better user feedback for connection problems

1.1.0
Added features:

Automated error detection with inline display
Intelligent refactoring suggestions
Performance optimizations for large files


How to Run the Project
This project is structured as a monorepo with two main parts: the backend server and the frontend VS Code extension.
Running the Backend

Navigate to the backend directory: cd backend
Create and activate a Python virtual environment
Install required packages: pip install -r requirements.txt
Create .env file with your GOOGLE_API_KEY
Run the server: uvicorn main:app --reload

Running the Frontend

Navigate to: cd frontend/ai-pair-programmer
Install dependencies: npm install
Open the folder in a separate VS Code window
Press F5 to start the Extension Development Host
Open a Python file and run the "Analyze Code with AI Pair Programmer" command

Following extension guidelines
Ensure that you've read through the extensions guidelines and follow the best practices for creating your extension.

Extension Guidelines

Working with Markdown
You can author your README using Visual Studio Code. Here are some useful editor keyboard shortcuts:

Split the editor (Cmd+\ on macOS or Ctrl+\ on Windows and Linux).
Toggle preview (Shift+Cmd+V on macOS or Shift+Ctrl+V on Windows and Linux).
Press Ctrl+Space (Windows, Linux, macOS) to see a list of Markdown snippets.

For more information

Visual Studio Code's Markdown Support
Markdown Syntax Reference

Enjoy!
