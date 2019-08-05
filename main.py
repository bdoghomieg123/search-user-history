import praw
import time
import os
import re
from common import clear
from praw.models import Comment



reddit=praw.Reddit('bot1')

username_of_redditor = input("What reddit user would you like to use this program on?")
phrase_to_lookup = input("What would you like to look for in this person's post history?")
clear()
print("Program checking user's history...")

def check_submissions():
    global times_said_in_posts
    times_said_in_posts = 0
    for submission in reddit.redditor(username_of_redditor).submissions.new(limit=None):
        if re.search(phrase_to_lookup ,submission.selftext, re.IGNORECASE):
            times_said_in_posts += 1
            if re.search(phrase_to_lookup ,submission.title, re.IGNORECASE):
                times_said_in_posts += 1

def check_comments():
    global times_said_in_comments
    times_said_in_comments = 0
    for comment in reddit.redditor(username_of_redditor).comments.new(limit=None):
        if re.search(phrase_to_lookup ,comment.body, re.IGNORECASE):
            times_said_in_comments += 1

check_submissions()
check_comments()
clear()

print(username_of_redditor,"said",phrase_to_lookup, times_said_in_posts,"time(s) in posts.\n")
print(username_of_redditor,"said",phrase_to_lookup, times_said_in_comments,"time(s) in comments.\n")
