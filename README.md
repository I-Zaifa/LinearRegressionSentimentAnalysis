## Description:

A learning project that I did which includes using opening prices along with sentiment analysis done on news headlines for the end of that month, to predict the closing prices. 

It was done this way because stock data is easily available but recent news data for every day of the month is not so free and the free one is limited.

### This project serves to test and showcase my skills in nlp sentiment analysis (using nltk library), Linear regression model use and interpretation in a theoretical context, and data preprocessing that is done for it. The data is limited and thus so are the results but that is not the main focus.

#### The Stock and News data was taken from https://www.alphavantage.co/ using it's free API (limited use).

## Process:
1. The data is downloaded using the API for both the stock and the news.
2. The stock data is sorted later and the news data is sorted seperately to extract only the summaries. The site acutally gives the sentiment scores too but that is done manually again later.
3. The sentiment analysis is done on the summaries of the news headlines which include both those related to microsoft and the stock market in general. My code specified MSFT ticker but overall data was downloaded for some reason (perhaps due to unavailability of further data on microsoft).
4. NLTK library was used for sentiment analysis. It was sdone on each summary to provide a psitive, negative and neutral sentiment for each summary for each month and in a seperate column their compound scores. The summaries and the scores are combined together.
5. Finally the linear regression model is used (from the scikit learn library). The stock and sentiment data is combined for coherance. It assumes opening of each month and the sentiment analysis for each month taken at a mean value, for its independant variables. The dependant variable is the closing price of each month which we try to predict.
6. The model is then saved to a pkg file which can be used later for closing price prediction by giving it the sentiment and opening of any month as parameters.

## Results:
