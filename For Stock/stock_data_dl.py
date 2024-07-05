import requests
import pandas as pd

# API request for Microsoft (MSFT) daily stock data
url = "https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "MSFT",
    "apikey": "enter_free_key_from_site",
    "outputsize": "full"  
}

response = requests.get(url, params=params)
data = response.json()
# print(data)

df_msft = pd.DataFrame(data["Time Series (Daily)"]).transpose()

df_msft.to_csv("msft_stock_data.csv")

# print(df_msft)