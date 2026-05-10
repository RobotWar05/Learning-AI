# BẢN ÔN CỨU ĐIỂM TRƯỚC THI AI

## 1. Các câu phải nhớ nguyên văn

### RAG là gì?

**Câu chuẩn đi thi:**

RAG là Retrieval-Augmented Generation, tức là phương pháp kết hợp truy xuất tài liệu và sinh câu trả lời. Hệ thống chia tài liệu thành chunk, tạo embedding, lưu vào vector database. Khi người dùng hỏi, hệ thống truy xuất các chunk liên quan rồi đưa vào prompt để LLM trả lời dựa trên dữ liệu đó.

**Tránh nói:**

- "RAG train tài liệu"
- "Chunk đã train"
- "RAG đảm bảo luôn đúng"

**Keyword bắt buộc:**

`chunking`, `embedding`, `vector database`, `retrieval`, `prompt`, `LLM`, `context`.

### Vì sao RAG giúp giảm hallucination?

**Câu chuẩn đi thi:**

RAG giúp giảm hallucination vì LLM không chỉ dựa vào kiến thức nội tại, mà được cung cấp context từ tài liệu đã truy xuất. Nếu retrieval lấy đúng tài liệu và prompt yêu cầu model bám theo context, câu trả lời sẽ có căn cứ hơn.

**Ý cuối rất quan trọng:**

> RAG giảm rủi ro hallucination, nhưng không đảm bảo đúng tuyệt đối.

Vì:

- Retrieval có thể lấy sai chunk.
- Tài liệu nguồn có thể thiếu hoặc sai.
- LLM vẫn có thể diễn giải sai context.

### Embedding là gì?

Embedding là quá trình biến văn bản, câu hỏi hoặc chunk tài liệu thành vector số biểu diễn ngữ nghĩa. Các đoạn có ý nghĩa gần nhau sẽ có vector gần nhau trong không gian embedding.

**Keyword:**

`vector số`, `biểu diễn ngữ nghĩa`, `semantic similarity`.

### Vector database dùng để làm gì?

Vector database dùng để lưu embedding của các chunk tài liệu kèm nội dung và metadata. Khi có câu hỏi, hệ thống tạo embedding cho câu hỏi rồi tìm các vector/chunk gần nhất theo độ tương đồng, ví dụ cosine similarity.

**Keyword:**

`embedding`, `metadata`, `similarity search`, `cosine similarity`, `source`.

### Guardrails là gì?

Guardrails là các cơ chế kiểm soát hành vi của chatbot/AI system để hệ thống trả lời trong phạm vi cho phép, không bịa, không lộ dữ liệu nhạy cảm, không đưa lời khuyên nguy hiểm và biết từ chối khi không đủ thông tin.

**Ví dụ guardrails:**

- Chỉ trả lời dựa trên context.
- Không trả lời ngoài phạm vi.
- Chặn prompt injection.
- Lọc input/output.
- Human-in-the-loop cho tác vụ rủi ro.

### Monitoring là gì?

Monitoring trong hệ thống AI là quá trình theo dõi chất lượng, hiệu năng, chi phí và độ an toàn sau khi triển khai.

**Cần monitor:**

`input`, `output`, `retrieved context`, `correctness`, `hallucination rate`, `retrieval quality`, `latency`, `token cost`, `tool error`, `user feedback`.

### AI agent khác chatbot thường ở đâu?

Chatbot thường chủ yếu nhận câu hỏi và sinh câu trả lời. AI agent phức tạp hơn vì có thể hiểu mục tiêu, lập kế hoạch nhiều bước, gọi công cụ/API, quan sát kết quả, điều chỉnh hành động và hoàn thành nhiệm vụ.

**Keyword:**

`LLM`, `planner`, `memory`, `tools`, `executor`, `safety layer`, `monitoring`.

## 2. Các lỗi vừa mắc và câu sửa đúng

