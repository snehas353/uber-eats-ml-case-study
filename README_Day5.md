# Uber Eats ML Capstone Project – Day 5

## 1. Objective
The objective of Day 5 is to develop and evaluate machine learning models using the prepared Uber Eats dataset. The goal is to predict delivery time and identify factors that influence delivery performance.

## 2. Review of Prepared Data
Reviewed the data prepared during the previous stages of the project.

Activities included:
- Checking the selected input features.
- Verifying the target variable for delivery-time prediction.
- Confirming that numerical and categorical features were prepared appropriately.
- Checking the training and testing datasets, where applicable.

## 3. Model Development
Worked on developing machine learning models for delivery-time prediction.

The models considered may include:
- Linear Regression: Establishes a baseline and estimates the relationship between input features and delivery time.
- Random Forest Regressor: Captures more complex relationships between features and delivery time.

The models were trained using the prepared training dataset.

## 4. Model Prediction
Used the trained models to generate delivery-time predictions on the test dataset.

Compared predicted delivery times with actual values to understand how accurately the models estimated delivery duration.

## 5. Model Evaluation
Evaluated model performance using suitable regression metrics.

### Mean Absolute Error (MAE)
Measures the average absolute difference between actual and predicted delivery times. Lower values indicate smaller prediction errors.

### Root Mean Squared Error (RMSE)
Measures prediction errors while penalizing larger errors more heavily. Lower values indicate better performance.

### R-squared (R²)
Measures how much variation in the target variable is explained by the model. Values closer to 1 generally indicate a better fit, although negative values are possible.

## 6. Model Comparison
Compared model evaluation results to identify which model performed better on the test data.

Considered:
- MAE values.
- RMSE values.
- R² scores.
- Differences between actual and predicted delivery times.

The final model should be selected based on test performance and the project's requirements rather than model complexity alone.

## 7. Feature Importance and Prediction Analysis
Where supported by the selected model, examined feature importance to understand which variables contributed most to predictions.

Potential factors included:
- Delivery distance.
- Traffic conditions.
- Weather conditions.
- Food preparation time.
- Relevant order and location characteristics.

Reviewed actual-versus-predicted visualizations to identify prediction patterns and potential errors.

## 8. Results and Documentation
Organized the model evaluation results and supporting project outputs.

Potential deliverables included:
- Trained model files.
- Model comparison results.
- Evaluation metrics.
- Prediction visualizations.
- Feature-importance analysis.
- Final project report.

## 9. Tools and Technologies
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook
- VS Code
- Git and GitHub

## 10. Outcome
Day 5 focused on machine learning model development and evaluation for Uber Eats delivery-time prediction.

The model comparison provides a basis for identifying a suitable prediction approach. The results can help explain delivery-time variation and support further investigation into operational efficiency.

## 11. Future Improvements
- Tune model hyperparameters.
- Evaluate additional regression algorithms.
- Investigate outliers and prediction errors.
- Improve feature quality and selection.
- Validate performance on unseen data.
- Save and document the best-performing model for future use.
