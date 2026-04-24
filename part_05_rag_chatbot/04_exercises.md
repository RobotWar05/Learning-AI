# Bài tập RAG và Chatbot

## Thiết kế chatbot học AI

1. Xác định user chính của chatbot.
2. Liệt kê 5 loại câu hỏi chatbot cần trả lời.
3. Xác định dữ liệu nguồn trong repo.
4. Viết fallback response khi không đủ dữ kiện.

## RAG cho PDF bài giảng

1. Mô tả pipeline ingest PDF.
2. Chọn chunk size giả định và giải thích.
3. Có nên dùng overlap không? Vì sao?
4. Metadata nào cần lưu cho mỗi chunk?

## Chunk size

1. Chunk quá dài gây vấn đề gì?
2. Chunk quá ngắn gây vấn đề gì?
3. Khi tài liệu có nhiều bảng, cần lưu ý gì?

## Hallucination risk

1. Nêu 3 nguyên nhân chatbot RAG vẫn trả lời sai.
2. Viết rule prompt để giảm bịa.
3. Thiết kế câu trả lời khi context không đủ.

## Prompt rules

Viết prompt rule gồm:

- Chỉ trả lời dựa trên context.
- Nếu không biết thì nói không đủ dữ kiện.
- Trả lời ngắn gọn.
- Nêu source nếu có.

## Architecture text diagram

Vẽ kiến trúc dạng text:

```text
User -> Frontend -> Backend -> Retriever -> Vector DB
                           -> LLM
                           -> Logs/Evaluation
```

## Evaluate answer quality

1. Tạo 5 câu hỏi test.
2. Viết expected answer ngắn.
3. Chấm câu trả lời theo 3 mức: đúng, thiếu, sai.
4. Ghi lỗi retrieval nếu context không liên quan.
