import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import glob
import os

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

files_all = "C:\\...\\extracted_financial_news*.csv"
output_file = "Sentiment_Analysis_for_"

### Goes over all the files and does sentiment analysis for each single summary in that file. 
### Gives +,- and neutral scores along with compound scores.

for file_path in glob.glob(files_all):

    df = pd.read_csv(file_path)
    file_name = os.path.basename(file_path)
    # print(file_name)

    output_file_name = output_file + file_name
    # print(output_file_name)
    

    ## Preprocessing the Data
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    def preprocess_text(text):
        tokens = word_tokenize(text)
        tokens = [token.lower() for token in tokens if token.isalpha()]
        tokens = [token for token in tokens if len(token) > 2]
        tokens = [token for token in tokens if token not in stop_words]
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return tokens

    df['Processed Summaries'] = df.iloc[:,0].apply(preprocess_text)

    # print(df['preprocessed_summaries'])


    ## Sentiment Analysis
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(text):
        text= ' '.join(text)
        scores = sia.polarity_scores(text)
        return scores

    df['Sentiment Scores'] = df['Processed Summaries'].apply(analyze_sentiment)
    # print(df['sentiment_scores'])


    ## Interpretation

    df['Compound Score'] = df['Sentiment Scores'].apply(lambda x: x['compound'])
    df.to_csv(f"{output_file_name}.csv",index=False)
    print(df['Compound Score'])

    output_file = "Sentiment_Analysis_for_"
    output_file_name = ''


## Ploting for induvidual files if needed for aid (add it in the loop as required)
# plt.hist(df['compound_score'], bins=20, edgecolor='k')
# plt.title('Sentiment Analysis of Market Summaries')
# plt.xlabel('Compund Sentiment Score')
# plt.ylabel('Frequency')
# plt.show()