| Lỗi dễ mất điểm | Cách nói đúng |
|---|---|
| "RAG train tài liệu" | RAG không nhất thiết train lại model; RAG lập chỉ mục tài liệu bằng chunking, embedding, vector DB rồi retrieval |
| "Validation dùng để đánh giá cuối cùng" | Train để học, validation để chọn model/hyperparameter, test để chấm cuối |
| Nhầm confusion matrix | Confusion matrix gồm TP, FP, FN, TN |
| Transformer dùng K-means | Transformer nổi bật nhờ attention/self-attention |
| Ảnh dùng Linear Regression | Ảnh thường dùng CNN |
| `range(1,5)` lấy cả 5 | Sai. `range(1,5)` là 1, 2, 3, 4 |
| `arr[1:4]` lấy index 1 đến 4 | Sai. Lấy index 1, 2, 3 |
| `arr > 20` và `arr[arr > 20]` | `arr > 20` là mask; `arr[arr > 20]` là dữ liệu đã lọc |
| `df.head()` | Xem vài dòng đầu |
| `df.info()` | Xem kiểu dữ liệu và non-null |
| `df.describe()` | Thống kê mean/std/min/max |
| `df.shape` | Số dòng, số cột |
| `df.columns` | Tên các cột |
| `df.isnull().sum()` | Đếm missing values từng cột |
| `df["label"].value_counts()` | Đếm tần suất từng giá trị |

## 3. Ba bài tự luận mẫu

### Bài 1: Thiết kế chatbot AI hoặc RAG chatbot

Để thiết kế một chatbot AI hoặc RAG chatbot, trước hết cần xác định mục tiêu, người dùng, phạm vi trả lời và tiêu chí thành công của hệ thống. Tiếp theo, thu thập dữ liệu chính thức như FAQ, website, PDF, quy chế, tài liệu nội bộ hoặc database liên quan.

Dữ liệu cần được làm sạch, loại bỏ nội dung trùng lặp, lỗi thời, nhạy cảm và gắn metadata như nguồn, thời gian, tiêu đề. Với RAG, tài liệu được chia thành các chunk nhỏ để dễ truy xuất và phù hợp giới hạn context. Sau đó tạo embedding để biến các chunk thành vector biểu diễn ngữ nghĩa, rồi lưu vào vector database kèm metadata.

Khi người dùng đặt câu hỏi, hệ thống tạo embedding cho câu hỏi, truy xuất các chunk liên quan, xây dựng prompt gồm câu hỏi, context và quy tắc trả lời, sau đó LLM sinh câu trả lời dựa trên tài liệu. Hệ thống cần có guardrails để hạn chế bịa thông tin, không lộ dữ liệu nhạy cảm, không trả lời ngoài phạm vi và chống prompt injection.

Sau khi triển khai, cần logging và monitoring các chỉ số như correctness, hallucination rate, retrieval quality, latency, token cost và feedback người dùng. Dựa trên log và feedback, hệ thống được cải thiện liên tục về dữ liệu, prompt, retrieval và chất lượng trả lời.

### Bài 2: Hạ tầng Ops/Monitoring cho chatbot hoặc agent

Ops và monitoring cho hệ thống AI là phần vận hành sau khi triển khai, nhằm đảm bảo hệ thống chạy ổn định, đúng chất lượng, kiểm soát chi phí và phát hiện lỗi sớm. Hạ tầng cơ bản có thể chia thành các lớp: data layer để lưu dữ liệu và tài liệu nguồn, processing/indexing layer để làm sạch dữ liệu, chunking và embedding, model/LLM layer để sinh câu trả lời, API/serving layer để cung cấp dịch vụ, application layer cho giao diện người dùng và observability layer để logging, monitoring, tracing và alerting.

Với chatbot/RAG, cần monitor input của người dùng, output của model, retrieved context, chất lượng truy xuất, correctness, hallucination rate, latency, token cost và feedback người dùng. Nếu retrieval lấy sai chunk hoặc model trả lời ngoài context, hệ thống cần ghi log để phân tích và cải thiện dữ liệu, prompt hoặc retriever.

Với AI agent, ngoài các chỉ số trên cần monitor tool calls, tool input/output, tool error rate, số lần gọi tool, vòng lặp vô hạn và các hành động rủi ro. Những tác vụ quan trọng nên có human-in-the-loop để con người phê duyệt trước khi thực hiện.

