#import tweepy
import tweepy
import time
# Keys and Access Tokens
CONSUMER_KEY    = 'IMYe8NtwehxoeC2oHv4jO4Qs0'
CONSUMER_SECRET = 'mwiwBQXo0KODagSjeEn5EddBIVzYe8rsNpsXEuGd3qWpOjNNZ0'

ACCESS_TOKEN    = '	761342792815616000-vaJEBVEV5mRa0C8XgBT6Mp2FE8ahqpr'
ACCESS_SECRET   = '3qI6CMjMnDle9bghbwFBQzlccqXjKdzt0aR3cNV2DFcGU'

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api  = tweepy.API(auth)
