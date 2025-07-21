# ai-pair-programmer README

This is the README for your extension "ai-pair-programmer". An intelligent, real-time coding assistant integrated directly into Visual Studio Code. This tool acts as an AI-powered pair programmer, enhancing developer productivity by providing context-aware suggestions, automated error detection, and intelligent refactoring options.

## Features

### Real-time Code Analysis
Send your current Python file to a powerful AI backend with a single command. The analysis is not just text-based - the system uses Abstract Syntax Trees (AST) to give the AI deep, structural context about the code's intent.

\!\[feature X\]\(images/feature-x.png\)

### AST-Powered Context
The system uses Abstract Syntax Trees (AST) to give the AI deep, structural context about the code's intent, providing more accurate suggestions than text-based analysis alone.

### GraphQL API Integration
Communication between the VS Code extension and the backend is handled by a modern, efficient GraphQL API for optimal performance.

### Integrated UI Experience
Suggestions and errors are displayed directly in the VS Code editor with native squiggly underlines and hover-over diagnostics, not just in a plain text log.

> Tip: The extension provides seamless integration with VS Code's native UI elements for the best user experience.

## Requirements

Before using this extension, you need to have the following dependencies installed and configured:

### Backend Server Requirements
* **Python 3.8+** - Required for the backend server
* **FastAPI** - High-performance web framework for the API
* **Google Gemini API Key** - Required for AI analysis capabilities

### Development Requirements
* **Node.js and npm** - For VS Code extension development
* **Visual Studio Code** - For development and testing

### Installation Steps

1. **Backend Setup:**
  ```bash
  cd backend
  python -m venv .venv
  source .venv/bin/activate  # macOS/Linux
  .\.venv\Scripts\activate   # Windows
  pip install -r requirements.txt