Hệ thống cần alerting khi error rate tăng, latency cao, token cost bất thường, hallucination nhiều hoặc feedback xấu tăng. Cuối cùng, log và feedback được dùng để cải thiện liên tục prompt, dữ liệu, retrieval và mô hình.

### Bài 3: Thiết kế AI agent hoặc sản phẩm AI thực tế

Để thiết kế một AI agent hoặc sản phẩm AI thực tế, trước hết cần xác định vấn đề cần giải quyết, người dùng mục tiêu, input, output và tiêu chí thành công. Ví dụ nếu xây agent hỗ trợ học AI, input là câu hỏi hoặc tài liệu học, output là câu trả lời, kế hoạch học hoặc bài kiểm tra.

Tiếp theo cần thu thập và xử lý dữ liệu phù hợp như tài liệu nội bộ, FAQ, PDF, database hoặc log người dùng. Sau đó chọn hướng AI phù hợp: ML/DL cho bài toán dự đoán hoặc phân loại, RAG cho hỏi đáp dựa trên tài liệu, và agent khi nhiệm vụ cần nhiều bước hoặc cần gọi công cụ.

Với AI agent, các thành phần chính gồm LLM làm bộ não xử lý, planner để lập kế hoạch, memory để lưu ngữ cảnh, tools/API để hành động, executor để thực hiện từng bước, safety layer để kiểm soát rủi ro và monitoring để theo dõi hệ thống.

Pipeline cơ bản là: nhận input -> phân tích mục tiêu -> lập kế hoạch -> gọi tool hoặc truy xuất dữ liệu -> tổng hợp kết quả -> kiểm tra an toàn -> trả output. Hệ thống cần đánh giá bằng metric phù hợp như task success rate, tool error rate, latency, token cost, user satisfaction và safety violation rate.

Các rủi ro cần kiểm soát gồm dữ liệu sai, bias, hallucination, lộ dữ liệu, gọi sai tool, vòng lặp vô hạn và hành động nguy hiểm. Vì vậy cần guardrails, logging, monitoring, feedback loop và human-in-the-loop cho tác vụ quan trọng.

## 4. Bảng keyword cứu điểm

### RAG

`document loading`, `cleaning`, `chunking`, `embedding`, `vector database`, `retrieval`, `similarity search`, `prompt construction`, `LLM`, `citation`, `guardrails`, `feedback`.

### Monitoring/Ops

`logs`, `metrics`, `traces`, `latency`, `token cost`, `error rate`, `retrieval quality`, `hallucination rate`, `alerting`, `dashboard`, `feedback loop`.

### AI Agent

`goal`, `planner`, `memory`, `tools`, `executor`, `tool calls`, `tool error`, `human-in-the-loop`, `safety layer`, `task success rate`.

### ML/DL

`train`, `validation`, `test`, `overfitting`, `underfitting`, `accuracy`, `precision`, `recall`, `F1`, `confusion matrix`, `CNN`, `RNN`, `Transformer`, `attention`.

### Python/NumPy/Pandas

`range`, `list`, `dict`, `function`, `np.array`, `shape`, `slicing`, `boolean mask`, `mean`, `df.head()`, `df.info()`, `df.describe()`, `df.isnull().sum()`, `value_counts()`.

## 5. Checklist 30 phút cuối

1. Đọc thuộc 3 câu:
   - RAG là gì?
   - Vì sao RAG giảm hallucination?
   - AI agent khác chatbot thường ở đâu?

2. Đọc lại 3 bài tự luận mẫu:
   - RAG chatbot
   - Ops/Monitoring
   - AI Agent

3. Ôn bảng dễ sai:
   - Train / validation / test
   - Accuracy / precision / recall / F1
   - CNN / RNN / Transformer
   - `df.head()` / `df.info()` / `df.describe()`
   - `df.shape` / `df.columns`
   - `arr[1:4]`
   - `arr[row, col]`

4. Khi vào thi tự luận, luôn viết theo khung:

   ```text
   Mục tiêu -> Dữ liệu -> Pipeline -> Đánh giá -> Rủi ro -> Monitoring
   ```

5. Câu nào bí, vẫn phải viết keyword đúng. Đừng bỏ trắng.
