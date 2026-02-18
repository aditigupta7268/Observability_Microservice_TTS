from fastapi import APIRouter
from app.observability.metrics import metrics_response
from app.observability.monitoring_service import get_dashboard_metrics

router = APIRouter(tags=["Monitoring"])

@router.get("/metrics")
def metrics():
    return metrics_response()

@router.get("/dashboard")
def dashboard():
    return get_dashboard_metrics()
