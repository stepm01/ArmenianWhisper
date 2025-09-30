"""Placeholder transcription service implementation."""
import asyncio
import uuid
from fastapi import UploadFile

from ..schemas.transcription import TranscriptionJobResponse, TranscriptionSegment


async def process_transcription_job(file: UploadFile) -> TranscriptionJobResponse:
    """Mock transcription pipeline; replace with real model inference."""
    # Simulate async processing to keep the contract realistic.
    await asyncio.sleep(0)

    dummy_segment = TranscriptionSegment(
        start=0.0,
        end=5.2,
        text_hy="Դասական նախադասություն վերապատմման համար։",
        text_en="Sample sentence for future translation pipeline.",
    )

    return TranscriptionJobResponse(
        job_id=str(uuid.uuid4()),
        status="completed",
        language="hy",
        segments=[dummy_segment],
        translated=True,
    )
