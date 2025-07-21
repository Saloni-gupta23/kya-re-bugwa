# 🤖 AI Pair Programmer

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![VS Code](https://img.shields.io/badge/VS%20Code-1.80%2B-blue)](https://code.visualstudio.com/)

An intelligent, real-time coding assistant integrated directly into Visual Studio Code. This tool acts as an AI-powered pair programmer, enhancing developer productivity by providing context-aware suggestions and automated error detection.

---

### ✨ Demo

*(It is highly recommended to record a short GIF of the extension in action and place it here. You can use tools like [LiceCap](https://www.cockos.com/licecap/) or [ScreenToGif](https://www.screentogif.com/) to create one.)*

![AI Pair Programmer Demo](https://i.imgur.com/g8c5YtM.gif) 
*A demonstration showing the extension identifying a bug and providing a suggestion.*

---

### 🚀 Core Features

* **🧠 Intelligent Code Analysis:** Leverages the Google Gemini API to perform deep, contextual analysis of your Python code.
* **AST-Powered Context:** Goes beyond simple text analysis by using Abstract Syntax Trees (AST) to understand the code's fundamental structure and intent.
* **⚡️ Real-time Diagnostics:** Displays errors and suggestions directly in the VS Code editor with native squiggly underlines and hover-over problem descriptions.
* **🌐 Modern GraphQL API:** Built with a flexible and efficient GraphQL API using FastAPI and Strawberry for seamless communication between the editor and the backend.
* **💻 VS Code Integration:** Operates as a lightweight, fully integrated extension within the familiar environment of Visual Studio Code.

---

### 🛠️ Technology Stack & Architecture

This project uses a client-server architecture to separate the frontend interface from the backend AI processing logic.

| Component         | Technology                               | Purpose                                                              |
| :---------------- | :--------------------------------------- | :------------------------------------------------------------------- |
| **Client** | VS Code Extension (TypeScript)           | The user-facing interface that lives in the developer's editor.      |
| **Backend Server** | Python & FastAPI                        | A high-performance web framework to build and serve the API.         |
| **AI Core** | Google Gemini API & Python `ast` module  | The "brain" responsible for analyzing the code and its structure.    |
| **API Layer** | GraphQL (with Strawberry)                | An efficient and flexible query language for client-server communication. |

---

### ⚙️ Setup and Installation

This project is structured as a monorepo. Follow the steps below to get both the backend and frontend running.

#### 1. Backend Server Setup

First, set up the Python server which handles the AI logic.

```bash
# 1. Navigate to the backend directory
cd backend

# 2. Create and activate a Python virtual environment
python -m venv .venv
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.\\.venv\\Scripts\\activate

# 3. Create a requirements.txt file
pip freeze > requirements.txt

# 4. Install the required packages
pip install -r requirements.txt

# 5. Create a .env file in the 'backend' directory
#    and add your Google API key:
#    GOOGLE_API_KEY="your_api_key_here"

# 6. Start the server!
uvicorn main:app --reload
