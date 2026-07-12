"""Fill the five TODOs, then run: python students/starter_code.py"""

from sklearn.base import clone
from sklearn.datasets import load_breast_cancer, make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Dataset 1: real, high-dimensional classification data
cancer = load_breast_cancer()
X_cancer, y_cancer = cancer.data, cancer.target

# Dataset 2: simulated, two-dimensional nonlinear data
X_moons, y_moons = make_moons(n_samples=300, noise=0.25, random_state=42)

# TODO 1: Add a Logistic Regression classifier to the pipeline.
logistic_model = make_pipeline(StandardScaler(), ...)

# TODO 2: Configure the KNN classifier to use five neighbors.
knn_model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=...))

models = {"Logistic Regression": logistic_model, "KNN": knn_model}
datasets = {"Breast Cancer": (X_cancer, y_cancer), "make_moons": (X_moons, y_moons)}

for dataset_name, (X, y) in datasets.items():
    print("=" * 40)
    print(dataset_name)

    # TODO 3 and TODO 4: Keep 30% for testing and preserve class proportions.
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=...,
        random_state=42,
        stratify=...,
    )

    for model_name, model in models.items():
        # clone() gives each dataset/model combination a fresh unfitted pipeline.
        current_model = clone(model)

        # TODO 5: Train the fresh model on the training data.
        current_model.____(X_train, y_train)
        y_pred = current_model.predict(X_test)

        print(model_name)
        print("Accuracy:", round(accuracy_score(y_test, y_pred), 3))
        if dataset_name == "Breast Cancer":
            malignant_recall = recall_score(y_test, y_pred, pos_label=0)
            print("Malignant Recall:", round(malignant_recall, 3))
        print()
