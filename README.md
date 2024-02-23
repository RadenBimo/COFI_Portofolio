# Portfolio Project

This is a material for a portfolio project class. showcasing a web application built with Streamlit for the frontend and FastAPI for the backend.

## Overview

This project aims to demonstrate the integration of Streamlit and FastAPI to create a full-stack web application. However, the primary purpose of this project is to showcase the construction of a portfolio for a data science practitioner with limited background in web development skills.
Streamlit is used for the frontend, providing an interactive and user-friendly interface, while FastAPI serves as the backend, handling Data Processing, Machine Learning, and serving RESTful APIs.

## Features

- **Interactive UI:** Streamlit provides an interactive user interface with various widgets and components for data visualization and interaction.
- **RESTful API:** FastAPI serves as the backend API, providing endpoints for data retrieval and manipulation.
- **Data Processing:** Backend handles data processing tasks efficiently, ensuring quick response times.
- **Machine Learning:** Incorporate machine learning models for prediction tasks.
- **Easy Deployment:** Both Streamlit and FastAPI are easy to deploy, making it simple to host the application on various platforms.

## Setup

### Requirements

- Python 3.9+
- fastapi 0.109.2
- matplotlib 3.8.2
- pandas 2.2.0
- pydantic 2.6.1
- scikit-learn 1.4.0
- seaborn 0.13.2
- uvicorn 0.27.0.post1

### Installation

1. Clone this repository to your local machine.
    ```bash
    git clone https://github.com/{your-username}/portfolio-project.git
    ```

2. Navigate to the project directory.
    ```bash
    cd COFI_Portofolio
    ```

3. Install dependencies.
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application Localy

1. Start the FastAPI backend server.
    ```bash
    uvicorn Backend.main:app --reload --host 127.0.0.1 --port 8000
    ```

2. Launch the Streamlit frontend.
    ```bash
    streamlit run Profile.py
    ```

3. Open your web browser and go to `http://localhost:8501` to access the application and you can see the documentation API on `http://localhost:8000/docs`.

### Running the Application Online

#### 1. Start the FastAPI backend server.

1.1 Create new spaces on hugging face FastAPI backend server.
![alt text](https://github.com/RadenBimo/COFI_Portofolio/blob/main/images/hf_01.png)

1.2 Choose Docker spaces SDK with blank template.
![alt text](https://github.com/RadenBimo/COFI_Portofolio/blob/main/images/hf_02.png)

1.3 Git Push or upload COFI_Portofolio to your space repository. Hugging Face automatically build your App.

1.4 Open your HF App and click the "⋮" simbol on your app. then click the embed this space option.
![alt text](https://github.com/RadenBimo/COFI_Portofolio/blob/main/images/hf_03.png)

1.5 Look the bottom at the box, this will become your domain to your Rest API.
![alt text](https://github.com/RadenBimo/COFI_Portofolio/blob/main/images/hf_04.png)





#### 2. Start  backend server.



