import streamlit as st
from src.data_structure import *
from src.util import *
from src.plot import *
from constants import IMAGES,ADS_PLOT,ADS_ASSET
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ['API_KEY']

df = pd.read_csv("./Modeling/data/Social_Network_Ads.csv")

st.set_page_config(
    page_title="Regression Model",
)

st.title("Client from ADS Predictor")
adjust_image(Image.open(ADS_ASSET["Image"]["logo"]))

#------------Model_Prediction------------
with st.container(height= 300):
    # Input
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

    # Model_Prediction
    if st.button('Predict'):
        if all([age, estimatedSalary, gender]):
            try:
                ads_data = AdsIn(gender=gender, age=age, estimatedSalary=estimatedSalary)
                data = send_data_to_api(f"{api_key}/ads/predict", ads_data.dict())
                st.markdown(data["purchased"])
            except:
                st.write("Wrong input format. Please check your input")
        else:
            st.write("Please fill in the blank space")

#------------Model_Profiling------------
st.header("About Model")

mu_tab,eda_tab,method_tab = st.tabs(["Model Usage","Exploratory Data Analysis","Methodology"])
with mu_tab:
    st.subheader("Model Usage")
    st.divider()

    st.write(ADS_ASSET["Model_usage"])

with eda_tab:
    st.subheader("Exploratory Data Analysis")
    st.divider()

    # Data Distribution
    st.markdown("### Data Distribution")
    col1, col2 = st.columns([1,1])
    st.scatter_chart(df,x='Age',y='EstimatedSalary',color='Purchased',use_container_width=True)
    with col1:
        st.plotly_chart(ADS_PLOT["Data_distribution"]["plot"][1], use_container_width=True)
    with col2:
        st.plotly_chart(ADS_PLOT["Data_distribution"]["plot"][0], use_container_width=True)

    if st.button("**Insight**",key = "scatter_chart"):
        st.markdown(ADS_PLOT["Data_distribution"]["desc"])
    
    # Gender Distribution
    st.markdown("### Gender Distribution Analysis")
    col1, col2 = st.columns([2,1])
    with col1:
        st.plotly_chart(ADS_PLOT["Gender_influence"]["plot"][0], use_container_width=True)
    with col2:
        st.plotly_chart(ADS_PLOT["Gender_influence"]["plot"][1], use_container_width=True)

    if st.button("**Insight**",key="bar_pie_chart"):
        st.markdown(ADS_PLOT["Gender_influence"]["desc"])

    st.write()

with method_tab:
    st.subheader("Methodology")
    st.divider()

    flow_chart = Image.open(ADS_ASSET["Image"]["methodology"])
    adjust_image(flow_chart)
    