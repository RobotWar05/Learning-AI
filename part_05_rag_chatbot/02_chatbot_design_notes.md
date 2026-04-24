# Ghi chú thiết kế chatbot

## 1. Requirement analysis

Trước khi xây chatbot, cần trả lời:

- Người dùng là ai?
- Họ hỏi loại câu hỏi nào?
- Dữ liệu nguồn ở đâu?
- Chatbot có được trả lời ngoài phạm vi không?
- Có cần trích nguồn không?

## 2. Target users

Ví dụ repo này hướng tới người học AI để ôn thi. Chatbot nên trả lời ngắn, đúng trọng tâm, có thể chỉ tới file học liên quan.

## 3. Scope of chatbot

Scope phải rõ. Nếu chatbot chỉ hỗ trợ nội dung trong repo, khi câu hỏi ngoài repo phải nói không đủ dữ kiện.

## 4. Data source

Dữ liệu có thể là Markdown trong repo, PDF bài giảng, note cá nhân hoặc link tài liệu. Cần version dữ liệu để biết câu trả lời dựa trên bản nào.

## 5. Frontend

Frontend có thể là web chat, CLI hoặc tích hợp trong app học tập. Nhiệm vụ chính là nhập câu hỏi, hiển thị câu trả lời, nguồn và feedback.

## 6. Backend

Backend nhận request, gọi retriever, xây prompt, gọi LLM, ghi log và trả response.

## 7. Database và vector database

- Database thường: lưu user, session, feedback.
- Vector database: lưu chunk embedding để retrieval.

## 8. LLM provider

LLM provider có thể là API ngoài hoặc model tự host. Cần cân nhắc cost, latency, privacy và chất lượng tiếng Việt.

## 9. Prompt design

Prompt nên có:

- Vai trò của chatbot.
- Context retrieved.
- Câu hỏi user.
- Quy tắc không bịa.
- Yêu cầu trích nguồn nếu có.

## 10. Conversation memory

Memory giúp chatbot hiểu hội thoại nhiều lượt, nhưng không nên đưa toàn bộ lịch sử nếu quá dài. Cần tóm tắt hoặc chọn lọc.

## 11. Authentication và rate limiting

Nếu triển khai thật, cần kiểm soát người dùng và giới hạn request để tránh lạm dụng chi phí.

## 12. Logging

Cần log request id, câu hỏi, context, output, latency, lỗi và feedback. Không nên log dữ liệu nhạy cảm không cần thiết.

## 13. Fallback response

Khi không đủ dữ kiện, chatbot phải nói rõ không đủ thông tin thay vì đoán.

## 14. User feedback

Feedback giúp phát hiện câu trả lời sai và tạo dataset evaluation.

## 15. Deployment architecture

```text
User -> Frontend -> API Backend -> Retriever -> Vector DB
                              -> LLM Provider
                              -> Logs/Evaluation
```
