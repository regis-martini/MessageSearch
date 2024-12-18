from fastapi import APIRouter, UploadFile, File # type: ignore
import os
import json
from app.services.search_service import process_and_store_messages

router = APIRouter()


@router.post("/upload")
async def upload_messages(file: UploadFile = File(...)):
    """
    Endpoint to upload message files.
    """
    try:
        contents = await file.read()
        messages = json.loads(contents.decode("utf-8"))
        process_and_store_messages(messages)  # Call the service
        return {
            "status": "success",
            "message": "Messages uploaded and processed successfully.",
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
