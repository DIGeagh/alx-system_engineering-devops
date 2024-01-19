#!/usr/bin/python3
"""
0-main
"""
import sys
from 0-subs import number_of_subscribers

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)
        print("{:d}".format(subscribers_count))
