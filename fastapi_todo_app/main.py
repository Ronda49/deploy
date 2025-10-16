from fastapi import FastAPI

app = FastAPI()

todos = []


@app.get("/")
def read_root():
    """Return a welcome message."""
    return {"message": "Welcome to FastAPI Todo app"}


@app.post("/todo/")
def create_todo(item: str):
    """Add a new todo item."""
    todos.append(item)
    return {"item": item}
