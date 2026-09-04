Linear Regression From Scratch

A simple Linear Regression project built from scratch using Python, NumPy, and Pandas.

This project predicts a student's exam score based on the number of hours they studied. Instead of using a machine learning library such as Scikit-learn, the linear regression calculations are implemented manually using mathematical formulas.

Project Overview

The model learns the relationship between:

Input (X): Hours Studied
Output (Y): Exam Score

The project follows the basic machine learning workflow:

Load the dataset
Split the data into training and testing sets
Calculate the regression line
Make predictions
Evaluate the model using MSE and R²
Predict an exam score for a student who studies for 7.5 hours
Technologies Used
Python
Pandas
NumPy
CSV Dataset
Project Structure
linear-regression-from-scratch/
│
├── linreg_students.csv
├── linear_regression.py
└── README.md
How It Works

The regression model finds a line:

y = b0 + b1x

Where:

b0 = Intercept
b1 = Slope
x = Hours studied
y = Predicted exam score

The slope is calculated using:

b1 = Σ((x - mean_x)(y - mean_y)) / Σ((x - mean_x)²)

The intercept is calculated using:

b0 = mean_y - b1 × mean_x
Data Split

The dataset is divided into:

70% Training Data
30% Testing Data

The training data is used to calculate the regression line, while the testing data is used to evaluate how well the model performs on unseen data.

Model Evaluation

The model uses two evaluation metrics:

Mean Squared Error (MSE)

MSE measures the average squared difference between the actual values and predicted values.

MSE = mean((actual - predicted)²)

A lower MSE generally means the predictions are closer to the actual values.

R² Score

R² measures how well the model explains the variation in the target variable.

R² = 1 - (Sum of Squared Errors / Total Sum of Squares)

A value closer to 1 generally indicates a better fit.

Example Prediction

The model can predict an exam score for a student who studies for 7.5 hours:

prediction_7_5 = predict(b0, b1, 7.5)

print("Prediction for 7.5 hours:", prediction_7_5)