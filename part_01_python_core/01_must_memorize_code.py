"""Các mẫu code Python nền tảng cần gõ lại trước kỳ thi AI."""

import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


print("=== 1. print, variables, data types ===")
name = "An"
age = 20
height = 1.70
is_student = True
print(name, age, height, is_student)
print(type(name), type(age), type(height), type(is_student))


print("\n=== 2. input and type casting - ví dụ, không chạy để tránh chờ nhập ===")
# raw_age = input("Nhap tuoi: ")
# age_number = int(raw_age)
# print(age_number + 1)


print("\n=== 3. if/elif/else score classification ===")
score = 8.0
if score >= 8.0:
    level = "Gioi"
elif score >= 6.5:
    level = "Kha"
elif score >= 5.0:
    level = "Trung binh"
else:
    level = "Yeu"
print(f"Diem {score} -> {level}")


print("\n=== 4. for + range sum from 1 to 10 ===")
total = 0
for i in range(1, 11):
    total += i
print("Tong 1..10 =", total)


print("\n=== 5. while factorial ===")
n = 5
factorial = 1
current = 1
while current <= n:
    factorial *= current
    current += 1
print(f"{n}! =", factorial)


print("\n=== 6. list basics ===")
numbers = [10, 20, 30, 40]
print("Phan tu dau:", numbers[0])
numbers.append(50)
numbers.remove(20)
print("List sau khi sua:", numbers)
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Mean:", sum(numbers) / len(numbers))


print("\n=== 7. loop through list ===")
for value in numbers:
    print("Gia tri:", value)


print("\n=== 8. list comprehension ===")
squares = [x * x for x in range(1, 6)]
even_numbers = [x for x in numbers if x % 2 == 0]
print("Binh phuong:", squares)
print("So chan:", even_numbers)


print("\n=== 9. dictionary basics ===")
student = {
    "name": "An",
    "score": 8.5,
    "label": "pass",
}
print(student["name"])
student["score"] = 9.0
student["class"] = "AI01"
print(student)


print("\n=== 10. frequency counting with dict ===")
labels = ["positive", "negative", "positive", "neutral", "positive"]
label_count = {}
for label in labels:
    if label not in label_count:
        label_count[label] = 0
    label_count[label] += 1
print(label_count)


print("\n=== 11. set for removing duplicates ===")
duplicated = [1, 2, 2, 3, 3, 3]
unique_values = set(duplicated)
print(unique_values)


print("\n=== 12. string methods ===")
text = "  AI,Machine Learning,Python  "
clean_text = text.strip().lower()
tokens = clean_text.split(",")
joined = " | ".join(tokens)
print(clean_text)
print(tokens)
print(joined)


print("\n=== 13. f-string ===")
model_name = "Logistic Regression"
accuracy = 0.92
print(f"Model {model_name} co accuracy = {accuracy:.2f}")


print("\n=== 14. function is_even ===")
def is_even(x):
    return x % 2 == 0


print(is_even(4), is_even(5))


print("\n=== 15. function mean ===")
def mean(values):
    if len(values) == 0:
        return None
    return sum(values) / len(values)


print(mean([1, 2, 3, 4]))


print("\n=== 16. function is_prime ===")
def is_prime(x):
    if x < 2:
        return False
    for divisor in range(2, int(x ** 0.5) + 1):
        if x % divisor == 0:
            return False
    return True


print(is_prime(2), is_prime(9), is_prime(13))


print("\n=== 17. function count_words ===")
def count_words(sentence):
    words = sentence.strip().lower().split()
    return len(words)


print(count_words("AI can learn from data"))


print("\n=== 18. function min_max_normalize ===")
def min_max_normalize(values):
    min_value = min(values)
    max_value = max(values)
    if max_value == min_value:
        return [0 for _ in values]
    return [(x - min_value) / (max_value - min_value) for x in values]


print(min_max_normalize([10, 20, 30, 40, 50]))


print("\n=== 19. function train_test_split_simple ===")
def train_test_split_simple(data, test_ratio=0.2):
    split_index = int(len(data) * (1 - test_ratio))
    train_data = data[:split_index]
    test_data = data[split_index:]
    return train_data, test_data


sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train, test = train_test_split_simple(sample_data, test_ratio=0.2)
print("Train:", train)
print("Test:", test)


print("\n=== 20. try/except ===")
raw_value = "12"
try:
    number = int(raw_value)
    print(number + 1)
except ValueError:
    print("Khong the ep kieu sang int")


print("\n=== 21. read text file example - ví dụ, không chạy nếu thiếu file ===")
# with open("data.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)


print("\n=== 22. write text file example - ví dụ, đang comment để không tạo file phụ ===")
# with open("output.txt", "w", encoding="utf-8") as f:
#     f.write("Ket qua hoc Python")


print("\n=== 23. small dataset as list of dict and label counting ===")
dataset = [
    {"text": "I like AI", "label": "positive"},
    {"text": "This is hard", "label": "negative"},
    {"text": "Python is useful", "label": "positive"},
    {"text": "I need more practice", "label": "negative"},
]

counts = {}
for row in dataset:
    label = row["label"]
    counts[label] = counts.get(label, 0) + 1

print("So luong tung label:", counts)
