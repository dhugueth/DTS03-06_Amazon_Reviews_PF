import re
import warnings
import requests
import streamlit as st
import pandas as pd
warnings.filterwarnings('ignore')

def pageII():
    columns = st.columns((8,2,2))
    columns[1].image("../img/skaivuinsightslogo.png", width = 350)
    columns[0].title("🤖 Recommendation System")
