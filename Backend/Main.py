from fastapi import FastAPI
from src.data_structure import *
from Backend.model.startups.startups_v0_1_0 import __version__ as startups_model_ver
from Backend.model.startups.startups_v0_1_0 import predict_pipeline as predict_startups
from Backend.model.ads.ads_v0_1_0 import __version__ as ads_model_ver
from Backend.model.ads.ads_v0_1_0 import predict_pipeline as predict_ads
import asyncio

__model_version__ = {
    "ads" : ads_model_ver,
    "startups" : startups_model_ver
}

app = FastAPI()

@app.get("/")
async def home():
    return {"health_check": "OK", "model_version":__model_version__}


@app.post("/startups/predict", response_model=StartupsOut)
async def predict(data: StartupsIn):
    """
    returns prediction of profit based whether Dept. and location of the store. 

    Parameters:
    - **rd** (float): R&D Dept spend.
    - **administration** (float): Administration Dept spend.
    - **marketing** (float): Marketing Dept spend.
    - **state** (str): The City Store branch located.

    Returns:
    - **Profit** (dict[string,int]): A dictionary containing prediction.
    """
    rd = data.rd
    administration = data.administration
    marketing = data.marketing
    state = data.state
    
    profit = await predict_startups(rd, administration, marketing, state)
    return {"profit": profit.round(2)}


@app.post("/ads/predict", response_model=AdsOut)
def predict(data: AdsIn):
    """
    returns prediction whether users have purchased a product by clicking on the advertisements shown to them.

    Parameters:
    - **gender** (str): gender of the user. Only use "Male" and "Female".
    - **age** (int): user age.
    - **estimatedSalary** (float): Estimation of User Salary

    Returns:
    - **Purchased** (dict[string, float]): A dictionary containing prediction.
    """
    gender = data.gender
    age = data.age
    estimatedSalary = data.estimatedSalary

    purchased = predict_ads(gender, age, estimatedSalary)
    return {"purchased": purchased}


if __name__== '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
