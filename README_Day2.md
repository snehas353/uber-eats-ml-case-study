# Uber Eats ML Capstone Project – Day 2

## 1. Objective
The objective of Day 2 is to continue the Uber Eats ML Capstone Project by examining the generated datasets, validating data quality, understanding relationships between tables, and preparing the data for exploratory data analysis and machine learning.

## 2. Dataset Loading and Inspection
Loaded the seven datasets generated during Day 1:
- Customers
- Restaurants
- Orders
- Deliveries
- Drivers
- Reviews
- Payments

Used Pandas to inspect the structure of each dataset. Checked the number of rows and columns, column names, data types, and sample records to understand the information available for analysis.

## 3. Data Quality Assessment
Performed initial data quality checks to identify issues that could affect analysis and model performance.

Activities included:
- Checking missing values in each column.
- Identifying duplicate rows and records.
- Examining unique values in important categorical columns.
- Checking whether numerical columns contain unexpected or invalid values.
- Reviewing date and time columns for consistency.

These checks help identify potential data problems before performing detailed analysis.

## 4. Relationship Validation
Examined relationships between the seven datasets using their corresponding identifiers.

Examples include:
- Customer IDs connecting customers with their orders.
- Restaurant IDs connecting restaurants with orders.
- Order IDs connecting orders with deliveries, reviews, and payments.
- Driver IDs connecting deliveries with drivers.

Checked whether the identifiers used to connect datasets were valid and whether unexpected unmatched records existed.

## 5. Data Type and Date-Time Validation
Reviewed data types to ensure that each column could be used correctly during analysis.

Activities included:
- Converting order timestamps into datetime format.
- Checking delivery and preparation time columns.
- Verifying numerical columns such as order amount, delivery distance, and ratings.
- Reviewing categorical columns such as city, restaurant category, weather, traffic, and payment method.

Correct data types are important for time-based analysis, aggregation, visualization, and machine learning.

## 6. Initial Data Preprocessing
Performed initial preparation based on the findings from the data quality checks.

This included reviewing missing and duplicate records, examining inconsistent values, and preparing relevant columns for subsequent analysis.

Any changes to the original data should be validated to ensure that useful information is not lost.

## 7. Initial Exploratory Analysis
Started examining the overall structure and distribution of the Uber Eats data to understand the business context.

Potential areas of investigation included:
- Distribution of orders across cities.
- Order status and order amount patterns.
- Delivery and preparation time distributions.
- Customer and restaurant activity.
- Availability of weather, traffic, and delivery-related features.

These initial observations help identify useful questions for the detailed EDA planned in the following stages.

## 8. Tools and Technologies
- Python
- Pandas
- NumPy
- Jupyter Notebook
- VS Code
- Git and GitHub for version control

## 9. Deliverables
- Inspection of the seven generated datasets.
- Data quality assessment covering missing values and duplicates.
- Validation of relationships between datasets.
- Review of data types and date-time columns.
- Initial data preprocessing and exploratory observations.
- Prepared datasets for detailed EDA and machine learning.

## 10. Outcome
Day 2 focused on understanding the generated Uber Eats datasets, checking their quality and relationships, and preparing them for subsequent analysis. These activities establish a foundation for detailed exploratory data analysis, feature engineering, and delivery-time prediction in the following project stages.

## Next Steps
Continue with detailed exploratory data analysis, investigate factors affecting delivery performance, and prepare relevant features for machine learning model development.
