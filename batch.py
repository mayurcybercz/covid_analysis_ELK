from textblob import TextBlob
import csv
#exculded the batch twitter data from repository
#download from https://www.kaggle.com/komalkhetlani/tweets-about-covid19-all-over-the-world 
#and add correct path below
tweets = open("historical_batch_data/splitcsv-d3f49214-cda7-478e-a712-f01725b62790-results/TweetsAboutCovid-19-1.csv", 'r',encoding="utf-8")
sntTweets = open("historical_batch_data/generated/test2.csv", "w",encoding="utf-8")

sentiments_writer = csv.writer(sntTweets, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

for row in tweets:
    row_lister=row.split(",")
    if (len(row_lister)>7):
        blob = TextBlob(row_lister[6])
    else:
        continue
    print(blob.sentiment.polarity)
    #remove quotes at start and end
    temp_id=row_lister[0].strip('\"')
    temp_timestamp=row_lister[1].strip('\"')
    temp_tweet=row_lister[6].strip('\"')
   

    if (blob.sentiment.polarity > 0):
        sentiments_writer.writerow([temp_id, temp_timestamp, temp_tweet, blob.sentiment.polarity, "positive"])
    elif (blob.sentiment.polarity < 0):
        sentiments_writer.writerow([temp_id, temp_timestamp, temp_tweet, blob.sentiment.polarity, "negative"])
    elif (blob.sentiment.polarity == 0.0):
        sentiments_writer.writerow([temp_id, temp_timestamp, temp_tweet, blob.sentiment.polarity, "neutral"])