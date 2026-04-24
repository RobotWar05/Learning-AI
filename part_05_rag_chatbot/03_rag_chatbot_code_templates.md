# Giải thích template RAG/chatbot

## 1. Mục tiêu file code

File `03_rag_chatbot_code_templates.py` minh họa pipeline RAG bằng standard library, không dùng embedding thật hoặc vector database thật. Mục tiêu là hiểu luồng dữ liệu trước khi học tool.

## 2. Document là gì

```python
DOCUMENTS = [{"id": "python", "text": "..."}]
```

Document là tài liệu nguồn. Trong hệ thống thật, document có thể là PDF, Markdown, trang web hoặc record trong database.

## 3. Chunk là gì

```python
simple_chunk(document, max_words=12)
```

Chunk là đoạn nhỏ được cắt từ document. Chunk giúp retrieval chính xác hơn và vừa context window.

## 4. Retrieval là gì

```python
retrieve(query, chunks, top_k=2)
```

Retrieval là bước tìm chunk liên quan đến câu hỏi. Code mẫu dùng keyword overlap. Hệ thống thật thường dùng embedding và vector search.

## 5. Prompt construction

```python
build_prompt(query, retrieved_chunks)
```

Prompt construction là ghép context, câu hỏi và quy tắc trả lời thành input cho LLM.

## 6. Mock LLM

```python
mock_llm(prompt)
```

Mock LLM giúp file chạy được mà không cần API. Trong hệ thống thật, hàm này được thay bằng lời gọi model.

## 7. Embedding/vector DB thật thay thế gì

Trong hệ thống thật:

- `tokenize` và keyword overlap được thay bằng embedding model.
- List `chunks` được thay bằng vector database.
- `retrieve` dùng cosine similarity hoặc ANN search.
- Có thể thêm reranker để sắp xếp lại kết quả.

## 8. Common mistakes

- Chunk quá dài hoặc quá ngắn.
- Không lưu source nên không trích dẫn được.
- Prompt không yêu cầu model bám context.
- Retrieval trả context sai nhưng vẫn tin câu trả lời.
- Không có evaluation dataset.
- Không có fallback khi không tìm thấy context.

## 9. Mini exercises

1. Thêm document mới về Deep Learning.
2. Đổi `top_k` từ 2 thành 1 và quan sát context.
3. Thêm rule trong prompt: nếu không có source thì không trả lời.
4. Viết evaluation kiểm tra answer có chứa chữ `source`.
5. Thay keyword retrieval bằng tính điểm số từ chung theo tỷ lệ.
