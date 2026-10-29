# Uber Eats ML Capstone Project – Day 4

## 1. Objective
The objective of Day 4 is to prepare the Uber Eats datasets for machine learning by selecting relevant features, processing categorical and numerical variables, and organizing the data for model training and evaluation.

## 2. Review of EDA Findings
Reviewed the findings from Day 3 Exploratory Data Analysis to understand the factors that may influence delivery performance.

Areas considered included:
- Delivery time and preparation time.
- Delivery distance.
- Weather and traffic conditions.
- Order amount and order characteristics.
- Restaurant and location-related information.

These observations help identify potentially useful features for predicting delivery time.

## 3. Feature Selection
Identified relevant input variables for the machine learning task.

Potential features included:
- Delivery distance.
- Food preparation time, when available at prediction time.
- Weather conditions.
- Traffic conditions.
- Order characteristics.
- Relevant restaurant or location information.

Selected features should be based on their relevance to the target variable and their availability at the time predictions are made.

## 4. Data Cleaning and Validation
Reviewed the data to ensure it was suitable for model development.

Activities included:
- Checking missing values in selected features.
- Reviewing duplicate records.
- Validating numerical values and categorical labels.
- Checking data types and inconsistent values.
- Ensuring the target variable was available and valid.

Any cleaning decisions should preserve meaningful observations and avoid introducing misleading values.

## 5. Feature Engineering
Prepared existing columns and derived useful features for model training where appropriate.

Potential activities included:
- Extracting hour or day information from timestamps.
- Preparing delivery distance and duration features.
- Grouping relevant categorical information.
- Creating suitable numerical and categorical input variables.

Feature engineering helps represent business information in a form that machine learning algorithms can process.

## 6. Encoding Categorical Variables
Reviewed categorical features such as weather, traffic, city, and restaurant category.

Where required, converted categorical values into numerical representations using appropriate encoding techniques, such as one-hot encoding.

Encoding methods should be selected based on the feature type and the requirements of the chosen model.

## 7. Preparing the Target Variable
Identified delivery time as the target variable for the prediction task.

Prepared the target values in a suitable numerical format and checked that the target did not contain invalid or missing values.

Care was taken to avoid using information that would not be available when making a real-world delivery-time prediction.

## 8. Training and Testing Data Preparation
Prepared the feature matrix and target variable for model development.

Where applicable:
- Separated input features from the target variable.
- Split the data into training and testing sets.
- Used a consistent random state for reproducibility.
- Ensured preprocessing steps were fitted using training data only to reduce data leakage.

## 9. Tools and Technologies
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook
- VS Code

## 10. Deliverables
- Reviewed and selected model features.
- Validated data for machine learning.
- Prepared numerical and categorical variables.
- Engineered relevant features where required.
- Prepared input features and target variable.
- Organized data for model training and evaluation.

## 11. Outcome
Day 4 focused on preparing the Uber Eats data for machine learning by reviewing important features, validating data quality, and organizing the target and input variables.

These preparations establish the foundation for developing, training, and evaluating delivery-time prediction models.

## Next Steps
Develop machine learning models, compare their performance using appropriate evaluation metrics, and identify the model that best meets the project's prediction objective.
