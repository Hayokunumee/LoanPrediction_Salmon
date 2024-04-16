import pandas as pd 
import streamlit as st
import joblib 
import warnings
warnings.filterwarnings('ignore')

ds = pd.read_csv('Loan_Data.csv')

# st.title('LOAN APPLICATION APP')
# st.subheader('Built By Salmon Crushers')

# Add header and subheader
st.markdown("<h1 style = 'color: #86469C; text-align: center; font-size: 60px; font-family: Arial Black'>LOAN APPLICATION APP</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #F11A7B; text-align: center; font-family: cursive '>Built By Salmon Crushers</h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html= True)


#Add an Image
st.image('pngwing.com loan1.png', width = 600, caption = 'Created By Ayokunumi')

#Add Project Problem Statement
st.markdown("<h2 style = 'color: #132043; text-align: center; font-family: montserrat '>Background Of Study</h2>", unsafe_allow_html = True)
st.markdown("<p>Leveraging Predictive Modeling for Fair Loan Qualification Based on Customer Features, this study aims to develop a robust predictive model that accurately determines loan eligibility by analyzing customer features, promoting efficiency and fairness in decision-making, and deploying it into a user-friendly system for real-time loan eligibility predictions</p>", unsafe_allow_html= True)

#SIDEBAR DESIGNS

#To Add Anything To The Sidebar Of The Page
st.sidebar.image('pngwing.com loan4.png')

st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)

#To Add The Project Dataset
st.divider()
st.header('Loan Data')
st.dataframe(ds, use_container_width = True)

#To Add Space To The Siebar Before Adding Writeup To Give Line Space
st.sidebar.markdown("<br>", unsafe_allow_html= True)
st.sidebar.markdown("<br>", unsafe_allow_html= True)

#User Inputs
app_income = st.sidebar.number_input('Applicant Income', ds['ApplicantIncome'].min(), ds['ApplicantIncome'].max())
co_app_income = st.sidebar.number_input('Co Applicant Income', ds['CoapplicantIncome'].min(), ds['CoapplicantIncome'].max())
education = st.sidebar.selectbox('Education', ds['Education'].unique())
gender = st.sidebar.selectbox('Gender', ds['Gender'].unique())
loan_status = st.sidebar.selectbox('Loan_Status', ds['Loan_Status'].unique())
married = st.sidebar.selectbox('Married', ds['Married'].unique())
ppty_area = st.sidebar.selectbox('Property_Area', ds['Property_Area'].unique())
self_employed = st.sidebar.selectbox('Self_Employed', ds['Self_Employed'].unique())

#Import Transformers
app_income = joblib.load('ApplicantIncome_scaler.pkl')
co_app_income = joblib.load('CoapplicantIncome_scaler.pkl')
education = joblib.load('Education_encoder.pkl')
gender = joblib.load('Gender_encoder.pkl')
loan_status = joblib.load('Loan_Status_encoder.pkl')
married = joblib.load('Married_encoder.pkl')
ppty_area = joblib.load('Property_Area_encoder.pkl')
self_employed = joblib.load('Self_Employed_encoder.pkl')
a
#User Input Datafrme
user_input = pd.DataFrame()
user_input['ApplicantIncome'] = [app_income]
user_input['CoapplicantIncome'] = [co_app_income]
user_input['Education'] = [education]
user_input['Gender'] = [gender]
user_input['Married'] = [married]
user_input['Property_Area'] = [ppty_area]
user_input['Self_Employed'] = [self_employed]

st.markdown("<br>", unsafe_allow_html = True)
st.header('Input Variable')
st.dataframe(user_input, use_container_width = True)

#Transform Users input According To trainng Scale And Encoding
user_input['ApplicantIncome'] = app_income_scaler.transform(user_input[['ApplicantIncome']])
user_input['CoapplicantIncome'] = co_app_income_scaler.transform(user_input[['CoapplicantIncome']])
user_input['Education'] = education_scaler.transform(user_input[['Education']])
user_input['Gender'] = gender_scaler.transform(user_input[['Gender']])
user_input['Married'] = married_scaler.transform(user_input[['Married']])
user_input['Property_Area'] = ppty_area_scaler.transform(user_input[['Property_Area']])
user_input['Self_Employed'] = self_employed_scaler.transform(user_input[['Self_Employed']])
st.header('Transformed Input Variable')
st.dataframe(user_input, use_container_width = True)
