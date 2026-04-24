# AI Study Roadmap Report

## 1. Goal of the task

Tạo cấu trúc ban đầu cho repository học AI bằng tiếng Việt, phục vụ ôn thi cấp tốc các mảng:

- Python Core.
- NumPy và Pandas.
- Machine Learning.
- Deep Learning.
- RAG và Chatbot.
- Agent Monitoring và Ops.

Yêu cầu chính là tạo roadmap có thể học ngay, trong đó `part_01_python_core` được triển khai chi tiết hơn các phần còn lại.

## 2. File/folder tree created

```text
Learning-AI/
├── README.md
├── learning_plan.md
├── progress_tracker.md
├── resources.md
├── AI_STUDY_ROADMAP_REPORT.md
│
├── part_01_python_core/
│   ├── README.md
│   ├── 00_checklist.md
│   ├── 01_must_memorize_code.py
│   ├── 02_exercises.md
│   ├── 03_notes.md
│   └── 04_quick_review.md
│
├── part_02_numpy_pandas/
│   ├── README.md
│   ├── 00_checklist.md
│   ├── 01_must_memorize_code.py
│   ├── 02_exercises.md
│   └── 03_notes.md
│
├── part_03_machine_learning/
│   ├── README.md
│   ├── 00_checklist.md
│   ├── 01_theory_notes.md
│   ├── 02_sklearn_code_templates.py
│   ├── 03_exercises.md
│   └── 04_quick_review.md
│
├── part_04_deep_learning/
│   ├── README.md
│   ├── 00_checklist.md
│   ├── 01_theory_notes.md
│   ├── 02_pytorch_basic_templates.py
│   ├── 03_exercises.md
│   └── 04_quick_review.md
│
├── part_05_rag_chatbot/
│   ├── README.md
│   ├── 00_checklist.md
│   ├── 01_rag_pipeline_notes.md
│   ├── 02_chatbot_design_notes.md
│   ├── 03_exercises.md
│   └── 04_quick_review.md
│
└── part_06_agent_monitoring_ops/
    ├── README.md
    ├── 00_checklist.md
    ├── 01_monitoring_notes.md
    ├── 02_ops_architecture_notes.md
    ├── 03_exercises.md
    └── 04_quick_review.md
```

## 3. Summary of each important file

| File | Tóm tắt |
|---|---|
| `README.md` | Giới thiệu mục tiêu repo, bảng 6 phần học, cấu trúc thư mục, cách học và luật học. |
| `learning_plan.md` | Kế hoạch học cấp tốc theo phần, mục tiêu, thời lượng gợi ý và ghi chú ưu tiên. |
| `progress_tracker.md` | Bảng tick tiến độ đọc, gõ code, làm bài tập và ôn lại. |
| `resources.md` | Danh sách link học Python, NumPy/Pandas, ML, DL, RAG/chatbot và monitoring/ops. |
| `part_01_python_core/README.md` | Hướng dẫn học Python nền tảng, dạng bài thi hay gặp và thứ tự học. |
| `part_01_python_core/00_checklist.md` | Checklist chi tiết cho cú pháp, vòng lặp, data structure, string, function, file/exception và bài gần AI. |
| `part_01_python_core/01_must_memorize_code.py` | Code Python chạy được, không dùng thư viện ngoài, gồm 23 nhóm ví dụ bắt buộc. |
| `part_01_python_core/02_exercises.md` | Bài tập Python chia theo nhóm, có bài gần AI/ML như đếm label, tỷ lệ label, train/test split, min-max normalize. |
| `part_01_python_core/03_notes.md` | Ghi chú lỗi thường gặp với ví dụ sai/đúng. |
| `part_01_python_core/04_quick_review.md` | Bảng cú pháp, hàm built-in, method thường dùng, 20 câu hỏi ôn và 10 câu hỏi dự đoán output. |
| `part_02_numpy_pandas/*` | Khung học NumPy/Pandas có checklist, bài tập và ghi chú không rỗng. |
| `part_03_machine_learning/*` | Khung học Machine Learning có lý thuyết, template pipeline scikit-learn và quick review. |
| `part_04_deep_learning/*` | Khung học Deep Learning có ghi chú neural network và template training loop. |
| `part_05_rag_chatbot/*` | Khung học RAG/chatbot có pipeline RAG và ghi chú thiết kế chatbot. |
| `part_06_agent_monitoring_ops/*` | Khung học monitoring/ops có logs, metrics, traces, evaluation và kiến trúc vận hành. |

## 4. Quality checklist

- [x] Nội dung Markdown học tập viết bằng tiếng Việt.
- [x] Không tạo folder bọc ngoài như `AI_Study_Roadmap`.
- [x] Không push remote.
- [x] Không xóa file không cần thiết.
- [x] Root `README.md` có bảng 6 phần đúng yêu cầu.
- [x] Có `learning_plan.md`, `progress_tracker.md`, `resources.md`.
- [x] `part_01_python_core` được triển khai chi tiết.
- [x] Các phần 2-6 có đủ file yêu cầu và nội dung placeholder không rỗng.
- [x] Code Python Part 1 không dùng external libraries.
- [x] Ví dụ input và đọc/ghi file được comment để tránh block hoặc tạo file phụ.

## 5. Result of running `python part_01_python_core/01_must_memorize_code.py`

Trong môi trường này, lệnh `python` đang trỏ tới:

```text
C:\Windows\system32\python
```

Kết quả khi chạy đúng lệnh yêu cầu:

```text
Command: python part_01_python_core/01_must_memorize_code.py
Exit code: 0
Stdout: empty
```

Để kiểm chứng script bằng Python thật trên máy, đã chạy:

```text
Command: py part_01_python_core/01_must_memorize_code.py
Exit code: 0
```

Kết quả chính:

```text
Tong 1..10 = 55
5! = 120
List sau khi sua: [10, 30, 40, 50]
Mean: 32.5
{'positive': 3, 'negative': 1, 'neutral': 1}
[0.0, 0.25, 0.5, 0.75, 1.0]
Train: [1, 2, 3, 4, 5, 6, 7, 8]
Test: [9, 10]
So luong tung label: {'positive': 2, 'negative': 2}
```

Ghi chú kỹ thuật: file đã được cấu hình `sys.stdout.reconfigure(encoding="utf-8")` để tránh lỗi Unicode khi in tiếng Việt trên Windows console.

## 6. Result of `git status`

Kết quả sau khi tạo đầy đủ file:

```text
 M README.md
?? AI_STUDY_ROADMAP_REPORT.md
?? learning_plan.md
?? part_01_python_core/
?? part_02_numpy_pandas/
?? part_03_machine_learning/
?? part_04_deep_learning/
?? part_05_rag_chatbot/
?? part_06_agent_monitoring_ops/
?? progress_tracker.md
?? resources.md
```

## 7. Suggested commit message

```text
init AI learning roadmap structure and Python core module
```
