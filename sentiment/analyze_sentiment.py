from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sentiment.slang_normalizer import normalize_slang

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
  cleaned = normalize_slang(text)
  score = analyzer.polarity_scores(text)['compound']

  if score >= 0.05:
    return 'Positive'
  elif score <= -0.05:
    return "Negative"
  else:
    return "Neutral"
  

# print(get_sentiment("Buda le chatxan ekdam"))