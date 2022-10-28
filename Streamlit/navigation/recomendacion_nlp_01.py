import re
import warnings
import requests
import streamlit as st
import pandas as pd
warnings.filterwarnings('ignore')
from functions import paginator


def pageII():
    columns = st.columns((8,2,2))
    columns[1].image("img/skaivuinsightslogo.png", width = 350)
    columns[0].title("🤖 Recommendation System")

    category = st.sidebar.selectbox("Category", (
    "Amazon_Instant_Video", "Beauty", "Books", "CDs_Vinyls", "Cellphones_Accessories", 
    "Clothing_Shoes_Jewelry", "Electronics", "Health_And_Personal", "Home_And_Kitchen", 
    "Movies_And_TV", "Pet_Supplies", "Sports_And_Outdoors"
    ))

    df = pd.read_csv(f"Streamlit/datasets/results/{category}_results.csv")
    df_products = pd.read_csv(f'Streamlit/datasets/products/{category}_products.csv')

    df_recommendations = df[['user_index', 'recommended_products', 'recommend_top_items', 'reviewerID']].drop_duplicates()
    df_recommendations.set_index(keys='user_index', drop=True, inplace=True)

    # Ingresamos el 'user_index' y el 'num_recommendations' para el usuario
    users = df_recommendations.index

    user = st.sidebar.selectbox(
        'User', users)

    reviews = df[['asinID', 'title', 'reviewText', 'overall', 'imUrl']].where(df['user_index'] == user).dropna().reset_index(drop=True)
    
    reviews_count = len(reviews)

    st.subheader(f"User {user} reviewed {reviews_count} products from {category}")

    pages = reviews['asinID'].to_list()

    with st.expander(label="Show reviews"):
        for i, page in paginator("Select a review page", pages, on_sidebar=False):
            col1, col2 = st.columns([1,1])
            col1.write('%s. **%s**' % (i, reviews.iloc[i]['title']))
            col1.image(reviews.iloc[i]['imUrl'], width=130)
            col2.metric("Rating", reviews.iloc[i]['overall'])
            col2.text_area('Review', reviews.iloc[i]['reviewText'], disabled=True)

    st.subheader(f"This user was recommended these products:")

    products = re.findall(r"(?<=\['| ')(.*?)(?=',|'\])", df_recommendations.iloc[user]['recommended_products'])

    with st.expander(label="Show recommendations"):
        col1, col2 = st.columns(2)
        for i in range(5):
            title1 = df_products['title'].where(df_products['asinID'] == products[i]).dropna().reset_index(drop=True)[0]
            col1.subheader(title1)
            url1 = 'https://www.amazon.com/s?k=' + products[i]
            col1.markdown(f"ID: {products[i]} - [Search in Amazon]({url1})")
            image1 = df_products['imUrl'].where(df_products['asinID'] == products[i]).dropna().reset_index(drop=True)[0]
            col1.image(image1, width=110)
            title2 = df_products['title'].where(df_products['asinID'] == products[i+5]).dropna().reset_index(drop=True)[0]
            col2.subheader(title2)
            url2 = 'https://www.amazon.com/s?k=' + products[i+5]
            col2.markdown(f"ID: {products[i+5]} - [Search in Amazon]({url2})")
            image2 = image1 = df_products['imUrl'].where(df_products['asinID'] == products[i+5]).dropna().reset_index(drop=True)[0]
            col2.image(image2, width=110)
