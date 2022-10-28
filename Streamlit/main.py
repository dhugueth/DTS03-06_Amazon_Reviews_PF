import streamlit as st
from navigation import landing, recomendacion_nlp_01, analisis_sentimientos

# Streamlit Pages
st.set_page_config(layout = 'wide', page_icon = "🤖", page_title='Skaivu Insights')
st.sidebar.image("https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/z3ahdkytzwi1jxlpazje",
width=50)

pages = {
    'Main Page': landing.pageI,
    'Recommendation System': recomendacion_nlp_01.pageII,
    'Sentiment Analysis': analisis_sentimientos.pageIII
}

selected_pages = st.sidebar.radio("Navigation", pages.keys())
pages[selected_pages]()
