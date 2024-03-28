from src.plot import *

ads_plot= AdsPlot()

INFO = { 
   "Name": "COFI",
   "Full_Name": "Coding for Indonesia",
   "Intro": "A Tech Educator and AI Enthusiast at cognitiveclass.ai",
   "About":"Hi I'm :blue[**Coding for Indonesia**]🙂, we are a training program provider that is committed to producing competent developers in the field of data science and other digital technologies.",
   "Address":"Coding For Indonesia Training Centre, Komplek Pertokoan Duta Mas, Blok A1 No.43 Jalan RS. Fatmawati Raya No.8 DKI Jakarta, Indonesia"
}

CONTACTS = {
   "Ig":{
        "desc":"cofi.official",
        "Url":"https://www.instagram.com/cofi.official?igsh=MTVwd2xzbzljZmM3cg=="
    },
   "WhatsApp":"+62 812-5500-6138",
   "Email": "info.codingforindonesia@gmail.com",

}

IMAGES = {
    "Ads": "./images/ads.jpg",
    "Cofi": "./images/COFI.png",
    "Git": "./images/Git.png",
    "Linkedin": "./images/Link.png",
    "WhatsApp": "./images/Whatsapp.png",
    "Gmail": "./images/gmail.png",
    "Ig": "./images/ig.png",
    "Methodology": "./images/ads_methodology.png"
}

ACTIVITY = {
    "Bootcamp" : {
        "desc":"""
            We provide you a comprehensive data science bootcamp designed to take you from zero to hero. Our team of seasoned experts is 
            fully equipped to guide you through the journey, empowering you to emerge as proficient data science practitioners poised to meet the 
            demands of the market.
        """,
        "image":"./images/Bootcamp2.jpg"
    },
    "Webinar" : {
        "desc": """
            Embark on a journey of continuous growth and mastery with our organized webinars. Led by industry-leading professionals, 
            these sessions are tailored to propel participants from novice to expert in various digital domains. Whether delving into 
            the latest technological trends or exploring emerging technique , our webinars provide you comprehensive learning and practical 
            application.
        """,
        "image":"./images/Webinar.jpg"
    }
}

ADS_PLOT = {
    "Data_distribution" : {
        "plot":  [ads_plot.dist_essalary_plot(),ads_plot.dist_age_plot()],
        "desc": """ 
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
            Create targeted marketing messages that resonate with different age groups. For younger demographics, emphasize the product's 
            innovation or relevance to modern lifestyles, while for older demographics, highlight its practicality or suitability for their needs.
            * **Product Adaptations:**  
            Consider adapting the product or its marketing approach to better suit the preferences and needs of older consumers, 
            ensuring it addresses their specific concerns or challenges.
            
            #### Impact for Model:
            1. The model is expected to predict 0 (not yet purchased the product) for younger people and 1 (purchased) for older individuals.
            2. The model is likely predicts 1 (purchased) for individuals with higher estimated salaries.
        """
    },
    "Gender_influence" : {
        "plot":  [ads_plot.box_gender(),ads_plot.pie_gender()],
        "desc": """
            #### Findings:
            * **Only 35.8% of those who saw advertisements buy the products.**  
            it implies that out of the total number of individuals exposed to the advertisements, 
            a relatively small proportion, specifically 35.8%, actually made a purchase.
            the number quite        

            * **There is no significant difference between women and men.**  
            There is no significant difference between women and men in terms of their response 
            to the advertisements or their likelihood of making a purchase.
            This suggests that the advertising campaign does not target one gender more effectively 
            than the other, and both women and men exhibit similar purchasing behaviors when exposed to the advertisements.

            #### Recommendation:
            1. **There is no significant difference between women and men:**

            * **Segmentation and Personalization:**  
            Utilize customer data to create targeted advertising campaigns that speak directly to the unique preferences and behaviors of 
            different demographic segments. This approach can lead to higher engagement and conversion rates by delivering more relevant 
            content to each group of gender.
            
            #### Impact for Model:
            1. The target feature having an imbalanced dataset can lead to biased model performance and inaccurate predictions, 
            as the algorithm may favor the majority class and neglect the minority class.
            2. Gender is likely to have a minimal impact on the prediction.
        """
    },
}

ADS_DESC={
    "Model_usage": """
        This predictive model can be integrated into advertising platforms to optimize ad targeting and budget allocation. 
        By accurately predicting which users are more likely to make a purchase, advertisers can tailor their campaigns to focus on high-potential 
        customers, thereby improving the overall return on investment (ROI) of their advertising efforts.
    """
}