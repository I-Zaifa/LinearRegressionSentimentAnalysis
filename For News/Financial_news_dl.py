import requests
import pandas as pd


day = 1
month = 1
year = 2022

api_key = "enter_free_key_from_site"

# Loop through the years
for y in range(0, 2):
    # Loop through months 
    for m in range(1, 13):
        # fiz the 0 issue for moth formatting
        month1 = f"{m:02d}"
        year1 = str(year)
        
        # Define the time range for the entire month
        time_from = f"{year1}{month1}01T0000"
        # Check for the last day of the month
        if m == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = m + 1
            next_year = year
        
        time_to = f"{next_year}{next_month:02d}01T0000"
        
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "NEWS_SENTIMENT",
            "tickers": "MSFT",
            "time_from": time_from,
            "time_to": time_to,
            "sort": "RELEVANCE",
            "apikey": api_key,
            "limit": "1000"
        }

        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200 and 'feed' in data:
            df_news = pd.DataFrame(data['feed'])
            df_news.to_csv(f"financial_news_{year1}_{month1}.csv", index=False)
            print(f"Data for {year1}-{month1} saved to financial_news_{year1}_{month1}.csv")
        else:
            print(f"No data for {year1}-{month1} or error in API call.")

    year -= 1

print("Data fetching complete.")
