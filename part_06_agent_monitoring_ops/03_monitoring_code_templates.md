# Giải thích template monitoring/ops

## 1. Mục tiêu file code

File `03_monitoring_code_templates.py` minh họa các khối monitoring cơ bản bằng standard Python: logging, đo latency, trace/span đơn giản, token/cost mock, JSONL log, evaluation record và alert rule.

## 2. Logging setup

```python
logging.basicConfig(...)
```

Logging giúp ghi lại sự kiện khi request chạy. Với AI app, log cần có request id để truy vết một câu hỏi từ đầu đến cuối.

## 3. Timing decorator

```python
@timing("mock_agent_request")
```

Decorator đo thời gian chạy của hàm. Trong hệ thống thật, metric này được gửi vào Prometheus, OpenTelemetry hoặc nền tảng observability.

## 4. Trace/span mock

```python
with span(request_id, "retrieve_context"):
    ...
```

Span đại diện cho một bước trong request. Nhiều span tạo thành trace. Với agent, span có thể là retrieval, tool call, LLM call, parsing.

## 5. Token/cost mock

```python
estimate_cost(input_tokens, output_tokens)
```

Cost tracking giúp phát hiện request bất thường hoặc prompt quá dài.

## 6. JSONL log

```python
write_jsonl_log(path, record)
```

JSONL phù hợp để lưu từng record trên một dòng. Trong production, thường dùng log collector thay vì ghi file thủ công.

## 7. Evaluation record

```python
make_evaluation_record(question, expected, actual, score)
```

Evaluation record giúp tạo dataset kiểm tra chất lượng chatbot/agent theo thời gian.

## 8. Alert condition

```python
should_alert(error_rate, avg_latency_ms, max_cost)
```

Alert giúp phát hiện lỗi sớm. Ngưỡng alert cần dựa trên yêu cầu thực tế.

## 9. Mapping sang công cụ thật

- `logging`: log collector hoặc cloud logging.
- `timing`: metrics backend.
- `span`: OpenTelemetry trace.
- `evaluation record`: LangSmith, Phoenix hoặc bảng evaluation nội bộ.
- `should_alert`: alert manager.

## 10. Common mistakes

- Logging sensitive data như API key, thông tin cá nhân.
- Không có request ID.
- Không đo latency từng bước.
- Không tracking cost/token.
- Không có evaluation dataset.
- Không có alerting.
- Chỉ log lỗi, không log luồng thành công nên khó so sánh.

## 11. Mini exercises

1. Thêm span `build_prompt`.
2. Thêm alert khi retrieval không có context.
3. Thêm field `model_name` vào log.
4. Viết hàm tính average latency từ list số.
5. Thiết kế một evaluation record có citation score.
