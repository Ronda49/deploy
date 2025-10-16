from fastapi import FastAPI

app = FastAPI()

todos = []

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Todo App"}

@app.get("/todos")
def get_todos():
    return {"todos": todos}

@app.post("/todos")
def add_todo(item: str):
    todos.append(item)
    return {"message": f"Added '{item}' to list"}

@app.delete("/todos/{index}")
def delete(index: int):
    if 0 <= index < len(todos):
        deleted = todos.pop(index)
        return {"message": f"Deleted '{deleted}'"}
    return {"error": "Invalid index"}
