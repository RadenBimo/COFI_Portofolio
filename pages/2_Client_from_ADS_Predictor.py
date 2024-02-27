import streamlit as st
from src.data_structure import *
from src.util import *
from constants import IMAGES
from PIL import Image
import pandas as pd

df = pd.read_csv("./Modeling/data/Social_Network_Ads.csv")

st.set_page_config(
    page_title="Regression Model",
)

st.title("Client from ADS Predictor")
pic = Image.open(IMAGES["Ads"])
adjust_image(pic)


#---Model_Prediction---
with st.container(height= 300):
    #---Input---
    col1, col2 = st.columns(2)

    with col1:
        age = st.text_input('Age:')
        estimatedSalary = st.text_input('Estimated Salary:')

    with col2:
        gender = st.radio(
            "Gender:",
            ["Female", "Male"],
            index=None,
        )

    #---Model_Prediction---
    if st.button('Predict'):
        if age and estimatedSalary and gender:
            try:
                ads_data = AdsIn(gender=gender, 
                                age=age,
                                estimatedSalary=estimatedSalary)
                data = send_data_to_api("https://radenbimo-portofoliotest.hf.space/ads/predict", ads_data.dict())
                st.markdown(data["purchased"])
            except:
                st.write("Wrong input format. Please check your input")
                st.write(ads_data.dict())
        else:
            st.write("Please fill in the blank space")

#---Model_Profiling---
st.header("About Model")

st.subheader("Model Usage")
st.write("This predictive model can be integrated into advertising platforms to optimize ad targeting and budget allocation. By accurately predicting which users are more likely to make a purchase, advertisers can tailor their campaigns to focus on high-potential customers, thereby improving the overall return on investment (ROI) of their advertising efforts.")

st.subheader("Exploratory Data Analysis")
st.scatter_chart(df,x='Age',y='EstimatedSalary',color='Purchased')
st.bar_chart(df.groupby(["Purchased","Gender"])
            .count()
            .reset_index()
            .pivot(index='Gender', columns='Purchased')['Age'])
st.write()