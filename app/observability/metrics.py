from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import Response

REQUEST_COUNT = Counter(
    "tts_requests_total",
    "Total TTS requests",
    ["endpoint", "method", "status"]
)

REQUEST_LATENCY = Histogram(
    "tts_latency_seconds",
    "Latency per endpoint",
    ["endpoint"]
)

ERROR_COUNT = Counter(
    "tts_errors_total",
    "Total failed requests"
)

def metrics_response():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
