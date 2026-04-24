# Ghi chú thiết kế chatbot

## Kiến trúc tối thiểu

- UI hoặc API nhận câu hỏi.
- Backend xử lý session.
- Retriever lấy tài liệu liên quan.
- LLM sinh câu trả lời.
- Logging lưu câu hỏi, context, output, latency.

## Câu hỏi thiết kế cần trả lời

- Chatbot dùng cho ai?
- Dữ liệu nguồn là gì?
- Cần trả lời có trích nguồn không?
- Có cần lưu lịch sử hội thoại không?
- Khi không biết, chatbot phải phản hồi thế nào?
