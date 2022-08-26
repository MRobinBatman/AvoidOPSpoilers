# -*- coding: utf-8 -*-
import praw
import datetime

import configparser

#Credentials
config = configparser.ConfigParser()
config.read('config.ini')
ua = config['reddit']['user_agent']
cl_id = config['reddit']['client_id']
cl_sec = config['reddit']['client_secret']
user = config['reddit']['username']
passw = config['reddit']['password']


#Reddit Sign-in
reddit = praw.Reddit(user_agent= ua,
                     client_id= cl_id,
                     client_secret= cl_sec,
                     username= user,
                     password= passw)

start_date = ""
stop_date =""

def get_dates():   
    time_frame = []
    f = open("dates.txt", "r")
    count = 0
    for line in f:
        # print(line)
        if count == 0:
            start_date = line
            time_frame.append(start_date.rstrip())
        else:
            stop_date = line
            time_frame.append(stop_date)
    return time_frame

def sub_or_unsub(sub):
    
    #Get timeframe from dates.txt
    time_frame = get_dates()
    
    #Subreddit Selection
    subreddit = reddit.subreddit(sub)
    
    
    #Getting the date
    today = datetime.datetime.now()
    
    
    # Uncomment the below line to get the date as mm/dd/yy
    # today = today.strftime("%x")
    
    # Uncomment the below line to get the data as just the 'Mon' style abbreviation
    # today = today.strftime("%a")
    
    today = today.strftime("%a %x")
    
    
    #Subscribing on Friday and unsubscribing on Tuesday
    if today == time_frame[0]:
        subreddit.unsubscribe()
        print("Unsubbed")
    elif today == time_frame[1]:
        subreddit.subscribe()
        print("Subbed")
        

for line in open("subreddits.txt"):
    sub_or_unsub(line)
