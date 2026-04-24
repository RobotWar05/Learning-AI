# Ghi chú monitoring

## 1. Logs

Logs ghi lại sự kiện chi tiết. Với chatbot, log nên có request id, thời điểm, câu hỏi, trạng thái, lỗi, latency và metadata cần thiết.

Không nên log dữ liệu nhạy cảm nếu không cần.

## 2. Metrics

Metrics là chỉ số tổng hợp theo thời gian:

- Latency trung bình.
- P95 latency.
- Error rate.
- Số request/phút.
- Token usage.
- Cost.
- Tỷ lệ retrieval có context.
- Tỷ lệ answer bị user đánh giá xấu.

## 3. Traces

Trace mô tả đường đi của một request. Một trace gồm nhiều span.

Ví dụ:

```text
request
├── retrieve_context
├── build_prompt
├── call_llm
└── evaluate_answer
```

## 4. Spans

Span là một bước nhỏ trong trace, có thời gian bắt đầu/kết thúc và trạng thái thành công/thất bại.

## 5. Latency và throughput

- Latency: thời gian xử lý một request.
- Throughput: số request xử lý trong một đơn vị thời gian.

## 6. Error rate

Error rate là tỷ lệ request lỗi. Với AI app, lỗi có thể là HTTP error, tool error, timeout, parse error hoặc retrieval empty.

## 7. Token usage và cost tracking

LLM tính chi phí theo token. Cần theo dõi input tokens, output tokens và cost ước lượng để phát hiện tăng bất thường.

## 8. Quality metrics

Quality không chỉ là hệ thống có trả lời hay không. Cần đo:

- Answer correctness.
- Faithfulness: câu trả lời có bám context không.
- Retrieval relevance.
- Citation correctness.
- User satisfaction.

## 9. Hallucination check

Hallucination có thể kiểm tra bằng rule, human review hoặc LLM-as-judge. Với dữ liệu quan trọng, cần trích nguồn và kiểm tra bằng câu hỏi chuẩn.

## 10. Retrieval metrics

- Context có được tìm thấy không.
- Context có liên quan không.
- Top-k có chứa đoạn đúng không.
- Reranker có cải thiện không.

## 11. LLM-as-judge

LLM-as-judge dùng một model để chấm câu trả lời. Cần cẩn thận vì judge cũng có thể sai. Không nên xem là sự thật tuyệt đối.

## 12. Human feedback

Feedback người dùng giúp phát hiện lỗi thực tế. Nên lưu rating, comment và request id.

## 13. Alerting

Alert nên kích hoạt khi:

- Error rate vượt ngưỡng.
- Latency tăng mạnh.
- Cost tăng bất thường.
- Retrieval empty quá nhiều.
- Feedback xấu tăng.

## 14. Dashboard

Dashboard nên hiển thị latency, traffic, error rate, cost, token usage, retrieval quality và evaluation score.
