# Ghi chú Python Core

File này dùng để ghi lỗi sai và quy tắc cần nhớ khi ôn thi.

## Lỗi thiếu dấu hai chấm

Sai:

```python
if score >= 5
    print("pass")
```

Đúng:

```python
if score >= 5:
    print("pass")
```

## Sai indentation

Sai:

```python
for x in [1, 2, 3]:
print(x)
```

Đúng:

```python
for x in [1, 2, 3]:
    print(x)
```

## `input()` trả về string

Sai:

```python
age = input("Age: ")
print(age + 1)
```

Đúng:

```python
age = int(input("Age: "))
print(age + 1)
```

## Index out of range

Sai:

```python
values = [10, 20, 30]
print(values[3])
```

Đúng:

```python
values = [10, 20, 30]
print(values[2])
```

## Missing dict key

Sai:

```python
student = {"name": "An"}
print(student["score"])
```

Đúng:

```python
student = {"name": "An"}
print(student.get("score", 0))
```

## Dùng `=` thay vì `==`

Sai:

```python
if score = 10:
    print("max")
```

Đúng:

```python
if score == 10:
    print("max")
```

## Quên `return`

Sai:

```python
def add(a, b):
    result = a + b
```

Đúng:

```python
def add(a, b):
    return a + b
```

## Sửa list khi đang duyệt

Sai:

```python
values = [1, 2, 3, 4]
for x in values:
    if x % 2 == 0:
        values.remove(x)
```

Đúng:

```python
values = [1, 2, 3, 4]
odd_values = [x for x in values if x % 2 != 0]
```

## `append` vs `extend`

```python
values = [1, 2]
values.append([3, 4])
print(values)  # [1, 2, [3, 4]]

values = [1, 2]
values.extend([3, 4])
print(values)  # [1, 2, 3, 4]
```
