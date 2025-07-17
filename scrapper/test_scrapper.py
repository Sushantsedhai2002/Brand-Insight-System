from reddit_scrapper import reddit_scrapper

brand = input("Enter a brand to search")
comments = reddit_scrapper(brand)

for i, comment in enumerate(comments[:20]):
    print(f"{i+1}. @{comment['reddit_username']}: {comment['comment_text'][:200]}")
