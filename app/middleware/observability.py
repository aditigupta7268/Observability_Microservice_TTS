import time
import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from app.observability.metrics import REQUEST_COUNT, REQUEST_LATENCY, ERROR_COUNT
from app.core.logger import get_logger

logger = get_logger(__name__)

class ObservabilityMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        trace_id = str(uuid.uuid4())
        start_time = time.time()

        try:
            response = await call_next(request)

            latency = time.time() - start_time

            REQUEST_COUNT.labels(
                endpoint=request.url.path,
                method=request.method,
                status=response.status_code
            ).inc()

            REQUEST_LATENCY.labels(
                endpoint=request.url.path
            ).observe(latency)

            logger.info(
                f"{request.method} {request.url.path} completed",
                extra={"trace_id": trace_id}
            )

            response.headers["X-Trace-ID"] = trace_id
            return response

        except Exception as e:
            ERROR_COUNT.inc()
            logger.error(str(e), extra={"trace_id": trace_id})
            raise e
