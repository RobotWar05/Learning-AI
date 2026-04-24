# Ghi chú pipeline RAG

## Pipeline cơ bản

1. Thu thập tài liệu.
2. Chia tài liệu thành chunk.
3. Tạo embedding cho từng chunk.
4. Lưu embedding vào vector database.
5. Khi có câu hỏi, tạo embedding cho câu hỏi.
6. Tìm chunk liên quan.
7. Đưa context vào prompt.
8. Model sinh câu trả lời.

## Điểm cần kiểm soát

- Chunk quá dài làm retrieval kém chính xác.
- Chunk quá ngắn có thể mất ngữ cảnh.
- Context sai dẫn tới trả lời sai.
- Cần lưu source để truy vết câu trả lời.
