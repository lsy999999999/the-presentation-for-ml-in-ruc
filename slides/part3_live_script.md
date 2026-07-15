# Part 3 Live Teaching Script (8-9 minutes)

This script is designed for a live coding exercise, not for reading the slides word for word.

- English blockquotes are the words to say.
- Chinese text in brackets is a stage direction and should not be read aloud.
- The bold English sentences are anchor lines. If you lose your place, find the next bold line and continue.

## Before Class

[最好在上课前把仓库链接发到群里，让同学提前 clone 并安装依赖。课堂上的 4 分钟只用来改代码，不用来安装 Python 包。]

[上台前准备好三个窗口：]

1. PPT，停在 Part 3 的第一页。
2. 编辑器，打开 `students/starter_code.py`。
3. 终端，进入仓库并激活虚拟环境。

[在自己的电脑上提前确认以下命令可以运行：]

```bash
source .venv/bin/activate
make run
make test
```

[再准备好 `instructor/answer_key.md` 和 `outputs/decision_boundaries.png`。即使现场有人运行失败，你仍然可以展示答案和结果。]

[团队分工建议：一人留在前面控制 PPT 和计时，其他成员在同学实操时走动答疑。这也符合课堂要求。]

## 0:00-0:45 | Transition to the Exercise

[切到 Slide 1。面对同学，不要先看电脑。]

> **Now we have seen how Logistic Regression and KNN work. It is time to test them ourselves.**
>
> In this short exercise, we will use the same two classifiers on two very different datasets. The goal is not only to find which number is higher. The goal is to understand why the models behave differently.
>
> If your Python environment is not ready, please work with the person next to you. One working computer per pair is enough.

## 0:45-1:25 | Introduce the Two Datasets

[指向 Slide 1 左侧。]

> The first dataset is the Breast Cancer dataset. It is real data with 569 observations and 30 features. The task is to classify a tumor as malignant or benign.

[指向右侧。]

> The second dataset is `make_moons`. It is simulated data with 300 observations and only two features. Its two classes form a curved, nonlinear pattern.
>
> **Before we run the code, make a prediction: on which dataset do you expect KNN to have an advantage?**

[停 3 秒，看同学反应。可以请一位同学回答；没人回答就继续。]

> Keep your prediction in mind. We will check it in a few minutes.

## 1:25-2:00 | Explain the Coding Task

[切到 Slide 2，同时在编辑器中打开 `students/starter_code.py`，让大家看到文件路径。]

> Please open `students/starter_code.py`. There are only five TODOs.
>
> You need to complete Logistic Regression, choose the number of neighbors for KNN, make a train-test split, and fit the models. The rest of the code is already provided.
>
> We use exactly the same workflow for both datasets, so please do not write two separate programs.
>
> When you finish, run this command from the project folder:

```bash
python students/starter_code.py
```

> **You have about two and a half minutes. Please start now.**

## 2:00-4:30 | Students Work

[保持 Slide 2，不要继续讲新知识。看计时，团队成员开始巡场。优先解决“文件找不到”和“环境未激活”，不要替同学重装整个环境。]

### At about 2:45

[如果很多人停在前两个 TODO，给第一个提示。]

> Here is the first hint: use `max_iter=1000` for Logistic Regression, and use five neighbors for KNN.

### At about 3:30

[给第二个提示。]

> For the split, use 30 percent as test data and keep the class proportions with `stratify=y`.

### At about 4:05

[给最后提示和倒计时。]

> The last missing method is the method that trains a scikit-learn model. You have about twenty seconds left.

### If most students are blocked by setup

[不要等待安装。让他们两人一组，然后在你的电脑上继续演示。]

> It looks like setup is taking longer than expected. That is okay. Please look at the front screen or join a nearby pair. We will complete the five lines together so that we can focus on the results.

## 4:30-5:10 | Reveal the Answers and Run

[回到自己的编辑器，快速依次展示五个答案。不要逐行解释整个文件。]

> **Let us check the five answers together.**
>
> They are `LogisticRegression(max_iter=1000)`, five neighbors, `test_size=0.3`, `stratify=y`, and finally `fit`.
>
> Notice that both models include `StandardScaler`. Scaling is especially important for KNN because KNN compares distances between observations.

[在终端运行：]

```bash
python students/starter_code.py
```

> Your results should be the same as, or very close to, the results on my screen.

## 5:10-6:35 | Discuss the Breast Cancer Results

[切到 Slide 3。先让同学看表格两秒。]

