
# Uber Eats ML Capstone Project
## Day 7 – Model Validation and Performance Analysis

### 1. Objective
The objective of Day 7 is to validate the trained machine learning model and evaluate its ability to predict delivery times on unseen data.

### 2. Activities Performed

- Loaded the processed Uber Eats dataset.
- Identified the model input features and target variable.
- Reviewed features for potential data leakage.
- Split the dataset into 80% training and 20% testing data.
- Trained the model using the training dataset.
- Generated predictions using the testing dataset.
- Evaluated model performance using MAE, RMSE and R².
- Compared actual and predicted delivery times.
- Performed residual and prediction error analysis.
- Created visualizations to understand model performance.
- Saved the validated model and evaluation results.

### 3. Model Evaluation Metrics

| Metric | Description |
|---|---|
| MAE | Measures the average absolute prediction error. |
| RMSE | Measures prediction error while penalizing larger errors. |
| R² | Measures how much variation in delivery time is explained by the model. |

### 4. Visualizations

The following visualizations were generated:

1. Actual vs Predicted Delivery Time
2. Distribution of Model Residuals
3. Residuals vs Predicted Delivery Time

### 5. Deliverables

The following files were generated:

- `data/processed/day7_test_predictions.csv`
- `data/processed/day7_evaluation_metrics.csv`
- `data/processed/day7_validation_summary.csv`
- `models/day7_validated_model.pkl`
- `submission/day7_validation_report.txt`

### 6. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Jupyter Notebook

### 7. Conclusion

The Day 7 activities focused on evaluating the delivery-time prediction model using a held-out test dataset.

Prediction results, evaluation metrics and residual analysis were saved for further review.

A feature leakage review and additional time-based validation are recommended before considering the model ready for deployment.
