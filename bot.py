
# -*- coding: utf-8 -*-


import tweepy, time, sys, random

#argfile = str(sys.argv[1])

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_KEY = ''
ACCESS_SECRET = ''


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
if ACCESS_KEY:
        
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET) #used for access keys
    api = tweepy.API(auth)

else:           ##This block will send the user to an auth link and ask to verify
    ##Authenication dance for users
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print("Error! Failed to get request token.")

    #session.set('request_token', auth.request_token)

    print(redirect_url)

    verifier = input('Verifier: ')      #prompts the user to enter verification code

    #token = session.get('request_token')
    #session.delete('request_token')
    #auth.request_token = token

    #auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print("Error! Failed to get access token.")

    #auth.set_access_token(key, secret)

    print("Access Token: " + auth.access_token)
    print("Access Token Secret: " + auth.access_token_secret)

    api = tweepy.API(auth)

#api.update_status(status='Firing up')

while True:
    random.seed()
    num = random.randint(1, 10)
    if num == 3:
        api.update_status(status='3!!!!!!!')
        #print("3!!!!!!!")
    else:
        api.update_status(status=num)
        #print(num)
    time.sleep(60)








"""
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(status = line)
    time.sleep(900) #tweet every fifteen minutes
    """


