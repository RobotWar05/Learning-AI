# Ghi chú pipeline RAG

## 1. RAG nghĩa là gì

RAG là Retrieval-Augmented Generation. Hệ thống không chỉ hỏi LLM trực tiếp, mà trước tiên tìm tài liệu liên quan để làm context cho câu trả lời.

## 2. Pipeline từng bước

```text
document -> chunk -> embedding -> vector store -> query -> retrieve -> prompt -> LLM -> answer
```

1. Document: tài liệu nguồn như PDF, Markdown, web page.
2. Chunk: chia tài liệu thành đoạn nhỏ.
3. Embedding: biến text thành vector số.
4. Vector store: lưu vector và metadata.
5. Query: câu hỏi của người dùng.
6. Retrieve: tìm chunk liên quan.
7. Prompt: ghép câu hỏi và context.
8. LLM: sinh câu trả lời.
9. Answer: trả lời, lý tưởng là có trích nguồn.

## 3. Chunk size

Chunk quá dài làm retrieval kém chính xác và tốn context window. Chunk quá ngắn dễ mất ý nghĩa. Cần chọn theo loại tài liệu.

## 4. Overlap

Overlap là phần chồng giữa các chunk liên tiếp. Nó giúp giảm mất ngữ cảnh ở ranh giới chunk.

## 5. Embeddings

Embedding biểu diễn ý nghĩa text bằng vector. Text có nghĩa gần nhau thường có vector gần nhau.

## 6. Cosine similarity

Cosine similarity đo mức gần nhau về hướng giữa hai vector. Trong RAG, thường dùng để tìm chunk liên quan đến query.

## 7. Vector database

Vector database lưu embedding, text gốc và metadata như source, page, section. Ví dụ thực tế: FAISS, Chroma, Pinecone, Weaviate.

## 8. Retrieval quality

Retrieval tốt nghĩa là lấy đúng đoạn chứa thông tin cần trả lời. Nếu retrieval sai, LLM có thể trả lời sai dù prompt viết tốt.

## 9. Context window

Context window là giới hạn lượng token model có thể nhận. Không thể nhét toàn bộ tài liệu vào prompt nếu quá dài.

## 10. Citations

Citation giúp người dùng kiểm chứng câu trả lời. Chatbot học tập nên trả lời kèm nguồn hoặc đoạn tài liệu liên quan.

## 11. Hallucination

Hallucination là khi model tạo thông tin không có trong dữ liệu hoặc không đúng sự thật. RAG giảm rủi ro này nhưng không loại bỏ hoàn toàn.

## 12. Khi RAG thất bại

- Chunking không hợp lý.
- Embedding không phù hợp ngôn ngữ/domain.
- Retrieval lấy sai context.
- Prompt không ép model bám nguồn.
- Tài liệu nguồn thiếu hoặc lỗi thời.

## 13. Cách cải thiện RAG

- Làm sạch tài liệu.
- Chọn chunk size/overlap tốt hơn.
- Dùng metadata filtering.
- Dùng reranker.
- Yêu cầu trả lời kèm nguồn.
- Tạo bộ câu hỏi evaluation.
