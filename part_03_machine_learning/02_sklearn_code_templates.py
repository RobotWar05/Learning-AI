"""Template scikit-learn cơ bản cho ôn thi Machine Learning."""

from sklearn.cluster import KMeans
from sklearn.datasets import make_classification, make_regression
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    mean_squared_error,
    precision_score,
    recall_score,
)
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


def regression_template():
    """Linear Regression với dữ liệu tổng hợp."""
    X, y = make_regression(n_samples=80, n_features=2, noise=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    print("Linear Regression MSE:", round(mse, 2))


def classification_template():
    """Logistic Regression, KNN, Decision Tree và metrics."""
    X, y = make_classification(
        n_samples=120,
        n_features=4,
        n_informative=3,
        n_redundant=0,
        random_state=42,
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    models = {
        "LogisticRegression": LogisticRegression(max_iter=1000),
        "KNN": KNeighborsClassifier(n_neighbors=3),
        "DecisionTree": DecisionTreeClassifier(max_depth=4, random_state=42),
    }

    for name, model in models.items():
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        print("\nModel:", name)
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Precision:", precision_score(y_test, y_pred, zero_division=0))
        print("Recall:", recall_score(y_test, y_pred, zero_division=0))
        print("F1:", f1_score(y_test, y_pred, zero_division=0))
        print("Confusion matrix:")
        print(confusion_matrix(y_test, y_pred))


def kmeans_template():
    """KMeans cho bài toán clustering không có label."""
    X = [
        [1.0, 1.0],
        [1.2, 0.8],
        [8.0, 8.0],
        [8.2, 7.8],
        [0.9, 1.1],
        [7.9, 8.1],
    ]
    model = KMeans(n_clusters=2, random_state=42, n_init=10)
    labels = model.fit_predict(X)
    print("\nKMeans labels:", labels)
    print("Cluster centers:", model.cluster_centers_)


def cross_validation_template():
    """Ví dụ cross validation để đánh giá ổn định hơn một lần split."""
    X, y = make_classification(
        n_samples=100,
        n_features=4,
        n_informative=3,
        n_redundant=0,
        random_state=7,
    )
    model = LogisticRegression(max_iter=1000)
    scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
    print("\nCross-val accuracy scores:", scores)
    print("Mean accuracy:", scores.mean())


if __name__ == "__main__":
    regression_template()
    classification_template()
    kmeans_template()
    cross_validation_template()
