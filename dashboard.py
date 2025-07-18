import streamlit as st
import pandas as pd
from config import get_connection
from scrapper.reddit_scrapper import reddit_scrapper
from database.db import insert_comment
from main import main
from gemini import get_brand_sentiment_summary

st.set_page_config(page_title='Brand Insight Dashboard', layout='wide')
st.title("Brand Sentiment Insights")

def load_data():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM brand_insights ORDER BY created_at DESC", conn)
    conn.close()
    return df

df = load_data()


brands = df['brand_name'].unique()
selected_brand = st.sidebar.selectbox("Select Brand", brands)

filtered_df = df[df['brand_name'].str.strip().str.lower() == selected_brand.strip().lower()]

col1, col2, col3 = st.columns(3)

search_query = st.text_input("Enter a Brand, Movie, etc.")
if st.button('Search'):
    if search_query.strip() != '':
        with st.spinner("Scraping Reddit Comments..."):
            main(search_query.strip())
            st.success(f"Scraped and stored comments for '{search_query}'")
            df = load_data()
            filtered_df = df[df['brand_name'].str.strip().str.lower() == search_query.strip().lower()]
            selected_brand = search_query  
    else:
        st.warning("Please enter a search query.")


all_comments = "\n".join(filtered_df['comment_text'].dropna().tolist())
if all_comments.strip():
    with st.spinner("Analyzing sentiment with Gemini..."):
        summary_text = get_brand_sentiment_summary(selected_brand, all_comments)
        st.subheader("Gemini Sentiment Summary")
        st.text(summary_text)
else:
    st.warning("No comments available for this brand.")

st.subheader("Sample Comments")
if not filtered_df.empty:
    st.dataframe(filtered_df[['reddit_username', 'comment_text']].head(10))
    # st.dataframe(filtered_df[['reddit_username', 'comment_text', 'sentiment']].head(10))

else:
    st.warning("No comments found for the selected brand.")

st.subheader(" Sample Sentiment Distribution (ROUGH CALCULATION BASED ON SMALL SAMPLE SIZE)")
sentiment_counts = filtered_df['sentiment'].value_counts()
st.bar_chart(sentiment_counts)

