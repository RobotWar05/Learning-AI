# Ôn nhanh Agent Monitoring/Ops

## Bảng thuật ngữ

| Thuật ngữ | Ý nghĩa |
|---|---|
| Log | Sự kiện chi tiết |
| Metric | Chỉ số đo theo thời gian |
| Trace | Đường đi của request |
| Span | Một bước trong trace |
| Latency | Thời gian phản hồi |
| Throughput | Lưu lượng xử lý |
| Error rate | Tỷ lệ request lỗi |
| Token usage | Số token tiêu thụ |
| Cost tracking | Theo dõi chi phí |
| Alerting | Cảnh báo khi vượt ngưỡng |
| Rollback | Quay về phiên bản ổn định |
| Audit log | Ghi thay đổi quan trọng |

## Logs vs metrics vs traces

| Loại | Trả lời câu hỏi |
|---|---|
| Logs | Chuyện gì đã xảy ra? |
| Metrics | Hệ thống đang tốt hay xấu theo số liệu? |
| Traces | Request đi qua bước nào và chậm/lỗi ở đâu? |

## Monitoring checklist

- [ ] Có request id.
- [ ] Có latency từng bước.
- [ ] Có error rate.
- [ ] Có token/cost.
- [ ] Có retrieval quality.
- [ ] Có evaluation dataset.
- [ ] Có dashboard.
- [ ] Có alert.
- [ ] Có rollback plan.

## 30 câu hỏi ôn thi

1. Monitoring là gì?
2. Observability là gì?
3. Logs dùng để làm gì?
4. Metrics dùng để làm gì?
5. Traces dùng để làm gì?
6. Span là gì?
7. Latency là gì?
8. Throughput là gì?
9. Error rate tính như thế nào?
10. Token usage quan trọng vì sao?
11. Cost tracking giúp gì?
12. Retrieval quality đo gì?
13. Hallucination check là gì?
14. LLM-as-judge là gì?
15. Human feedback dùng để làm gì?
16. Dashboard nên có chỉ số nào?
17. Alert nên kích hoạt khi nào?
18. Incident response gồm bước nào?
19. Rollback là gì?
20. Vì sao cần version prompt?
21. Vì sao cần version model?
22. Vì sao cần version data?
23. Secrets management là gì?
24. Environment variables dùng để làm gì?
25. Rate limit giúp gì?
26. Cache có lợi và rủi ro gì?
27. Fallback model dùng khi nào?
28. Audit log ghi gì?
29. CI/CD trong AI app cần thêm gì?
30. Vì sao không nên log dữ liệu nhạy cảm?

## 10 case questions

1. Latency tăng gấp đôi sau deploy. Bạn kiểm tra gì trước?
2. Cost tăng mạnh nhưng request count không tăng. Nguyên nhân có thể là gì?
3. User báo chatbot bịa. Cần xem log nào?
4. Retrieval empty rate tăng. Cần kiểm tra gì?
5. Model provider lỗi timeout. Ops nên làm gì?
6. Prompt mới làm chất lượng giảm. Cần rollback gì?
7. Không có request id trong log gây khó khăn gì?
8. Dashboard chỉ có CPU/RAM, thiếu metric LLM. Thiếu gì?
9. Evaluation score giảm sau khi ingest tài liệu mới. Cần kiểm tra gì?
10. Alert quá nhạy gây spam. Cần điều chỉnh gì?
