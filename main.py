from scrapper.reddit_scrapper import reddit_scrapper
from sentiment.analyze_sentiment import get_sentiment
from database.db import insert_comment

def main():
    brand = input("🔍 Enter a brand to analyze: ").strip()

    print(f"\n📡 Scraping Reddit for '{brand}'...")
    comments = reddit_scrapper(brand)

    if not comments:
        print("⚠️ No comments found.")
        return

    print(f"🧠 Analyzing {len(comments)} comments...\n")

    for i, comment in enumerate(comments):
        text = comment['comment_text']
        username = comment['reddit_username']
        sentiment = get_sentiment(text)

        insert_comment(brand, username, text, sentiment)

        # print(f"{i+1:02d}. @{username}: [{sentiment}] → {text[:80] if text else 'No text'}")
        

    print(f"\n✅ Done! {len(comments)} comments inserted into database.")

if __name__ == "__main__":
    main()
