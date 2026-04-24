# Bài tập NumPy và Pandas

## NumPy array creation

1. Tạo array từ list `[2, 4, 6, 8, 10]`.
2. In `shape`, `ndim`, `dtype`.
3. Tạo matrix 3x2 từ các số 1 đến 6.

## Slicing

1. Lấy 3 phần tử đầu của array.
2. Lấy cột thứ hai của matrix 2 chiều.
3. Lấy hàng cuối cùng của matrix.

## Boolean filtering

1. Lọc các phần tử `>= 6`.
2. Lọc các phần tử chẵn.
3. Đếm số phần tử lớn hơn mean.

## Normalize array

1. Min-max normalize `[10, 20, 30, 40, 50]`.
2. Viết function xử lý trường hợp toàn bộ giá trị bằng nhau.
3. Giải thích vì sao normalization cần trong một số thuật toán ML.

## DataFrame filtering

1. Tạo DataFrame gồm `name`, `age`, `score`, `label`.
2. Lọc các dòng có `score >= 7`.
3. Lọc các dòng có `label == "pass"`.
4. Chọn hai cột `name` và `score`.

## Groupby average

1. Tính điểm trung bình theo `label`.
2. Tính tuổi trung bình theo `label`.
3. Sắp xếp kết quả groupby giảm dần.

## Merge data

1. Tạo bảng sinh viên gồm `student_id`, `name`.
2. Tạo bảng điểm gồm `student_id`, `score`.
3. Merge hai bảng theo `student_id`.
4. Giải thích khác nhau giữa `left`, `inner`, `outer`.

## Handle missing values

1. Tạo DataFrame có ít nhất một giá trị `None`.
2. Dùng `isnull().sum()` để đếm missing values.
3. Dùng `fillna` để điền điểm thiếu bằng mean.
4. Dùng `dropna` và giải thích khi nào không nên dùng.

## Mini dataset processing for ML

1. Tạo DataFrame có các cột `height`, `weight`, `age`, `label`.
2. Tách `X = height, weight, age`.
3. Tách `y = label`.
4. Kiểm tra phân bố label.
5. Normalize các cột số bằng min-max.
