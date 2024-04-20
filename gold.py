import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.model_selection import cross_val_score

from google.colab import drive
drive.mount('/content/drive')

gold_data = pd.read_csv('/content/drive/MyDrive/dataset/gold/Gold.csv')

desired_columns = ['open', 'high', 'low', 'close',]
df = gold_data[desired_columns]
print(df)

df.info()

df.describe()

ma_1000_days = df.close.rolling(1000).mean()

plt.figure(figsize=(8,6))
plt.plot(ma_1000_days, 'r')
plt.plot(df.close, 'g')
plt.show()

target = df['close']
target

df.isnull().sum()

df.shape
X = df.drop(columns=['close'])  # Features (all columns except 'close')
Y = df['close']  # Target variable ('close' column)

# Spliting the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# test_size=0.2 means 20% of the data will be used for testing, adjust as needed
# random_state=42 is used for reproducibility, you can change this or omit it
print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of y_train:", Y_train.shape)
print("Shape of y_test:", Y_test.shape)

regressor = RandomForestRegressor(n_estimators=100)

regressor.fit(X_train,Y_train)

test_data_prediction = regressor.predict(X_test)

error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared error : ", error_score)

Y_test = list(Y_test)

plt.plot(Y_test, color='blue', label = 'Actual Value')
plt.plot(test_data_prediction, color='green', label='Predicted Value')
plt.title('Actual Price vs Predicted Price')
plt.xlabel('Number of values')
plt.ylabel('GLD Price')
plt.legend()
plt.show()

# Perform k-fold cross-validation
cv_scores = cross_val_score(regressor, X_train, Y_train, cv=5)

# Calculate the mean and standard deviation of the cross-validation scores
print("Mean CV Score:", np.mean(cv_scores))
print("Standard Deviation of CV Scores:", np.std(cv_scores))

df[['open', 'high', 'low', 'close',]].plot(kind='box')

def calculate_up_probability(model, data):
    # Make predictions for the entire dataset
    predicted_prices = model.predict(data)

    # Calculate the difference between consecutive days' prices
    price_diff = np.diff(predicted_prices)

    # Count the number of times the price increased
    num_up_days = np.sum(price_diff > 0)

    # Calculate the total number of days
    total_days = len(price_diff)

    # Calculate the probability of the price going up the next day
    up_probability = num_up_days / total_days

    return up_probability

# Train the model using all available data
regressor.fit(X, Y)

# Calculate the probability of the price going up the next day
up_probability = calculate_up_probability(regressor, X)

print("Probability of the price going up the next day:", up_probability)

import plotly.graph_objs as go

# Define layout for the plot
layout = go.Layout(
    title='Actual vs. Predicted Gold Prices',  # Title of the plot
    xaxis=dict(
        title='Date',  # Title for the x-axis
        titlefont=dict(  # Font properties for the x-axis title
            family='Courier New, monospace',  # Font family
            size=18,  # Font size
            color='#7f7f7f'  # Font color (hex code)
        )
    ),
    yaxis=dict(
        title='Gold Price',  # Title for the y-axis
        titlefont=dict(  # Font properties for the y-axis title
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)

# Data for the plot
actual_data = go.Scatter(x=df.index, y=df['close'], mode='lines', name='Gold Price', line=dict(color='blue'))
#predicted_data = go.Scatter(x=df.index, y=test_data_prediction, mode='lines', name='Predicted Price', line=dict(color='green'))

# Creating the plot
plot = go.Figure(data=[actual_data, predicted_data], layout=layout)

# Show the plot
plot.show()

