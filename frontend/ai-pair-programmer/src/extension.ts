// src/extension.ts

// 1. Import necessary modules
// 'vscode' contains the VS Code extensibility API
import * as vscode from 'vscode';
// 'axios' is the library we'll use to make HTTP requests to our backend
import axios from 'axios';

// 2. The 'activate' function: This is the main entry point of your extension.
// It's called only once when your extension is activated.
export function activate(context: vscode.ExtensionContext) {

    // 3. Register our command
    // The command 'ai-pair-programmer.analyzeCode' must match the command field in package.json
    let disposable = vscode.commands.registerCommand('ai-pair-programmer.analyzeCode', async () => {
        // This is the code that will run every time the user executes our command.

        // 4. Get the active text editor
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage('No active text editor found. Please open a file to analyze.');
            return; // Stop execution if no file is open
        }

        // 5. Get the code from the editor
        const code = editor.document.getText();
        if (!code.trim()) {
            vscode.window.showInformationMessage('The file is empty. Please write some code to analyze.');
            return; // Stop if the file is empty
        }

        // Optional: Check if the file is a Python file
        if (editor.document.languageId !== 'python') {
            vscode.window.showWarningMessage('This extension is optimized for Python. Analysis for other languages may not be accurate.');
        }

        // 6. Create and show an output channel
        // This provides a clean way to show logs and results from our backend.
        const outputChannel = vscode.window.createOutputChannel('AI Pair Programmer');
        outputChannel.clear(); // Clear previous results
        outputChannel.show(true); // Bring the channel into view
        outputChannel.appendLine('🤖 Contacting the AI Pair Programmer...');

        // 7. Make the API call to our backend
        try {
            outputChannel.appendLine('Sending code for analysis...');
            const response = await axios.post('http://127.0.0.1:8000/analyze', {
                code: code
            });

            // 8. Display the result
            outputChannel.appendLine('✅ Analysis complete!');
            outputChannel.appendLine('---');

            // The response.data will contain the JSON from our FastAPI backend.
            // We use JSON.stringify to format it nicely before printing.
            const formattedJson = JSON.stringify(response.data, null, 4);
            outputChannel.appendLine(formattedJson);

        } catch (error: any) {
            // 9. Handle errors (e.g., backend is not running, network error)
            outputChannel.appendLine('❌ An error occurred.');
            if (axios.isAxiosError(error) && error.response) {
                // The request was made and the server responded with a status code
                // that falls out of the range of 2xx (e.g., our 400 SyntaxError)
                outputChannel.appendLine(`Error from backend: ${error.response.status} ${error.response.statusText}`);
                const formattedJson = JSON.stringify(error.response.data, null, 4);
                outputChannel.appendLine(formattedJson);
            } else {
                // Something happened in setting up the request that triggered an Error
                outputChannel.appendLine('Could not connect to the AI backend. Is it running?');
                outputChannel.appendLine(error.message);
            }
        }
    });

    // Add the command to the extension's context so it will be disposed of when the extension is deactivated
    context.subscriptions.push(disposable);
}

// 10. The 'deactivate' function: This is called when your extension is deactivated.
// You can use it to clean up any resources.
export function deactivate() {}
