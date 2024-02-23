import streamlit as st
import requests
from PIL import Image

def send_data_to_api(url: str, data: dict)-> dict :
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def adjust_image(pic: Image, formation: list =[1,3,1]) -> None:
    col1,col2,col3 = st.columns(formation)
    with col1:
        st.write("")
    with col2:
        col2 = st.image(pic)
    with col3:
        st.write("")

def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

def auto_activity(activity: dict):
    col1, col2 = st.columns([4,7], gap="small")
    col3, col4 = st.columns([7,4], gap="small")
    for val in activity.vals():

        with col1:
            st.image(cofi_pic)
        with col2:
            st.write()