from gtts import gTTS
from pathlib import Path
import time
import uuid
import json
from datetime import datetime
from app.core.config import settings
from app.observability.metrics_snapshot import collect_metrics_snapshot


def generate_audio(text: str):

    start_time = time.time()

    output_dir = settings.output_path
    output_dir.mkdir(parents=True, exist_ok=True)

    unique_id = uuid.uuid4().hex[:8]
    timestamp = int(time.time())

    filename = f"{timestamp}_{unique_id}.mp3"
    file_path = output_dir / filename

    # Generate MP3
    tts = gTTS(text=text, lang="en")
    tts.save(str(file_path))

    latency = time.time() - start_time

    # -------------------------
    # 1️⃣ Request Metadata JSON
    # -------------------------
    metadata = {
        "id": unique_id,
        "text": text,
        "filename": filename,
        "file_path": str(file_path),
        "created_at": datetime.utcnow().isoformat(),
        "file_size_bytes": file_path.stat().st_size,
        "latency_seconds": round(latency, 4)
    }

    json_path = output_dir / f"{timestamp}_{unique_id}.json"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)

    # -------------------------
    # 2️⃣ Metrics Snapshot JSON
    # -------------------------
    metrics_snapshot = collect_metrics_snapshot()

    metrics_path = output_dir / f"{timestamp}_{unique_id}_metrics.json"

    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_snapshot, f, indent=4)

    return file_path
