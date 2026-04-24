# Bài tập Agent Monitoring/Ops

## Xác định cần log gì

1. Với chatbot RAG, liệt kê 10 field nên log.
2. Field nào không nên log vì nhạy cảm?
3. Vì sao request id quan trọng?

## Định nghĩa metrics

1. Định nghĩa latency trung bình.
2. Định nghĩa error rate.
3. Định nghĩa cost/request.
4. Định nghĩa retrieval hit rate.
5. Định nghĩa user negative feedback rate.

## Thiết kế dashboard

Dashboard cần có:

- Request count.
- Average latency và P95 latency.
- Error rate.
- Token usage.
- Cost.
- Retrieval empty rate.
- Evaluation score.
- User feedback.

## Incident response checklist

1. Xác định incident bắt đầu lúc nào.
2. Kiểm tra deploy gần nhất.
3. Kiểm tra logs/traces.
4. Kiểm tra model provider.
5. Rollback nếu cần.
6. Ghi nguyên nhân gốc.
7. Thêm test/evaluation để tránh lặp lại.

## Đánh giá câu trả lời xấu

Cho câu trả lời chatbot sai:

1. Kiểm tra retrieved context.
2. Kiểm tra prompt.
3. Kiểm tra model output.
4. Kiểm tra source/citation.
5. Ghi vào evaluation dataset.

## Tính average latency

Cho latency `[1000, 1200, 800, 2000]` ms:

1. Tính average latency.
2. Nếu ngưỡng alert là 1500 ms, có alert không?

## Detect high error rate

Trong 100 request có 8 request lỗi:

1. Error rate là bao nhiêu?
2. Nếu ngưỡng là 5%, có alert không?

## Đề xuất alert rules

Viết 5 rule alert cho chatbot RAG production.
