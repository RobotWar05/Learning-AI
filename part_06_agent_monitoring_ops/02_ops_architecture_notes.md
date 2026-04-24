# Ghi chú kiến trúc Ops

## 1. Local dev

Local dev dùng để thử nhanh prompt, pipeline và code. Không nên dùng dữ liệu production nhạy cảm nếu không cần.

## 2. Staging

Staging mô phỏng production để kiểm tra trước khi deploy thật. Nên chạy evaluation dataset tại đây.

## 3. Production

Production cần ổn định, có monitoring, alerting, rollback và quản lý secret.

## 4. API backend

Backend nhận request, xác thực, gọi retriever/LLM/tool, ghi log và trả response.

## 5. Database

Database lưu user, session, feedback, evaluation result hoặc audit log.

## 6. Vector database

Vector database lưu chunk embedding và metadata. Cần version dữ liệu để biết câu trả lời dựa trên bản tài liệu nào.

## 7. Model provider

Model provider có thể là API ngoài hoặc model tự host. Cần theo dõi latency, cost, rate limit và lỗi.

## 8. Secrets management

API key không được hard-code. Dùng environment variables hoặc secret manager.

## 9. Environment variables

Các config như API key, model name, database URL, log level nên đưa vào environment variables.

## 10. CI/CD concept

CI kiểm tra code, test và lint. CD triển khai tự động có kiểm soát. Với AI app, nên thêm evaluation trước deploy.

## 11. Deployment

Cần biết bản nào đang chạy: code version, prompt version, model version, data version.

## 12. Rollback

Rollback là quay về phiên bản ổn định khi bản mới gây lỗi. Cần rollback được prompt/model/data, không chỉ code.

## 13. Rate limit

Rate limit bảo vệ hệ thống khỏi lạm dụng, giảm cost và tránh vượt quota model provider.

## 14. Caching

Cache có thể giảm latency và cost với câu hỏi lặp lại. Cần cẩn thận khi dữ liệu thay đổi.

## 15. Fallback model

Khi model chính lỗi hoặc quá tải, có thể chuyển sang model phụ. Cần log rõ khi fallback xảy ra.

## 16. Incident response

Quy trình tối thiểu:

1. Xác định ảnh hưởng.
2. Xem dashboard.
3. Kiểm tra logs/traces.
4. Rollback nếu cần.
5. Ghi postmortem.
6. Thêm test/evaluation để tránh lặp lại.

## 17. Audit log

Audit log ghi lại thay đổi quan trọng như prompt update, data ingestion, model switch và config change.
