from app.observability.metrics import REQUEST_COUNT, ERROR_COUNT, REQUEST_LATENCY


def collect_metrics_snapshot():

    # Total Requests
    total_requests = sum(
        sample.value for sample in REQUEST_COUNT.collect()[0].samples
        if sample.name.endswith("_total")
    )

    # Total Errors
    total_errors = sum(
        sample.value for sample in ERROR_COUNT.collect()[0].samples
    )

    # Latency stats
    latency_samples = REQUEST_LATENCY.collect()[0].samples

    return {
        "total_requests": total_requests,
        "total_errors": total_errors,
        "latency_samples": [
            {
                "name": s.name,
                "labels": s.labels,
                "value": s.value
            }
            for s in latency_samples
        ]
    }
