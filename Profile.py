import streamlit as st
import requests
from src.data_structure import *
from constants import IMAGES, ACTIVITY, CONTACTS, INFO
from PIL import Image


cofi_pic = Image.open(IMAGES["Cofi"])
wa_pic = Image.open(IMAGES["WhatsApp"])
linkedin_pic = Image.open(IMAGES["Linkedin"])
git_pic = Image.open(IMAGES["Git"])
ig_pic = Image.open(IMAGES["Ig"])


st.set_page_config(
    page_title="My  Profile",
)

#---BIO SECTION---
st.image(cofi_pic, width=150)
st.title("Coding for Indonesia")
st.write(INFO["About"])

# --- PROFILE SECTION ---
st.header("Activity")

col1, col2 = st.columns([4,7], gap="small")
col3, col4 = st.columns([7,4], gap="small")

for i ,(key, val) in enumerate(ACTIVITY.items()):
    pic = Image.open(val['image'])
    pic = pic.resize((1079,1343))
    if (i % 2) != 0 :
        with col1:
            st.empty()
            st.image(pic)
        with col2:
            st.subheader(key)
            st.write(val['desc'])
    else:
        with col3:
            st.subheader(key)
            st.write(val['desc'])          
        with col4:
            st.empty()   
            st.image(pic)