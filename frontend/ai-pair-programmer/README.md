# AI Pair Programmer

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![VS Code](https://img.shields.io/badge/VS%20Code-1.80%2B-blue)](https://code.visualstudio.com/)

An intelligent, real-time coding assistant integrated directly into Visual Studio Code. This tool acts as an AI-powered pair programmer, enhancing developer productivity by providing context-aware suggestions and automated error detection.

---

### Core Features

* **Intelligent Code Analysis:** Leverages the Google Gemini API to perform deep, contextual analysis of Python code.
* **AST-Powered Context:** Goes beyond simple text analysis by using Abstract Syntax Trees (AST) to understand the code's fundamental structure and intent.
* **Real-time Diagnostics:** Displays errors and suggestions directly in the VS Code editor with native squiggly underlines and hover-over problem descriptions.
* **Modern GraphQL API:** Built with a flexible and efficient GraphQL API using FastAPI and Strawberry for seamless communication between the editor and the backend.
* **VS Code Integration:** Operates as a lightweight, fully integrated extension within the familiar environment of Visual Studio Code.

---

### Technology Stack & Architecture

This project uses a client-server architecture to separate the frontend interface from the backend AI processing logic.

| Component        | Technology                               | Purpose                                                              |
| :--------------- | :--------------------------------------- | :------------------------------------------------------------------- |
| **Client** | VS Code Extension (TypeScript)           | The user-facing interface that lives in the developer's editor.      |
| **Backend Server** | Python & FastAPI                        | A high-performance web framework to build and serve the API.         |
| **AI Core** | Google Gemini API & Python `ast` module  | The "brain" responsible for analyzing the code and its structure.    |
| **API Layer** | GraphQL (with Strawberry)                | An efficient and flexible query language for client-server communication. |

---

### Local Development Setup

This project is structured as a monorepo. Follow the steps below to get both the backend and frontend running.

#### 1. Backend Server Setup

First, set up the Python server which handles the AI logic.

```bash
# 1. Navigate to the backend directory from the project root
cd backend

# 2. Create a Python virtual environment
python -m venv .venv

# 3. Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows (Command Prompt/PowerShell):
.\\.venv\\Scripts\\activate

# 4. Install the required Python packages from the requirements file
pip install -r requirements.txt

# 5. Create a .env file in the 'backend' directory.
#    Add your Google API key to this file:
#    GOOGLE_API_KEY="your_api_key_here"

# 6. Start the FastAPI server
uvicorn main:app --reload
```
The backend will now be running and listening at `http://127.0.0.1:8000`.

#### 2. Frontend Extension Setup

Next, set up the VS Code extension which acts as the client.

```bash
# 1. From the project root, navigate to the frontend directory
cd frontend/ai-pair-programmer

# 2. Install the required Node.js packages
npm install

# 3. Open ONLY this frontend folder in a *separate* VS Code window.
#    (File -> Open Folder... -> select 'frontend/ai-pair-programmer')

# 4. In this new VS Code window, start the extension debugger
#    by pressing F5.
```
This will open a new "Extension Development Host" window where you can test the extension.

---

### How to Use the Extension

1.  Ensure both the backend server and the Extension Development Host are running as described above.
2.  In the **Extension Development Host** window, open any Python file (`.py`).
3.  Open the Command Palette (`Ctrl+Shift+P` on Windows/Linux, `Cmd+Shift+P` on macOS).
4.  Type and select the command **"Analyze Code with AI Pair Programmer"**.
5.  Bugs or suggestions found by the AI will appear as problems with red squiggly underlines directly in your code. Hover over them to see the details.

---

### Project Status

This project is being developed in phases. The current status is as follows:

* [x] **Phase 1:** Core Backend & AI Logic
* [x] **Phase 2:** VS Code Extension Client
* [x] **Phase 3:** GraphQL Integration & UI Improvements
* [ ] **Phase 4:** PostgreSQL Database & User Management
* [ ] **Phase 5:** Dockerization & Deployment

**Next Up:** Implementing a database to manage users and projects.
