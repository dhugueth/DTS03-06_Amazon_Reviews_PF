import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from random import choice

# Model Variables
MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

category = choice(["Amazon_Instant_Video", "Beauty", "Books", "CDs_Vinyls", "Cellphones_Accessories", 
    "Clothing_Shoes_Jewelry", "Electronics", "Health_And_Personal", "Home_And_Kitchen", 
    "Movies_And_TV", "Pet_Supplies", "Sports_And_Outdoors"])

df = pd.read_csv(f"Streamlit/datasets/results/{category}_results.csv", nrows=100)

def pageIII():
    columns = st.columns((8,2,2))
    columns[1].image("img\skaivuinsightslogo.png", width = 350)
    columns[0].title("🤖 Review Sentiment Analysis")

    review = df['reviewText'].sample()

    col1, col2 = st.columns([1,1])

    col1.markdown('''
            ## Write a review!!
    ''', unsafe_allow_html = True)
    
    random = col2.checkbox('Get Random Review', help='Get a random review to analyze')
    if random:
        col2.text_area(label='', value=review.iloc[0], disabled=True)

    with st.form(key = "inputText"):
        text = st.text_area("Enter Text Here")
        submit_button = st.form_submit_button(label = "Analyze")

    # Modeling
    if submit_button:      
        encoded_text = tokenizer(text, return_tensors = "pt")
        output = model(**encoded_text)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        # Results
        scores_dict = {
            'Sentiments': ['Positive', 'Neutral', 'Negative'],
            'Scores': [scores[2], scores[1], scores[0]]
        }

        scores_df = pd.DataFrame(scores_dict)
       
        if scores_dict['Scores'][2] >= 0.6:
            st.markdown("### **Sentiment**: Negative 😥")
        
        elif scores_dict['Scores'][1] >= 0.6:
            st.markdown("### **Sentiment**: Neutral 😐")

        elif scores_dict['Scores'][0] >= 0.6:
            st.markdown("### **Sentiment**: Positive 😀")
        
        else:
            st.markdown("### **Sentiment**: Normal 🙂")

        barchart = px.bar(
            data_frame = scores_df,
            x = "Sentiments",
            y = "Scores",
            color = "Sentiments",
            color_discrete_map = {"Negative": "red", "Neutral": "blue", "Positive": "green"},
            opacity = 0.5,
            pattern_shape = "Sentiments", pattern_shape_sequence = ["x", ".", "+"],
        )

        barchart.update_layout(xaxis = dict(showgrid = False),
                               yaxis = dict(showgrid = False))

        st.plotly_chart(barchart, use_container_width = True)

        