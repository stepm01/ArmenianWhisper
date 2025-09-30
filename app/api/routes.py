"""API routes for ArmenianWhisper backend."""
from fastapi import APIRouter, File, HTTPException, UploadFile

from ..schemas.transcription import TranscriptionJobResponse
from ..services.transcription import process_transcription_job

router = APIRouter()


@router.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    """Health probe for uptime monitoring."""
    return {"status": "ok"}


@router.post("/transcribe", response_model=TranscriptionJobResponse, tags=["transcription"])
async def transcribe_audio(file: UploadFile = File(...)) -> TranscriptionJobResponse:
    """Accept an audio file and return a transcription job response."""
    if not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Unsupported file type. Provide an audio file.")
    return await process_transcription_job(file)
