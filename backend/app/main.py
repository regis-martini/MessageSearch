from fastapi import FastAPI # type: ignore
from app.api.v1.messages import router as messages_router

app = FastAPI(title="MessageSearch", version="1.0.0")

# Include message-related routes
app.include_router(messages_router, prefix="/api/v1/messages")
