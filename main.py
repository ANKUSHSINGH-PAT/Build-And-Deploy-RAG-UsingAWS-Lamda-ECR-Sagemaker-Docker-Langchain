from fastapi import FastAPI
from QASystem.api import router as qa_router
from QASystem.config import settings

app = FastAPI(title=settings.APP_NAME)
app.include_router(qa_router, prefix="/qa")

@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.APP_NAME}!"}
