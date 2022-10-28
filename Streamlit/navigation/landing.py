import streamlit as st

def pageI():
    columns = st.columns((8,2,2))
    columns[1].image("img/skaivuinsightslogo.png", width = 350)
    columns[0].title("🤖 Amazon Reviews: Machine Learning Models!")

    st.markdown("""
        ### Welcome👋
        This application presents the following features:
        #### 1. Recommendation system of users who have made purchases and reviews. From a list of predetermined users and a list of categories, the desired number of products will be recommended.
        #### 2. Sentiment analysis for texts. You will be able to write a text and the general feeling will be determined from the words contained in it. 
        ####  
        ##### To learn more about how the models work feel free to visit [Github Repository](https://github.com/dhugueth/DTS03-06_Amazon_Reviews_PF) 😊
        ##### 
        ##### ✨Work Team:
        ###### [Ingmar Orta](https://www.linkedin.com/in/ingmarorta/) - Data Scientist 
        ###### [Tomás Astrada](https://www.linkedin.com/in/tom%C3%A1s-astrada-370b73171/) - Data Engineer
        ###### [Jean Fabra](https://www.linkedin.com/in/jeanfabra/) - Data Engineer 
        ###### [Jorge Fonseca](https://www.linkedin.com/in/jorge-fonseca-alba-83433b117/) - Data Scientist 
        ###### [Daniela Hugueth](https://www.linkedin.com/in/dhugueth/) - Data Analyst
        """, unsafe_allow_html=True)
