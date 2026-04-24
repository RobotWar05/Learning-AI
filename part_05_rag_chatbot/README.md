# Phần 5: RAG và Chatbot

## Mục tiêu

Hiểu chatbot là gì, RAG là gì, vì sao cần RAG, cách thiết kế kiến trúc chatbot và cách đánh giá chất lượng câu trả lời.

## Chatbot thường là gì

Chatbot là hệ thống nhận câu hỏi/ngữ cảnh từ người dùng và trả lời bằng text hoặc hành động. Chatbot đơn giản có thể chỉ gọi LLM trực tiếp, nhưng chatbot dùng dữ liệu riêng thường cần retrieval, logging và evaluation.

## RAG là gì

RAG là Retrieval-Augmented Generation: trước khi model trả lời, hệ thống truy xuất tài liệu liên quan rồi đưa vào prompt làm ngữ cảnh.

## Vì sao cần RAG

- Giảm phụ thuộc vào kiến thức nội tại của model.
- Cho phép trả lời dựa trên dữ liệu riêng.
- Có thể trích nguồn để kiểm chứng.
- Giảm hallucination nếu retrieval và prompt được thiết kế tốt.

## Chatbot thường vs Chatbot RAG vs Agent chatbot

| Loại | Đặc điểm | Rủi ro |
|---|---|---|
| Chatbot thường | Gọi LLM trực tiếp | Dễ trả lời sai dữ liệu riêng |
| Chatbot RAG | Truy xuất tài liệu rồi trả lời | Sai nếu retrieval sai |
| Agent chatbot | Có thể gọi tool và lập kế hoạch | Cần monitoring và kiểm soát tool |

## RAG pipeline

```text
document -> chunk -> embedding -> vector store -> query -> retrieve -> prompt -> LLM -> answer
```

## Chatbot architecture

- Frontend/API nhận câu hỏi.
- Backend quản lý request/session.
- Retriever lấy context.
- Prompt builder tạo prompt.
- LLM sinh câu trả lời.
- Logger/evaluator ghi nhận chất lượng.

## Evaluation

Cần đánh giá:

- Câu trả lời có đúng không?
- Có dùng đúng nguồn không?
- Có bịa không?
- Latency có chấp nhận được không?
- Người dùng có hài lòng không?

## File trong phần này

- [Checklist](./00_checklist.md)
- [RAG pipeline notes](./01_rag_pipeline_notes.md)
- [Chatbot design notes](./02_chatbot_design_notes.md)
- [Template RAG/chatbot](./03_rag_chatbot_code_templates.py)
- [Giải thích template RAG/chatbot](./03_rag_chatbot_code_templates.md)
- [Bài tập](./04_exercises.md)
- [Ôn nhanh](./05_quick_review.md)

## Thứ tự học

1. Học RAG pipeline.
2. Học chunking, retrieval, prompt construction.
3. Học kiến trúc chatbot.
4. Đọc code template RAG đơn giản.
5. Làm bài tập thiết kế chatbot học AI.
