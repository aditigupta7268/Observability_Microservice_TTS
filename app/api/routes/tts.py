from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.schemas.tts_schema import TTSRequest
from app.services.tts_service import generate_audio

router = APIRouter(
    prefix="/tts",
    tags=["TTS"]
)

@router.post("/")
def create_tts(request: TTSRequest):
    """
    Generates TTS audio file.
    Also stores:
        - audio (.mp3)
        - metadata (.json)
        - metrics snapshot (_metrics.json)
    inside output folder.
    """

    file_path = generate_audio(request.text)

    return FileResponse(
        path=str(file_path),
        media_type="audio/mpeg",
        filename=file_path.name
    )
