#!/usr/bin/python3
"""
100-count
"""
import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    if count_dict is None:
        count_dict = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'MyBot/1.0'}

    params = {'limit': 100, 'after': after}
    
    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title:
                        if word in count_dict:
                            count_dict[word] += 1
                        else:
                            count_dict[word] = 1

            after = data['data']['after']
            if after is not None:
                return count_words(subreddit, word_list, after, count_dict)
            else:
                # Sort the results in descending order by count and then alphabetically
                sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_count:
                    print(f"{word}: {count}")
        else:
            return

    except Exception:
        return

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = [x for x in sys.argv[2].split()]
        count_words(subreddit, keywords)
