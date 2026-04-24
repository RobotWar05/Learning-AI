"""Code NumPy và Pandas cần nhớ cho ôn thi AI."""

import numpy as np
import pandas as pd


print("=== 1. Create NumPy array ===")
arr = np.array([10, 20, 30, 40, 50])
print(arr)


print("\n=== 2. shape, ndim, dtype ===")
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("shape:", matrix.shape)
print("ndim:", matrix.ndim)
print("dtype:", matrix.dtype)


print("\n=== 3. indexing and slicing ===")
print("arr[0]:", arr[0])
print("arr[1:4]:", arr[1:4])
print("matrix[0, 2]:", matrix[0, 2])
print("matrix[:, 1]:", matrix[:, 1])


print("\n=== 4. boolean mask ===")
mask = arr >= 30
print("mask:", mask)
print("filtered:", arr[mask])


print("\n=== 5. vectorized operations ===")
print("arr + 5:", arr + 5)
print("arr * 2:", arr * 2)
print("arr / 10:", arr / 10)


print("\n=== 6. broadcasting example ===")
scores = np.array([[7, 8, 9], [6, 7, 8]])
bonus = np.array([1, 0, 1])
print(scores + bonus)


print("\n=== 7. aggregation with axis ===")
data_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("sum all:", data_2d.sum())
print("sum axis=0:", data_2d.sum(axis=0))
print("sum axis=1:", data_2d.sum(axis=1))
print("mean axis=0:", data_2d.mean(axis=0))


print("\n=== 8. reshape ===")
reshaped = np.arange(1, 7).reshape(2, 3)
print(reshaped)


print("\n=== 9. create Pandas DataFrame manually ===")
df = pd.DataFrame(
    {
        "name": ["An", "Binh", "Chi", "Dung"],
        "score": [8.5, 6.0, 9.0, np.nan],
        "label": ["pass", "pass", "pass", "unknown"],
    }
)
print(df)
print(df.head())
print(df.describe(numeric_only=True))


print("\n=== 10. read_csv example - đang comment để không cần file ngoài ===")
# df_from_csv = pd.read_csv("students.csv")
# print(df_from_csv.head())


print("\n=== 11. select column ===")
print(df["score"])
print(df[["name", "label"]])


print("\n=== 12. filter rows ===")
passed = df[df["score"] >= 7]
print(passed)


print("\n=== 13. loc and iloc ===")
print("loc rows 0..1, columns name/score")
print(df.loc[0:1, ["name", "score"]])
print("iloc first two rows, first two columns")
print(df.iloc[0:2, 0:2])


print("\n=== 14. add new column ===")
df["score_filled"] = df["score"].fillna(df["score"].mean())
df["passed_exam"] = df["score_filled"] >= 6.5
print(df)


print("\n=== 15. groupby ===")
print(df.groupby("label")["score_filled"].mean())


print("\n=== 16. sort_values ===")
print(df.sort_values("score_filled", ascending=False))


print("\n=== 17. missing values ===")
print(df.isnull().sum())
print(df.dropna())
print(df.fillna({"score": 0}))


print("\n=== 18. merge two DataFrames ===")
classes = pd.DataFrame(
    {
        "name": ["An", "Binh", "Chi", "Dung"],
        "class_name": ["AI01", "AI01", "AI02", "AI02"],
    }
)
merged = pd.merge(df, classes, on="name", how="left")
print(merged)


print("\n=== 19. export CSV example - đang comment để không tạo file phụ ===")
# merged.to_csv("students_processed.csv", index=False)
