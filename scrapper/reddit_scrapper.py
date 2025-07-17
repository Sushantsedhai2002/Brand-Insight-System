import praw
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

def reddit_scrapper(brand_name, limit = 20):
  reddit = praw.Reddit(
    client_id = REDDIT_CLIENT_ID,
    client_secret = REDDIT_CLIENT_SECRET,
    user_agent = REDDIT_USER_AGENT
  )
  comments = []

  for submission in reddit.subreddit('all').search(brand_name, sort = 'relevance', limit = limit):
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list()[:10]:
      if comment.body == "[delted]" or comment.body == "[removed]":
        continue
      if len(comment.body) < 10:
        continue
      bad_words = ['http://', 'https://', 'buy now', 'click here', 'NSFW']
      if any(word in comment.body.lower() for word in bad_words):
        continue
      comments.append({
        'brand_name': brand_name,
        'reddit_username': comment.author.name if comment.author else 'unknown',
        'comment_text' : comment.body
      })

  return comments