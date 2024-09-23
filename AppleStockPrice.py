# Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
from keras import Input
from keras.models import Sequential
from keras.layers import Dense, LSTM

sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")



df_asp = pd.read_csv('AppleStockPrice.csv')


df_asp['Date'] = pd.to_datetime(df_asp['Date'], dayfirst=True)
df_asp.set_index('Date', inplace=True)

print(df_asp)



print(df_asp.describe())


print(df_asp.info())

# 1. Plotting the Closing Price
plt.figure(figsize=(15, 10))
df_asp['Adj Close'].plot()
plt.ylabel('Close Price')
plt.xlabel('Date')
plt.title("Closing Price of AAPL")
plt.tight_layout()
plt.show()


# 2. Plotting the Sales Volume
plt.figure(figsize=(15, 10))
df_asp['Volume'].plot()
plt.ylabel('Volume')
plt.xlabel('Date')
plt.title("Sales Volume of AAPL")
plt.tight_layout()
plt.show()


# 3. Calculate Moving Averages (10, 20, 50 days)
ma_days = [10, 20, 50]
for ma in ma_days:
    df_asp[f"MA for {ma} days"] = df_asp['Adj Close'].rolling(ma).mean()
    
# Plot the Moving Averages with Adjusted Close Price
plt.figure()
df_asp[['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']].plot()
plt.title('APPLE Adjusted Close Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.tight_layout()
plt.show()


# 4. Calculate Daily Return
df_asp['Daily Return'] = df_asp['Adj Close'].pct_change()

# Plot the Daily Return
plt.figure(figsize=(15, 10))
df_asp['Daily Return'].plot(legend=True, linestyle='--', marker='o')
plt.title('APPLE Daily Return')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.tight_layout()
plt.show()


# 5. Histogram of Daily Returns
plt.figure(figsize=(12, 9))
df_asp['Daily Return'].hist(bins=50)
plt.xlabel('Daily Return')
plt.ylabel('Counts')
plt.title('Apple Daily Return Distribution')
plt.tight_layout()
plt.show()


# Grab all the closing prices for the tech stock list into one DataFrame
closing_df = df_asp['Adj Close']

# Make a new tech returns DataFrame
tech_rets = closing_df.pct_change()
tech_rets.head()


# 6. Predicting Closing Price Using LSTM

# Filter only 'Close' price
data = df_asp.filter(['Close'])
dataset = data.values

# Split data into training and test sets (95% training)
training_data_len = int(np.ceil(len(dataset) * 0.95))

# Scale the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

# Create training data
train_data = scaled_data[0:int(training_data_len), :]
x_train = []
y_train = []

for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])

# Convert training data to numpy arrays
x_train, y_train = np.array(x_train), np.array(y_train)

# Reshape the data
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
# Build the LSTM model
model = Sequential()

# Use an Input layer to specify the shape of the input data
model.add(Input(shape=(x_train.shape[1], 1)))

# Add LSTM layers
model.add(LSTM(128, return_sequences=True))
model.add(LSTM(64, return_sequences=False))

# Add Dense layers
model.add(Dense(25))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, batch_size=1, epochs=1)



# Create test data
test_data = scaled_data[training_data_len - 60:, :]
x_test = []
y_test = dataset[training_data_len:, :]

for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i, 0])
    
# Convert test data to numpy arrays and reshape
x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
# Get model predictions and invert scaling
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

# Calculate RMSE
rmse = np.sqrt(np.mean(((predictions - y_test) ** 2)))
print(f'RMSE: {rmse}')



# 7. Plotting Predictions vs Actual Prices

# Create dataframes for train, validation, and predictions
train = data[:training_data_len]
valid = data[training_data_len:].copy()
valid.loc[:, 'Predictions'] = predictions

# Plot the data
plt.figure(figsize=(16, 6))
plt.title('Model Prediction vs Actual Price')
plt.plot(train['Close'], label='Train')
plt.plot(valid[['Close', 'Predictions']], label=['Valid', 'Predictions'])
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.legend(loc='lower right')
plt.show()



# Display the validation and predictions
print(valid)