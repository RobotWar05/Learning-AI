"""Khung code scikit-learn sẽ triển khai chi tiết sau."""


def pipeline_steps():
    steps = [
        "load data",
        "split X/y",
        "train_test_split",
        "model.fit",
        "model.predict",
        "evaluate",
    ]
    return steps


if __name__ == "__main__":
    for step in pipeline_steps():
        print(step)
