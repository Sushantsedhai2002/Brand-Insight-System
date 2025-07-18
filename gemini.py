
import os
import google.generativeai as genai

genai.configure(api_key='AIzaSyBnd03haKIynOXiSP7b6Tc7NxPrr1hPN2g')


def get_brand_sentiment_summary(brand_name, comments):
    prompt_text = f"""
You are an analyst. The following text contains user comments about {brand_name}. Please:
1. Summarize the **overall sentiment** expressed in these comments (as "Positive", "Neutral", or "Negative"). You can ignore any comments that are vague, spammy, or unrealted
2. Identify the **one main positive aspect** mentioned frequently (keep it a single line with few words).
3. Identify the **one main negative aspect or criticism** mentioned (keep it a single line with few words).
4. Provide one actionable **suggestion** that the brand could adopt to improve its public perception, such as a strategy or marketing idea..


Comments:
{comments}
"""
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt_text)
    return response.text.strip()