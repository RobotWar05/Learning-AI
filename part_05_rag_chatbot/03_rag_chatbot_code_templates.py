"""Template giáo dục RAG/chatbot đơn giản, chỉ dùng standard library."""

import sys
from collections import Counter


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


DOCUMENTS = [
    {
        "id": "python",
        "text": "Python co list, dict, function, try except va duoc dung nhieu trong AI.",
    },
    {
        "id": "ml",
        "text": "Machine Learning hoc quy luat tu du lieu. Can tach train test va danh gia bang metric.",
    },
    {
        "id": "rag",
        "text": "RAG gom document, chunk, retrieval, prompt va LLM de tra loi dua tren tai lieu.",
    },
]


def simple_chunk(document, max_words=12):
    """Chia document thành các chunk nhỏ theo số từ."""
    words = document["text"].split()
    chunks = []
    for start in range(0, len(words), max_words):
        chunk_words = words[start : start + max_words]
        chunks.append(
            {
                "source": document["id"],
                "text": " ".join(chunk_words),
            }
        )
    return chunks


def build_chunks(documents):
    """Tạo danh sách chunk từ nhiều document."""
    all_chunks = []
    for document in documents:
        all_chunks.extend(simple_chunk(document))
    return all_chunks


def tokenize(text):
    """Tokenize rất đơn giản để minh họa keyword retrieval."""
    return [word.strip(".,!?").lower() for word in text.split()]


def retrieve(query, chunks, top_k=2):
    """Tìm chunk liên quan bằng số keyword trùng nhau."""
    query_terms = Counter(tokenize(query))
    scored = []
    for chunk in chunks:
        chunk_terms = Counter(tokenize(chunk["text"]))
        score = sum((query_terms & chunk_terms).values())
        scored.append((score, chunk))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [chunk for score, chunk in scored[:top_k] if score > 0]


def build_prompt(query, retrieved_chunks):
    """Ghép context và câu hỏi thành prompt."""
    context_lines = [
        f"- Source {chunk['source']}: {chunk['text']}" for chunk in retrieved_chunks
    ]
    context = "\n".join(context_lines) if context_lines else "Khong co context phu hop."
    return (
        "Ban la chatbot hoc AI. Chi tra loi dua tren context.\n"
        f"Context:\n{context}\n"
        f"Cau hoi: {query}\n"
        "Tra loi ngan gon va neu source neu co."
    )


def mock_llm(prompt):
    """Mock LLM để file chạy được mà không cần API."""
    if "Khong co context phu hop" in prompt:
        return "Toi chua du du kien tu tai lieu de tra loi."
    return "Cau tra loi mau: hay dua vao context da retrieve va kem source."


def answer_question(query):
    chunks = build_chunks(DOCUMENTS)
    retrieved = retrieve(query, chunks)
    prompt = build_prompt(query, retrieved)
    answer = mock_llm(prompt)
    return {
        "query": query,
        "retrieved": retrieved,
        "prompt": prompt,
        "answer": answer,
    }


def evaluate_answer(result):
    """Evaluation đơn giản: kiểm tra có retrieved context không."""
    return {
        "has_context": len(result["retrieved"]) > 0,
        "answer_length": len(result["answer"].split()),
    }


if __name__ == "__main__":
    sample_query = "RAG gom nhung buoc nao?"
    result = answer_question(sample_query)
    print("Query:", result["query"])
    print("Retrieved:", result["retrieved"])
    print("Prompt:\n", result["prompt"])
    print("Answer:", result["answer"])
    print("Evaluation:", evaluate_answer(result))

    print("\nChatbot loop example - đang comment để tránh chờ nhập:")
    # while True:
    #     user_query = input("User: ")
    #     if user_query.lower() in {"exit", "quit"}:
    #         break
    #     print(answer_question(user_query)["answer"])
