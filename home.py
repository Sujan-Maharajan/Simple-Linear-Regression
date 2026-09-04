import pandas as pd
import numpy as np

def data_load(linreg_students_csv):
    data = pd.read_csv(linreg_students_csv)
    x = data["hours_studied"].values
    y = data["exam_score"].values

    return x,y

def data_split(x,y):
    total = len(x)
    train_size = int(total*0.7)
    
    x_train = x[:train_size]
    y_train = y[:train_size]

    x_test = x[train_size:]
    y_test = y[train_size:]

    return x_train, y_train, x_test, y_test

def calculation_line(x,y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    upper = np.sum((x-mean_x)*(y-mean_y))
    lower = np.sum((x-mean_x)**2)
    b1 = upper/lower
    b0 = mean_y-b1*mean_x

    return b0,b1

def predict(b0,b1,x):

    return b0+b1*x

def evaluate(y,predictions):
    mean_y = np.mean(y)
    mse = np.mean((y-predictions) **2)
    square_error = np.sum((y-predictions) **2)
    square_total = np.sum((y-mean_y) **2)
    r2 = 1-(square_error/square_total)

    return mse,r2


x, y = data_load("linreg_students.csv")
x_train, y_train, x_test, y_test = data_split(x, y)

print("Training data:", len(x_train)) 
print("Testing data:", len(x_test))

b0, b1 = calculation_line(x_train, y_train)

print("Intercept(b0):", b0)
print("Slope(b1):", b1)

test_predictions = predict(b0, b1, x_test)
mse, r2 = evaluate(y_test, test_predictions)

print("MSE:", mse)
print("R²:", r2)

prediction_7_5 = predict(b0, b1, 7.5)

print("Prediction for 7.5 hours:", prediction_7_5)