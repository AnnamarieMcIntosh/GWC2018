#import tweepy
import tweepy
import time
# Keys and Access Tokens
CONSUMER_KEY    = 'TruiCyGO8mLoNjwAXVmgymGy4'
CONSUMER_SECRET = 'iEAtMTCjIirTMO4tm2Jiyg2CE0F1P07cVPhnT8toMJFSm8NouO'

ACCESS_TOKEN    = '1017154656831590400-RUrOPtvOeWJcmEGPWHuQDe1qP0gKUI'
ACCESS_SECRET   = 'IYIsXU7GgsLFiq11DrZik83JRNQPMqONwbpUIQrfEktXG'

loop = 0
# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api  = tweepy.API(auth)

# Update Status
api.update_status("Hey @gtloveit , yeet")

# while loop <7
#     api.update_status("Hey @gtloveit , yeet" + str(loop))
#     loop += 1
#     time.sleep(30)
