from app.observability.metrics import REQUEST_COUNT, ERROR_COUNT

def get_dashboard_metrics():

    total_requests = sum(
        sample.value for sample in REQUEST_COUNT.collect()[0].samples
        if sample.name.endswith("_total")
    )

    total_errors = sum(
        sample.value for sample in ERROR_COUNT.collect()[0].samples
    )

    error_rate = (
        (total_errors / total_requests) * 100
        if total_requests > 0 else 0
    )

    return {
        "total_requests": total_requests,
        "total_errors": total_errors,
        "error_rate_percent": round(error_rate, 2)
    }
