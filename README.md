# Logistic Regression vs. KNN: In-Class Exercise

This repository contains the student starter code for an in-class comparison of Logistic Regression and K-Nearest Neighbors (KNN).

| Dataset | Purpose | What to compare |
| --- | --- | --- |
| Breast Cancer | Real, 30-feature classification task | Test accuracy and malignant recall |
| `make_moons` | Simulated 2D nonlinear task | Test accuracy and decision boundaries |

The data are loaded from scikit-learn. No download, account, or external data file is needed after the Python dependencies are installed.

## Quick start

Python 3.11 or later is required by the pinned dependencies.

```bash
git clone https://github.com/lsy999999999/the-presentation-for-ml-in-ruc.git
cd the-presentation-for-ml-in-ruc
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Creating the virtual environment can take a little time and may produce no terminal output. Wait until the command prompt returns before continuing.

## Exercise

Open [`students/starter_code.py`](students/starter_code.py) and complete its five TODOs. The task is to:

1. Build a scaled Logistic Regression pipeline.
2. Build a scaled KNN pipeline with `k=5`.
3. Make a stratified 70/30 train-test split.
4. Fit fresh copies of both models.
5. Compare their performance on both datasets.

After completing the TODOs, run:

```bash
python students/starter_code.py
```

You can also use `make run`. Before the TODOs are completed, an error is expected.

## Sources

- scikit-learn, `load_breast_cancer`: https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-dataset
- scikit-learn, `make_moons`: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html
