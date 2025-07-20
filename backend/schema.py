# backend/schema.py

import strawberry
from typing import List, Optional
from ai_service import get_ai_analysis # We'll reuse our existing AI service!
import ast

# 1. Define the 'Suggestion' type for GraphQL.
# This tells Strawberry what a "Suggestion" object looks like.
# It matches the schema from your project plan.
@strawberry.type
class Suggestion:
    line_number: int
    error_description: str
    suggested_fix: str

# 2. Define the main 'Query' type.
# Queries are how clients ask for data.
@strawberry.type
class Query:
    # This defines a query named 'analyzeCode'.
    # It takes one argument: 'code' (a string).
    # It returns a list of 'Suggestion' objects.
    @strawberry.field
    def analyzeCode(self, code: str) -> List[Suggestion]:
        """
        Analyzes the given Python code and returns a list of suggestions.
        """
        print("GraphQL query received for code analysis.")
        try:
            # We reuse our existing logic!
            # First, generate the AST.
            ast_representation = ast.dump(ast.parse(code), indent=4)
            # Then, call our AI service.
            analysis_result = get_ai_analysis(code, ast_representation)

            # The AI service returns a list of dictionaries. We need to convert
            # this into a list of 'Suggestion' objects for GraphQL.
            if isinstance(analysis_result, list):
                return [Suggestion(**item) for item in analysis_result]
            else:
                # If the AI returns an error, we can return it in a specific way
                # For now, we'll return an empty list on error.
                print(f"AI service returned an error: {analysis_result}")
                return []

        except SyntaxError as e:
            # If the code has a syntax error, we can't analyze it.
            # We return an empty list. In a more advanced setup, we could
            # define a custom GraphQL error for this.
            print(f"Syntax error in user code: {e}")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

# 3. Create the final schema object that FastAPI will use.
schema = strawberry.Schema(query=Query)
