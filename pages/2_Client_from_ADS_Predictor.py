import streamlit as st
from src.data_structure import *
from src.util import *
from constants import IMAGES
from PIL import Image
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

mu_tab,eda_tab,arch_tab = st.tabs(["Model Usage","Exploratory Data Analysis","Model Architecture"])

with mu_tab:
    st.subheader("Model Usage")
    st.write("This predictive model can be integrated into advertising platforms to optimize ad targeting and budget allocation. By accurately predicting which users are more likely to make a purchase, advertisers can tailor their campaigns to focus on high-potential customers, thereby improving the overall return on investment (ROI) of their advertising efforts.")

with eda_tab:
    st.subheader("Exploratory Data Analysis")
    st.scatter_chart(df,x='Age',y='EstimatedSalary',color='Purchased')
    if st.button("**Insight**",key = "scatter_chart"):

        st.markdown(""" 
        #### Findings:
        * **People with higher estimated salaries are more likely to purchase the product.**
        This could be because people with more money have more disposable income to spend on non-essential items.
        * **There may be a sweet spot for age.** It appears that people in their 40+ are more likely to purchase the product than younger. 
        This could be because people in this age group are more likely to be financially secure or the product most usefull for older people.

        #### Recommendation:
        1. **People with higher estimated salaries are more likely to purchase the product:**

        * **Targeted Marketing Campaigns:**  
        Focus on marketing strategies that appeal to individuals with higher disposable income. 
        This might involve showcasing the product's quality, luxury, or exclusivity.
        * **Customized Offers:**  
        Offer personalized promotional offers or discounts for wealthy clients, focusing on the product's value proposition.

        2. **There may be a sweet spot for age:**
        * **Segmented Messaging:**  
        Create targeted marketing messages that resonate with different age groups. For younger demographics, emphasize the product's innovation or 
        relevance to modern lifestyles, while for older demographics, highlight its practicality or suitability for their needs.
        * **Product Adaptations:**  
        Consider adapting the product or its marketing approach to better suit the preferences and needs of older consumers, 
        ensuring it addresses their specific concerns or challenges.
        
        #### Impact for Model:
        1. The model is expected to predict 0 (not yet purchased the product) for younger people and 1 (purchased) for older individuals.
        2. The model is likely predicts 1 (purchased) for individuals with higher estimated salaries.
        """)


    fig_box_gender = px.histogram(
        df.groupby(["Purchased","Gender"])
            .count()
            .reset_index(),
        x= 'Purchased',
        y= 'User ID',
        color= 'Gender',
        barmode= 'group',
    )


    purchased_counts = df['Purchased'].value_counts()
    fig = go.Figure(data=[go.Pie(labels=purchased_counts.index, values=purchased_counts.values)])
    fig.update_traces(
        hoverinfo='label+percent',
        textfont_size=15,
        marker=dict(
            colors=['#008B8B','#4682B4'],
            line=dict(color='#000000', width=2)
            )
        )

    col1, col2 = st.columns([2,1])
    with col1:
        st.plotly_chart(fig_box_gender, use_container_width=True)
    with col2:
        st.plotly_chart(fig, use_container_width=True)

    if st.button("**Insight**",key="bar_pie_chart"):

        st.markdown(""" 
        #### Findings:
        * **Only 35.8% of those who saw advertisements buy the products.**  
        it implies that out of the total number of individuals exposed to the advertisements, a relatively small proportion, specifically 35.8%, actually made a purchase.
        the number quite        

        * **There is no significant difference between women and men.**  



        #### Recommendation:
        1. **People with higher estimated salaries are more likely to purchase the product:**

        * **Targeted Marketing Campaigns:**  
        Focus on marketing strategies that appeal to individuals with higher disposable income. 
        This might involve showcasing the product's quality, luxury, or exclusivity.
        * **Customized Offers:**  
        Offer personalized promotional offers or discounts for wealthy clients, focusing on the product's value proposition.

        2. **There may be a sweet spot for age:**
        * **Segmented Messaging:**  
        Create targeted marketing messages that resonate with different age groups. For younger demographics, emphasize the product's innovation or 
        relevance to modern lifestyles, while for older demographics, highlight its practicality or suitability for their needs.
        * **Product Adaptations:**  
        Consider adapting the product or its marketing approach to better suit the preferences and needs of older consumers, 
        ensuring it addresses their specific concerns or challenges.
        
        #### Impact for Model:
        1. The model is expected to predict 0 (not yet purchased the product) for younger people and 1 (purchased) for older individuals.
        2. The model is likely predicts 1 (purchased) for individuals with higher estimated salaries.
        """)

    st.write()