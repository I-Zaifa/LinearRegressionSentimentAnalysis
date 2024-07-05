import glob
import os
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib


all_sentiment_files = 'C:\\....\\Sentiment*.csv' # Enter the path to the files on your PC
stock_file = pd.read_csv('C:\\...\\MSFT_monthly.csv')

# stock_data['Date'] = pd.to_datetime(stock_file['Date'])
# print(stock_data)

sentiment_summary = []

## Calculated the mean of each 50 + summaries from a file.
def calculate_mean_for_sentiment(file):
    sentiment_data = pd.read_csv(file)
    mean_sentiment = sentiment_data['Compound Score'].mean().round(2)
    return mean_sentiment

## Prepares a new list with the new mean added to the right Date. 
for file in glob.glob(all_sentiment_files):
    year_month = file.split('_')[6:8]
    year = year_month[0]
    month = year_month[1].split('.')[0]
    if month[0] == '0':
        month = month[1]
    year_month = month + '/' + '1' + '/' + year
    # print(year_month)

    mean_sentiment = calculate_mean_for_sentiment(file)
    sentiment_summary.append({"Date": year_month, 'Sentiment' : mean_sentiment})


sentiment_data = pd.DataFrame(sentiment_summary)
# print(sentiment_data)

merged_data = pd.merge(stock_file, sentiment_data, on="Date") #Merges based on similar column.

# print(merged_data)

X = merged_data[['Sentiment', 'Open']]
y = merged_data['Close']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
## Different states will produce different results. This ensures that the results stay the same everytime with the same random splits.

model = LinearRegression()
model.fit(X_train, y_train)

y_predicted = model.predict(X_test)

mean_squared_error = mean_squared_error(y_test, y_predicted)
r2 = r2_score(y_test, y_predicted)

print(f'Mean Squared Error: {mean_squared_error}') # 135.12
print(f'R-Squared: {r2}') # 0.84

new_data = pd.DataFrame({'Sentiment': [0.5], 'Open': [150.0]})
prediction = model.predict(new_data)

print("Predicted Closing Price:", prediction)

## Make a package of the Model and saves it to a file which can be used later by importing it and using it as showed right above.
filename_for_model = 'Linear_Regression_Model.pkl'
joblib.dump(model, filename_for_model)

