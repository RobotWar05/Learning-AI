"""Template monitoring/ops giáo dục, chỉ dùng standard Python."""

import json
import logging
import sys
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from functools import wraps


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s request_id=%(request_id)s %(message)s",
)
logger = logging.getLogger("ai_monitoring_demo")


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def log_event(request_id, event_name, **fields):
    """Ghi log có cấu trúc ở mức đơn giản."""
    payload = {"event": event_name, **fields}
    logger.info(json.dumps(payload, ensure_ascii=False), extra={"request_id": request_id})


def timing(metric_name):
    """Decorator đo thời gian chạy của một hàm."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed_ms = (time.perf_counter() - start) * 1000
            print(f"metric={metric_name} latency_ms={elapsed_ms:.2f}")
            return result

        return wrapper

    return decorator


@contextmanager
def span(request_id, name):
    """Mock span để minh họa trace."""
    start = time.perf_counter()
    log_event(request_id, "span_start", span=name)
    try:
        yield
        status = "ok"
    except Exception as exc:
        status = "error"
        log_event(request_id, "span_error", span=name, error=str(exc))
        raise
    finally:
        elapsed_ms = (time.perf_counter() - start) * 1000
        log_event(request_id, "span_end", span=name, status=status, latency_ms=elapsed_ms)


def estimate_cost(input_tokens, output_tokens, price_per_1k_tokens=0.001):
    """Ước lượng cost đơn giản theo token."""
    total_tokens = input_tokens + output_tokens
    return total_tokens / 1000 * price_per_1k_tokens


def write_jsonl_log(path, record):
    """Ghi một record JSONL."""
    with open(path, "a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")


def make_evaluation_record(question, expected, actual, score):
    """Tạo record evaluation đơn giản."""
    return {
        "time": now_iso(),
        "question": question,
        "expected": expected,
        "actual": actual,
        "score": score,
    }


def should_alert(error_rate, avg_latency_ms, max_cost):
    """Điều kiện alert đơn giản."""
    alerts = []
    if error_rate > 0.05:
        alerts.append("error_rate_high")
    if avg_latency_ms > 3000:
        alerts.append("latency_high")
    if max_cost > 1.0:
        alerts.append("cost_high")
    return alerts


@timing("mock_agent_request")
def handle_request(request_id, question):
    with span(request_id, "retrieve_context"):
        context = "context mau ve AI"
    with span(request_id, "call_llm"):
        answer = f"Tra loi dua tren {context}: {question}"
    input_tokens = len(question.split()) + len(context.split())
    output_tokens = len(answer.split())
    cost = estimate_cost(input_tokens, output_tokens)
    log_event(
        request_id,
        "request_done",
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        cost=cost,
    )
    return answer


if __name__ == "__main__":
    request_id = "req-001"
    answer = handle_request(request_id, "Machine Learning la gi?")
    print("Answer:", answer)
    print("Cost estimate:", estimate_cost(20, 30))
    print("Evaluation:", make_evaluation_record("AI là gì?", "Trả lời đúng", answer, 0.8))
    print("Alerts:", should_alert(error_rate=0.08, avg_latency_ms=1200, max_cost=0.2))

    print("\nJSONL write example - đang comment để không tạo file phụ:")
    # write_jsonl_log("monitoring_log.jsonl", {"time": now_iso(), "answer": answer})
