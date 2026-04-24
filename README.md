# Learning-AI

Repository này dùng để học cấp tốc các kiến thức nền tảng phục vụ kỳ thi AI, bao gồm Python, xử lý dữ liệu, Machine Learning, Deep Learning, RAG, chatbot và tư duy monitoring/ops cho hệ thống AI.

Mục tiêu không phải học thuộc lòng rời rạc, mà là xây được bản đồ kiến thức đủ rõ để:

- Đọc hiểu câu hỏi lý thuyết AI/ML/DL.
- Viết được các đoạn code Python cơ bản trong bài thi.
- Hiểu quy trình xử lý dữ liệu, huấn luyện mô hình và đánh giá kết quả.
- Nắm được tư duy thiết kế chatbot/RAG và cách quan sát hệ thống AI khi vận hành.

## Tổng quan lộ trình

| Phần | Tên phần | Mục tiêu | Trạng thái |
|---|---|---|---|
| Phần 1 | Python nền tảng | Đọc hiểu và viết code Python cơ bản phục vụ AI | Đang triển khai |
| Phần 2 | NumPy và Pandas | Xử lý dữ liệu dạng mảng và bảng | Khung |
| Phần 3 | Machine Learning | Hiểu thuật toán ML và code scikit-learn | Khung |
| Phần 4 | Deep Learning | Hiểu neural network, loss, optimizer, PyTorch cơ bản | Khung |
| Phần 5 | RAG và Chatbot | Hiểu pipeline RAG và thiết kế chatbot | Khung |
| Phần 6 | Agent Monitoring/Ops | Hiểu logs, metrics, traces, evaluation, deployment mindset | Khung |

## Cấu trúc repository

```text
Learning-AI/
├── README.md
├── learning_plan.md
├── progress_tracker.md
├── resources.md
├── AI_STUDY_ROADMAP_REPORT.md
├── part_01_python_core/
├── part_02_numpy_pandas/
├── part_03_machine_learning/
├── part_04_deep_learning/
├── part_05_rag_chatbot/
└── part_06_agent_monitoring_ops/
```

## Cách học từng phần

1. Đọc `README.md` trong từng phần để biết mục tiêu và thứ tự học.
2. Mở `00_checklist.md` để đánh dấu kiến thức bắt buộc.
3. Gõ lại code mẫu, không chỉ đọc.
4. Làm bài tập trong file `exercises`.
5. Dùng file `quick_review` để ôn nhanh trước kỳ thi.
6. Cập nhật tiến độ trong [progress_tracker.md](progress_tracker.md).

## Luật học

- Ưu tiên hiểu bản chất trước khi học thuộc cú pháp.
- Với code Python, phải tự gõ lại tối thiểu một lần.
- Với thuật toán ML/DL, luôn trả lời được: input là gì, output là gì, loss/metric là gì.
- Không nhảy sang RAG/chatbot nếu chưa nắm Python, dữ liệu bảng và khái niệm model cơ bản.
- Mỗi ngày nên có một vòng: đọc lý thuyết, gõ code, làm bài tập, tự kiểm tra.

## File điều hướng

- [learning_plan.md](learning_plan.md): kế hoạch học cấp tốc theo từng phần.
- [progress_tracker.md](progress_tracker.md): bảng theo dõi tiến độ học.
- [resources.md](resources.md): tài nguyên học chính thống và gợi ý luyện tập.
