"""Utilities for transcribing audio files with optional timestamps."""

from __future__ import annotations

from collections import defaultdict
from math import floor
from typing import Any, Dict, Iterable, List


def transcribe_audio(audio_file_path: str, client) -> Dict[str, Any]:
    """Transcribe an audio file using Whisper and return text with segments.

    The response is requested in ``verbose_json`` format so that the Whisper API
    returns the individual segments alongside the full transcription. The
    returned dictionary always contains ``text`` and ``segments`` keys; when an
    exception occurs the error message is exposed under ``error``.
    """

    with open(audio_file_path, "rb") as audio_file:
        try:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                language="uk",
                response_format="verbose_json",
            )
            return {
                "text": getattr(transcription, "text", ""),
                "segments": getattr(transcription, "segments", []) or [],
            }
        except Exception as exc:  # pragma: no cover - simple error passthrough
            return {"text": "", "segments": [], "error": str(exc)}


def _segment_value(segment: Any, key: str, default: Any = None) -> Any:
    if isinstance(segment, dict):
        return segment.get(key, default)
    return getattr(segment, key, default)


def _format_timestamp(total_seconds: float) -> str:
    total_seconds = max(0, int(total_seconds))
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"


def format_segments_with_timestamps(
    segments: Iterable[Any], interval_seconds: int = 5
) -> List[str]:
    """Group Whisper segments into timestamped blocks.

    Each block represents a window of ``interval_seconds`` seconds and is
    formatted as ``MM:SS`` followed by the concatenated text recognised within
    that window. Empty text fragments are ignored and windows without text are
    skipped.
    """

    if interval_seconds <= 0:
        raise ValueError("interval_seconds must be positive")

    grouped_segments: Dict[int, List[str]] = defaultdict(list)

    for segment in segments or []:
        start = _segment_value(segment, "start")
        text = (_segment_value(segment, "text", "") or "").strip()

        if start is None or not text:
            continue

        bucket = interval_seconds * floor(float(start) / interval_seconds)
        grouped_segments[int(bucket)].append(text)

    formatted_blocks: List[str] = []
    for bucket_start in sorted(grouped_segments.keys()):
        bucket_text = " ".join(grouped_segments[bucket_start]).strip()
        if not bucket_text:
            continue
        timestamp = _format_timestamp(bucket_start)
        formatted_blocks.append(f"{timestamp}\n{bucket_text}")

    return formatted_blocks


__all__ = [
    "format_segments_with_timestamps",
    "transcribe_audio",
]
