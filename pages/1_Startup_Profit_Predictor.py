import streamlit as st
from src.data_structure import *
from src.util import *
from constants import IMAGES, STARTUP_STATE_CLASS,STARTUP_ASSET
from PIL import Image

st.set_page_config(
    page_title="Hello",
)

st.title("Start Up Company Profit Predictor")

adjust_image(STARTUP_ASSET["Image"]["logo"])

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
        state = st.selectbox('State:', STARTUP_STATE_CLASS)
        
if st.button('Predict'):
    if all([rd, administration, marketing,state]):
        try:
            ads_data = StartupsIn(rd=rd, administration=administration, marketing=marketing,state=state)
            with st.spinner(text='In progress'):
                data = send_data_to_api("https://radenbimo-portofoliotest.hf.space/startups/predict", ads_data.dict())
                st.success(str(data["profit"]))
        except:
            st.write("Wrong input format. Please check your input")
    else:    
        st.write("Please fill in the blank space")
