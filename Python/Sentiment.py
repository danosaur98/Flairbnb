import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from operator import itemgetter
import math

df = pd.read_csv("neighbourhoods.csv", low_memory=False)
neighborhood_sentiment = {x: [] for x in list(df['neighbourhood'])}
neighborhood_positive_reviews = {x: 0 for x in list(df['neighbourhood'])}

df = pd.read_csv("reviews.csv", low_memory=False)
review_id = list(df['listing_id'])
review_text = list(df['comments'])
reviews_dictionary = dict(zip(review_text, review_id))

df = pd.read_csv("listings.csv", low_memory=False)
listing_id = list(df['id'])
listing_neighborhood = list(df['neighbourhood_cleansed'])
listings_dictionary = dict(zip(listing_id, listing_neighborhood))

sid = SentimentIntensityAnalyzer()
for review in review_text:
    review_str = str(review)
    ss = sid.polarity_scores(review_str)
    try:
        neighborhood_sentiment[listings_dictionary[reviews_dictionary[review]]].append(ss['compound'])
        if ss['compound'] > 0:
            neighborhood_positive_reviews[listings_dictionary[reviews_dictionary[review]]] = \
                neighborhood_positive_reviews[listings_dictionary[reviews_dictionary[review]]] + 1
    except KeyError as e:
        continue

sentiment_analysis = {}
for n in neighborhood_sentiment:
    sentiment_analysis[n] = sum(neighborhood_sentiment[n]) / len(neighborhood_sentiment[n])

positive_reviews = {}
for n in neighborhood_positive_reviews:
    positive_reviews[n] = float(neighborhood_positive_reviews[n]) / len(neighborhood_sentiment[n])

for k, v in sorted(sentiment_analysis.items(), key=itemgetter(1)):
    print(k, ": ", v)
for k, v in sorted(positive_reviews.items(), key=itemgetter(1)):
    print(k, ": ", v)
# for l in sorted(sentiment_analysis):
#    print(l, sentiment_analysis[l])
# for l in sorted(positive_reviews):
#    print(l, positive_reviews[l])
