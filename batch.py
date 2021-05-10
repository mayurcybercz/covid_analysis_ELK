from textblob import TextBlob
import csv
#exculded the batch twitter data from repository
#download from https://www.kaggle.com/komalkhetlani/tweets-about-covid19-all-over-the-world 
#and add correct path below
tweets = open("historical_batch_data/splitcsv-d3f49214-cda7-478e-a712-f01725b62790-results/TweetsAboutCovid-19-1.csv", 'r',encoding="utf-8")
sntTweets = open("historical_batch_data/generated/sentiment_final.csv", "w",encoding="utf-8")

sentiments_writer = csv.writer(sntTweets, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for row in tweets:
    row_lister=row.split(",")
    if (len(row_lister)>11):
        blob = TextBlob(row_lister[6])
    else:
        continue
    print(blob.sentiment.polarity)
    if (blob.sentiment.polarity > 0):
        sentiments_writer.writerow([row_lister[0], row_lister[1], row_lister[6],row_lister[11], blob.sentiment.polarity, "positive"])
    elif (blob.sentiment.polarity < 0):
        sentiments_writer.writerow([row_lister[0], row_lister[1], row_lister[6],row_lister[11], blob.sentiment.polarity, "negative"])
    elif (blob.sentiment.polarity == 0.0):
        sentiments_writer.writerow([row_lister[0], row_lister[1], row_lister[6],row_lister[11], blob.sentiment.polarity, "neutral"])