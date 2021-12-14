#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 09:32:40 2021

@author: shining
"""

import tweepy
import time
import requests
import time

# twitter developer app authentication info
api_key = "xg0ZnYOWTTCXpxtSG8qPT02aT"
api_key_secret = "HltHFDAvqQwUl5AP2y90qXMDppQX02SeEPwOSt4DYBGJxo3a28"
access_token = "1445459910360064002-MtwfNthg4loMM1wubslDclJUQwnejV"
access_token_secret = "Am4DpOyt3eBNMvFTKLDGEPpBdv8g4QUVoVvEWmpvePBTg"

#Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Verify the credentials to make sure it works
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Define a reply functon that can respond to tweets depending on the content
def reply_to_tweets():
    # starting retrieving process
    print('retrieving and replying to tweets...', flush=True)
    # serach all mention tweets and start analyzing them one by one in reverse order
    mentions = api.mentions_timeline()
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.text, flush=True)
        
        #recognize 'hello' and respond 'hello back to you' if not already done so
        if 'hello!' in mention.text.lower():
            print('found hello', flush=True)
            try:
                api.update_status(status = '@' + mention.user.screen_name + 
                                  ' Hello back to you!', in_reply_to_status_id = mention.id)
                print('responded to hello')
            except tweepy.errors.Forbidden:
                print('Already responded')
        
        # recognize 'help!' or 'info!' message and provide instructions if not already done so
        if ('help!' or 'info!') in mention.text.lower():
            print ('found help request', flush = True)
            try:
                api.update_status(status = '@' + mention.user.screen_name + 
                                  ' Please refer to XXX', in_reply_to_status_id = mention.id)
                print('responded to help')
            except tweepy.errors.Forbidden:
                print('Already responded')
        
        # the last two cases: a valid stock price ticker or unsupported message
        else:
            # define access to Yahoo API
            stock = mention.text.split(' ')[1].upper()
            apikey='S3WcV2Penj7CcWmgrznW71Wxe5xUYGWaEAcBht99'
            url = "https://yfapi.net/v6/finance/quote"
            querystring = {"symbols":stock}
            headers = {
              'x-api-key': apikey
                }
            
            # obtain stock information (similar to code used in quiz 2)
            try:
                response = requests.request("GET", url, headers=headers, params=querystring)
                response.raise_for_status()
                
                stock_json = response.json()
                Comp_Name = stock_json['quoteResponse']['result'][0]["shortName"]
                Comp_Name = Comp_Name.replace(',',' ')
                Price = str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"])
                Time_raw = stock_json['quoteResponse']['result'][0]["regularMarketTime"]
                Time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(Time_raw))

                print("Pulling data for:" + stock)
                reply_text = ' '+ Comp_Name + ', ' + str(Time) + ', ' + Price
                
                # recognize stock ticker and respond with price and time if not already done so
                try:
                    api.update_status(status = '@' + mention.user.screen_name + 
                                      reply_text, in_reply_to_status_id = mention.id)
                    print('responded to price check')
                except tweepy.errors.Forbidden:
                    print('Already responded')
            except KeyError:
                print('found unknown input')              
                try:
                    api.update_status(status = '@' + mention.user.screen_name + 
                                      ' Sorry I do not understand', in_reply_to_status_id = mention.id)
                    print('responded to unknown input')
                except tweepy.errors.Forbidden:
                    print('Already responded')
            
            # last scenario: respond to unsupported tweet content if not already done so
            except IndexError:
                print('found unknown input')
                try:
                    api.update_status(status = '@' + mention.user.screen_name + 
                                      ' Sorry I do not understand', in_reply_to_status_id = mention.id)
                    print('responded to unknown input')
                except tweepy.errors.Forbidden:
                    print('Already responded')


# refresh every 30 seconds to check                
while True:
    reply_to_tweets()
    time.sleep(30)
