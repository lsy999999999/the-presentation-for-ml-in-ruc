# Speaker prompts: Part 3 (about 8-9 minutes)

## Slide 1: Two datasets, one question (1 minute)

"We will use the same two classifiers twice. Breast Cancer is a real medical dataset with 30 features. `make_moons` is simulated two-dimensional data with a curved pattern. The question is not simply which model wins. It is how the same models react to different data structures and different evaluation goals."

## Slide 2: Your coding task (about 4 minutes)

"Please complete the five small TODOs in the starter file. Build the two pipelines, choose K, make a stratified 70/30 split, and fit a fresh model. You do not need to write plotting code. Raise a hand if you are blocked."

## Slide 3: Breast Cancer (about 1.5 minutes)

"Accuracy is useful, but it is not enough in a medical setting. The malignant label here is zero, so our recall explicitly uses `pos_label=0`. A false negative misses a malignant case, which can be more serious than a false positive. Ask: is the model with the highest accuracy always the safest one?"

## Slide 4: make_moons (about 2 minutes)

"Logistic Regression learns a linear boundary after scaling the features. It cannot naturally follow the curved moons. KNN uses nearby observations, so its boundary bends around local structure. The conclusion is conditional: choose a model using data geometry, the metric, and the consequences of errors."
