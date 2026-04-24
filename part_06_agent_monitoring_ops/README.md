# Phần 6: Agent Monitoring và Ops

## Mục tiêu

Hiểu cách quan sát, đánh giá và vận hành chatbot/agent AI: log gì, đo gì, trace gì, cảnh báo gì và xử lý sự cố ra sao.

## Monitoring là gì

Monitoring là theo dõi hệ thống bằng số liệu và sự kiện để biết hệ thống đang hoạt động tốt hay có lỗi.

## Observability là gì

Observability là khả năng hiểu trạng thái bên trong hệ thống thông qua logs, metrics và traces. Với agent, observability giúp biết request đi qua bước nào, tool nào được gọi, lỗi ở đâu.

## Vì sao chatbot/agent cần monitoring

- LLM có thể trả lời sai hoặc hallucinate.
- Retrieval có thể lấy sai context.
- Tool calling có thể lỗi.
- Chi phí token có thể tăng bất thường.
- Latency có thể vượt ngưỡng.
- Prompt/model/data thay đổi có thể gây regression.

## Logs, metrics, traces

- Logs: sự kiện chi tiết.
- Metrics: chỉ số tổng hợp như latency, error rate, cost.
- Traces: đường đi của một request qua nhiều bước.

## Evaluation

Evaluation kiểm tra chất lượng câu trả lời bằng bộ câu hỏi chuẩn, human feedback hoặc LLM-as-judge.

## Feedback loop

Feedback từ người dùng và lỗi production cần được đưa lại vào dataset evaluation để cải thiện prompt, retrieval hoặc model.

## Deployment mindset

Triển khai AI không chỉ là chạy được. Cần version prompt/model/data, rollback được, có alert và có quy trình xử lý incident.

## File trong phần này

- [Checklist](./00_checklist.md)
- [Monitoring notes](./01_monitoring_notes.md)
- [Ops architecture notes](./02_ops_architecture_notes.md)
- [Template monitoring](./03_monitoring_code_templates.py)
- [Giải thích template monitoring](./03_monitoring_code_templates.md)
- [Bài tập](./04_exercises.md)
- [Ôn nhanh](./05_quick_review.md)

## Thứ tự học

1. Học logs/metrics/traces.
2. Học các chỉ số riêng cho LLM/RAG.
3. Học kiến trúc deployment.
4. Đọc template logging/tracing.
5. Làm bài tập thiết kế dashboard và alert.
