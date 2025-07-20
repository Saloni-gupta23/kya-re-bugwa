// src/extension.ts

import * as vscode from 'vscode';
import axios from 'axios';

// --- NEW: Create a DiagnosticCollection ---
// This will manage all the squiggly lines and problems we report.
// We create it outside 'activate' so it persists.
const diagnosticCollection = vscode.languages.createDiagnosticCollection('aiPairProgrammer');

interface Suggestion {
    lineNumber: number;
    errorDescription: string;
    suggestedFix: string;
}

export function activate(context: vscode.ExtensionContext) {
    // When the extension is activated, we push our diagnostic collection to the context's subscriptions.
    // This ensures it's cleaned up properly when the extension is deactivated.
    context.subscriptions.push(diagnosticCollection);

    let disposable = vscode.commands.registerCommand('ai-pair-programmer.analyzeCode', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage('No active text editor found.');
            return;
        }

        const document = editor.document;
        const code = document.getText();
        if (!code.trim()) {
            vscode.window.showInformationMessage('The file is empty.');
            return;
        }

        // Show a progress notification to the user
        vscode.window.withProgress({
            location: vscode.ProgressLocation.Notification,
            title: "AI Pair Programmer",
            cancellable: false
        }, async (progress) => {
            progress.report({ message: "Analyzing your code..." });

            const graphqlQuery = {
                query: `
                    query AnalyzeCode($code: String!) {
                        analyzeCode(code: $code) {
                            lineNumber
                            errorDescription
                            suggestedFix
                        }
                    }
                `,
                variables: { code: code }
            };

            try {
                const response = await axios.post('http://127.0.0.1:8000/graphql', graphqlQuery, {
                    headers: { 'Content-Type': 'application/json' }
                });

                const suggestions: Suggestion[] = response.data.data.analyzeCode;

                // --- NEW: Process suggestions into Diagnostics ---
                const diagnostics: vscode.Diagnostic[] = [];
                if (suggestions && suggestions.length > 0) {
                    suggestions.forEach(suggestion => {
                        // VS Code lines are 0-indexed, but our AI gives 1-indexed lines.
                        const line = suggestion.lineNumber - 1;
                        
                        // Find the full line of text to underline the whole thing.
                        const lineOfText = document.lineAt(line);
                        const range = new vscode.Range(
                            new vscode.Position(line, lineOfText.firstNonWhitespaceCharacterIndex),
                            new vscode.Position(line, lineOfText.range.end.character)
                        );

                        // Create the diagnostic message
                        const message = `${suggestion.errorDescription}\nSuggested Fix: ${suggestion.suggestedFix}`;
                        
                        const diagnostic = new vscode.Diagnostic(
                            range,
                            message,
                            vscode.DiagnosticSeverity.Error // Show as a red error
                        );
                        // Provide a source for the error
                        diagnostic.source = 'AI Pair Programmer';
                        diagnostics.push(diagnostic);
                    });
                }
                
                // Clear old diagnostics for this file and set the new ones
                diagnosticCollection.set(document.uri, diagnostics);

                if (diagnostics.length > 0) {
                    vscode.window.showInformationMessage(`AI Pair Programmer found ${diagnostics.length} issue(s).`);
                } else {
                    vscode.window.showInformationMessage('AI Pair Programmer found no issues. Great work!');
                }

            } catch (error: any) {
                vscode.window.showErrorMessage('Failed to get analysis. Is the backend server running?');
                console.error(error);
            }
        });
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {
    // When the extension is deactivated, clear all diagnostics.
    diagnosticCollection.clear();
}
