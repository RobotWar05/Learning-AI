# Ôn nhanh RAG và Chatbot

## Bảng thuật ngữ RAG

| Thuật ngữ | Ý nghĩa |
|---|---|
| Document | Tài liệu nguồn |
| Chunk | Đoạn nhỏ của tài liệu |
| Embedding | Vector biểu diễn ý nghĩa text |
| Vector database | Nơi lưu và tìm vector |
| Retrieval | Tìm context liên quan |
| Reranking | Sắp xếp lại kết quả retrieval |
| Prompt | Input gửi cho LLM |
| Context window | Giới hạn token model nhận |
| Citation | Trích nguồn |
| Hallucination | Model bịa hoặc nói sai |

## Bảng kiến trúc chatbot

| Thành phần | Vai trò |
|---|---|
| Frontend | Nhận câu hỏi và hiển thị trả lời |
| Backend | Điều phối request |
| Retriever | Tìm context |
| Vector DB | Lưu embedding |
| LLM | Sinh câu trả lời |
| Logger | Ghi request/output |
| Evaluator | Chấm chất lượng |

## 30 câu hỏi ôn thi

1. RAG là gì?
2. Vì sao cần RAG?
3. Chatbot thường khác chatbot RAG ở đâu?
4. Agent chatbot khác chatbot RAG ở đâu?
5. Document loading là gì?
6. Chunking là gì?
7. Chunk size ảnh hưởng gì?
8. Overlap dùng để làm gì?
9. Embedding là gì?
10. Vector database lưu gì?
11. Retrieval là gì?
12. Reranking là gì?
13. Cosine similarity dùng để làm gì?
14. Prompt construction gồm gì?
15. Context window là gì?
16. Citation có ích gì?
17. Hallucination là gì?
18. RAG có loại bỏ hoàn toàn hallucination không?
19. Khi retrieval sai thì chuyện gì xảy ra?
20. Metadata nên lưu gì?
21. Conversation memory dùng để làm gì?
22. Tool calling là gì?
23. Fallback response nên viết thế nào?
24. Evaluation dataset là gì?
25. User feedback dùng để làm gì?
26. Vì sao cần logging chatbot?
27. Rate limiting dùng để làm gì?
28. LLM provider cần cân nhắc gì?
29. Chatbot học tập nên trích nguồn không?
30. Khi nào không nên dùng RAG?

## 10 case questions

1. Chatbot trả lời đúng văn phong nhưng sai nguồn. Lỗi có thể nằm ở đâu?
2. Retrieval không lấy được chunk liên quan. Cần kiểm tra gì?
3. Tài liệu dài hơn context window. Cần làm gì?
4. User hỏi ngoài phạm vi dữ liệu. Chatbot nên trả lời thế nào?
5. Chunk chứa nửa định nghĩa, nửa còn lại ở chunk sau. Cần cải thiện gì?
6. Câu trả lời không có citation. Rủi ro gì?
7. Chatbot dùng dữ liệu cũ. Cần quản lý gì?
8. Query tiếng Việt nhưng embedding kém tiếng Việt. Hậu quả gì?
9. Agent gọi nhầm tool. Cần monitoring gì?
10. Làm sao tạo bộ câu hỏi evaluation cho chatbot học AI?
