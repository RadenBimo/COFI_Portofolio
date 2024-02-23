import streamlit as st
from src.data_structure import *
from src.util import *
from constants import IMAGES
from PIL import Image

st.set_page_config(
    page_title="Hello",
)

st.title("Start Up Company Profit Predictor")
pic = Image.open("./images/profit.png")

col1,col2,col3 = st.columns([1,3,1])
with col1:
    st.write("")
with col2:
    col2 = st.image(pic)
with col3:
    st.write("")

#---Data Inspection---
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with st.container():
    with col1:
        rd = st.text_input('R&D Spend:')
    with col2:
        administration = st.text_input('Administration Spend:')
    with col3:
        marketing = st.text_input('Marketing Spend:')
    with col4:
        state = st.text_input('State Spend:')
        
if st.button('Predict'):
    if rd and administration and marketing and state:
        ads_data = StartupsIn(rd=rd, administration=administration, marketing=marketing,state=state)
        st.write(ads_data)
        data = send_data_to_api("https://radenbimo-portofoliotest.hf.space/startups/predict", ads_data.dict())
        st.write(data["profit"])
