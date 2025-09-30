"""Transcription response models."""
from datetime import timedelta
from pydantic import BaseModel


class TranscriptionSegment(BaseModel):
    start: float
    end: float
    text_hy: str
    text_en: str | None = None

    @property
    def duration(self) -> float:
        return self.end - self.start


class TranscriptionJobResponse(BaseModel):
    job_id: str
    status: str = "queued"
    language: str = "hy"
    segments: list[TranscriptionSegment] = []
    translated: bool = False

    @property
    def total_duration(self) -> float:
        return sum(segment.duration for segment in self.segments)

    @property
    def total_segments(self) -> int:
        return len(self.segments)
