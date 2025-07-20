# backend/main.py

from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from schema import schema # Import the schema we just created

# Create the GraphQL router, passing in our schema
graphql_app = GraphQLRouter(schema)

# Create the main FastAPI app
app = FastAPI(
    title="AI Pair Programmer - GraphQL",
    description="The GraphQL backend for the AI Pair Programmer.",
    version="0.2.0",
)

# Include the GraphQL router at the '/graphql' endpoint
# All GraphQL requests will now go to http://127.0.0.1:8000/graphql
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def read_root():
    """
    A simple root endpoint to confirm the server is running.
    """
    return {"status": "The AI Pair Programmer GraphQL backend is running!"}
