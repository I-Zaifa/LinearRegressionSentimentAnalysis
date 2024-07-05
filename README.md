## Description:

A learning project that I did which includes using opening prices along with sentiment analysis done on news headlines for the end of that month for **Microsoft Corp. From Feb-2022 to December-2023**, to predict the closing prices. 

It was done this way because stock data is easily available but recent news data for every day of the month is not so free and the free one is limited.

### This project serves to test and showcase my skills in nlp sentiment analysis (using nltk library), Linear regression model use and interpretation in a theoretical context, and the data preprocessing that is done for it. The data is limited and thus so are the results but that is not my main focus right now.

#### The Stock and News data was taken from https://www.alphavantage.co/ using it's free API (limited use). Sublime Text Editor was used to write the code. (ChatGPT honourable mention?)

## Process:
1. The data is downloaded using the API for both the stock and the news.
2. The stock data is sorted later and the news data is sorted separately to extract only the summaries. The site actually gives the sentiment scores too but that is done manually again later.
3. The sentiment analysis is done on the summaries of the news headlines which include both those related to Microsoft and the stock market in general. My code specified MSFT ticker but overall data was downloaded for some reason (perhaps due to unavailability of further data on Microsoft).
4. NLTK library was used for sentiment analysis. It was done on each summary to provide a positive, negative and neutral sentiment for each summary for each month and in a separate column their compound scores. The summaries and the scores are combined together.
5. Finally the linear regression model is used (from the sci-kit learn library). The stock and sentiment data is combined for coherence. It assumes opening of each month and the sentiment analysis for each month taken at a mean value, for its independent variables. The dependent variable is the closing price of each month which we try to predict. (The train/test split is 80/20)
6. The model is then saved to a pkg file which can be used later for closing price prediction by giving it the sentiment and opening of any month as parameters.

## Results:
The current model has the data for every month for 2 years. It trains on 80% of it and then it is tested on the other 20%. 

Sentiment and Opening prices are the Independent Variables. Closing Price is the Dependent Variable. 

The current model gives the following results:
![tfp](https://github.com/I-Zaifa/LinearRegressionSentimentAnalysis/assets/174838964/2c835bc0-7b08-450d-9744-5c7af9be58cf)

The MSE is very high telling that there is a lot of difference in the actual and predicted values in the test data but the R2 value shows that a lot of the variation (84%) in the model's dependent variable can be explained by the independent variables. (Using other random splits will lead to different results due to the sample size being very small).

## Improvements Required:
1. The main improvement required is the increase in the data of the news headlines and the stock which should be for every day and not just for the month as a whole. More years can be added as long as the news headlines are from reliable sources. (News archives could be used with OCR for text reading from images)
2. The data should also take into consideration items such as the fact that when data is being taken for every day then any news after 5 should be added to the next day as the market closes down. Also that the weekends news should be shifted to be with Monday's news.
3. Other measures should be added to validate the interpretation of the results such as adjusted r2 score and cross-validating the data across numerous random iterations of test/train splits to make sure that the same or near the same results still hold.
4. **This would have been a perfect project, one I would have worked a lot more on but could not due to the limited availability of the news related data.** (Webscraping is a different skill; one I plan to improve in the near future) 
