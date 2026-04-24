# Ghi chú kiến trúc Ops

## Kiến trúc vận hành tối thiểu

1. API nhận request.
2. Agent/LLM xử lý.
3. Tool hoặc database được gọi khi cần.
4. Logging/Tracing ghi lại toàn bộ flow.
5. Evaluation kiểm tra chất lượng.
6. Dashboard theo dõi latency, error, cost.

## Nguyên tắc vận hành

- Không deploy thay đổi prompt/model mà không có kiểm tra.
- Cần lưu version của prompt.
- Cần có dữ liệu test đại diện.
- Cần biết rollback về bản ổn định.
