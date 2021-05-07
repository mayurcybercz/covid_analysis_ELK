from tweepy import OAuthHandler
from tweepy import Stream

import sys

# Import twitter keys and tokens
from my_config import consumer_key
from my_config import consumer_secret
from my_config import access_token
from my_config import access_token_secret


# Import listener
from tools.tweet_listener import TweetStreamListener

def main():
    """Pipelines"""

    # Obtain the input topics of your interests
    topics = []
    if len(sys.argv) == 1:
        # Default topics
        topics = ['#covid', '#corona', '#SARS','#vaccination','#Pfizer'
                  'covid', 'corona', 'SARS','vaccination','Pfizer']
    else:
        for topic in sys.argv[1:]:
            topics.append(topic)
    
    
    index = "covid-analysis-elk"
    doc_type = "new-tweet"

    print("==> Topics", topics)
    print("==> Index: {}, doc type: {}".format(index, doc_type))
    print("==> Start retrieving tweets...")

    # Create instance of the tweepy tweet stream listener
    listener = TweetStreamListener(
                        index,
                        doc_type)

    # Set twitter keys/tokens
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Set the program to restart automatically in case of errors
    while True:
        try:
            # Search twitter for topics of your interests
            stream = Stream(auth, listener)
            stream.filter(track=topics)
        except KeyboardInterrupt:
            # To stop the program
            stream.disconnect()
            print("==> Stop")
            break
        except:
            continue

if __name__ == '__main__':
    main()