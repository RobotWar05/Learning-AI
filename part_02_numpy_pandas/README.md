# PHẦN 2 - NUMPY VÀ PANDAS

## Mục tiêu

Sau phần này, bạn cần đọc hiểu và viết được code xử lý dữ liệu dạng mảng và bảng, đủ để chuẩn bị dữ liệu trước khi đưa vào mô hình Machine Learning.

## Vì sao NumPy/Pandas quan trọng trong AI

- NumPy giúp tính toán số nhanh, gọn và gần với dạng dữ liệu model cần.
- Pandas giúp đọc, lọc, làm sạch và thống kê dữ liệu bảng.
- Hầu hết pipeline ML đều có bước: đọc dữ liệu, kiểm tra dữ liệu, xử lý missing values, tách feature/label.

## Kiến thức cần học

### NumPy

- `ndarray`, `shape`, `ndim`, `dtype`.
- Indexing, slicing, boolean indexing.
- Vectorization và broadcasting.
- `axis`.
- `sum`, `mean`, `max`, `min`.
- `reshape`, `concatenate`.
- Tạo dữ liệu ngẫu nhiên bằng `random`.

### Pandas

- `Series`, `DataFrame`.
- `read_csv`.
- `head`, `info`, `describe`.
- Chọn cột, lọc dòng.
- `loc`, `iloc`.
- Thêm cột.
- `sort_values`.
- `groupby`.
- `merge`.
- Missing values: `isnull`, `dropna`, `fillna`.
- Export CSV.

## Thứ tự học

1. Học NumPy array, shape và slicing.
2. Học boolean mask và vectorized operation.
3. Học DataFrame, chọn cột và lọc dòng.
4. Học missing values, groupby và merge.
5. Gõ lại code trong `01_must_memorize_code.py`.
6. Làm bài tập mini dataset phục vụ ML.

## Tài liệu học chính

- [NumPy Absolute Beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Pandas Intro Tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)

## Dạng bài thi hay gặp

- Dự đoán shape sau khi reshape hoặc slicing.
- Lọc phần tử array bằng điều kiện.
- Tính mean theo hàng hoặc cột.
- Lọc DataFrame theo điều kiện.
- Groupby để tính trung bình theo nhãn.
- Xử lý missing values.
- Merge hai bảng theo key.

## File trong phần này

- [Checklist](./00_checklist.md)
- [Code bắt buộc nhớ - NumPy/Pandas](./01_must_memorize_code.py)
- [Giải thích code bắt buộc nhớ](./01_must_memorize_code.md)
- [Bài tập](./02_exercises.md)
- [Notes](./03_notes.md)
- [Ôn nhanh](./04_quick_review.md)

## Checklist hoàn thành

- [ ] Đọc README.
- [ ] Gõ lại code mẫu.
- [ ] Làm bài tập DataFrame filtering.
- [ ] Làm bài tập groupby và missing values.
- [ ] Trả lời được câu hỏi quick review.
