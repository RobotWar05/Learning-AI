"""Khung PyTorch cơ bản sẽ triển khai chi tiết sau."""


def training_loop_concept():
    return [
        "forward",
        "compute loss",
        "zero gradients",
        "backward",
        "optimizer step",
    ]


if __name__ == "__main__":
    for step in training_loop_concept():
        print(step)
