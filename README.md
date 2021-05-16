# ml-scoring

## Logistic regression

Distribution of GINI across crossvalidation folds and ROC curve for example train/test split:

<img src="./Img/logreg_cv_roc.png" width="800"/>

Shap values:

<img src="./Img/logreg_shap.png" width="800"/>

## Results

|                      | Taiwan 30k | Taiwan 10k | Taiwan 1k |
|----------------------|------------|------------|-----------|
| Logistic regression  | 0.482 (0.011) | 0.476 (0.022) | 0.448 (0.045) |
| Decision tree        |            |            |           |
| Random forest        |            |            |           |
| LightGBM             |            |            |           |