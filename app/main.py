from fastapi import FastAPI

from app.api.routes.todo.read import router as todo_read


app = FastAPI()
app.include_router(router=todo_read)