> For the Breast Cancer data, Logistic Regression has an accuracy of 0.988, while KNN has an accuracy of 0.959.
>
> However, accuracy is not the only number we should check in a medical problem. Here, label zero means malignant. Therefore, we calculate malignant recall with `pos_label=0`.
>
> **Malignant recall asks: out of all truly malignant cases, how many did the model identify correctly?**

[指向 recall 一列。]

> Logistic Regression has a malignant recall of 0.984. It misses one malignant case in this test set. KNN has a recall of 0.891, so it misses seven malignant cases.
>
> A missed malignant case is a false negative, and its cost may be serious. In this example, Logistic Regression is better on both accuracy and malignant recall. So there is no trade-off between these two metrics in this particular result. The important lesson is that accuracy alone would not tell us how many malignant cases were missed.
>
> **For a real application, we must choose metrics according to the cost of errors.**

## 6:35-7:55 | Discuss the `make_moons` Results

[切到 Slide 4。先指左图，再指右图。]

> Now look at `make_moons`. Logistic Regression reaches an accuracy of 0.856, while KNN reaches 0.911.
>
> Logistic Regression learns one linear decision boundary after scaling. But the two moon shapes curve around each other, so one straight boundary cannot separate them very well.
>
> KNN makes predictions from nearby training observations. Because it works locally, its decision boundary can bend around the curved pattern.
>
> **This does not mean that KNN is always better. It means that KNN matches the geometry of this dataset better.**
>
> KNN can also become sensitive to noise and to the choice of K. Logistic Regression may be simpler, faster to interpret, and more stable when a roughly linear boundary is appropriate.

## 7:55-8:40 | Final Takeaway

[回到同学，不必再切页面。放慢语速。]

> Let us return to our prediction.
>
> On the real, high-dimensional Breast Cancer data, Logistic Regression performs better in this experiment. On the curved `make_moons` data, KNN performs better because it can learn a flexible local boundary.
>
> **The main conclusion is simple: model choice depends on data structure, evaluation goals, and the cost of errors.**
>
> A higher accuracy on one dataset does not make a model universally better. We need to ask what structure the data has, what error matters, and what metric answers our real question.
>
> That is the end of our exercise. Thank you.

## Flexible Timing

### If students finish early

> Please discuss one question with your partner: what might happen if we change K from 5 to 1, or from 5 to 30?

[收一两个答案，然后总结：]

> A very small K creates a more flexible boundary and may overfit noise. A larger K creates a smoother boundary and may underfit the pattern.

### If students need more time

[最多多给 30-45 秒，并压缩结果讨论。不要压缩最后的核心结论。]

> I will give you thirty more seconds. You do not need to understand every line yet; focus on completing the five TODOs and producing the output.

### If nobody can run the code

[直接展示你的终端输出和 Slide 3、Slide 4。]

> We will use my output so that a setup problem does not stop the discussion. You can run the same file after class. For now, let us interpret the results together.

### If your own live demo fails

[不要现场长时间 debug。打开已经生成的结果图和 PPT。]

> The live environment is not cooperating, so I will use the reproducible output that I generated before class. The fixed random seed gives us the results shown here.

## Quick Answers for Questions

### Why do we use `StandardScaler`?

> KNN is based on distance, so a feature with a large numerical scale could dominate the distance. Scaling also makes the regularized Logistic Regression pipeline more appropriate and consistent.

### Why do we use `stratify=y`?

> It keeps approximately the same class proportions in the training and test sets, which makes the comparison more reliable.

### Why is malignant label zero?

> That is how this scikit-learn dataset defines its target: zero is malignant and one is benign. This is why malignant recall needs `pos_label=0`.

### Why can we not draw the Breast Cancer boundary?

> The Breast Cancer dataset has 30 features. A complete decision boundary exists in a 30-dimensional feature space, so we cannot display it directly on a two-dimensional plot.

### Why choose K equal to 5?

> Five is a simple demonstration value. In a real analysis, we would tune K using validation or cross-validation rather than assuming that five is optimal.

### Does this experiment prove that one model is better?

> No. It is one train-test split on two datasets. A stronger comparison would use cross-validation, uncertainty estimates, and possibly more metrics. This exercise demonstrates how model behavior changes with data geometry and evaluation goals.

### Why use `clone(model)`?

> It creates a fresh, unfitted copy for each dataset. This prevents a fitted model from one iteration from being accidentally reused in another.

## Pronunciation Reminders

- malignant: muh-LIG-nuhnt
- benign: bih-NINE
- recall: ree-CALL
- stratify: STRAT-ih-fy
- nonlinear: non-LIN-ee-er
- geometry: jee-OM-uh-tree
