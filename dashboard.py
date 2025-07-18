import streamlit as st 
import pandas as pd
from config import get_connection
from 

st.set_page_config(page_title='Brand Insight Dashboard', layout='wide')
st.title("Brand Sentiment Insights")

search_query = st.text_input("Enter a Brand or movie, .., etc")
if st.button('Search'):
  if search_query.strip() != '':
    pass
    

def load_data():
  conn = get_connection()
  df = pd.read_sql("SELECT * FROM brand_insights ORDER BY created_at DESC", conn)
  conn.close()
  return df

df = load_data()
# st.write("Available columns:", df.columns.tolist())


brands = df['brand_name'].unique()
selected_brand = st.sidebar.selectbox("Select Brand", brands)

filtered_df = df[df['brand_name'] == selected_brand]

col1, col2,col3 = st.columns(3)


st.subheader("Sample Comments")
st.dataframe(filtered_df[['reddit_username', 'comment_text', 'sentiment']].head(10))

st.subheader("Sentiment Distribution")
sentiment_counts = filtered_df['sentiment'].value_counts()
st.bar_chart(sentiment_counts)