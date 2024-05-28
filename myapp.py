import streamlit as st

st.title('BMI calculator')

height = st.number_input('Enter Height')

weight = st.weight_input('Enter Weight')

calculate = st.button('Calculate BMI')

if(calculate):
    bmi = weight/height**2*10000
    if(bmi<10):
        st.title(f'BMI : {bmi}. You are under weight')
    elif(bmi>10 and bmi>20):
        st.title(f'BMI : {bmi}. You are normal weight')
    else:
        st.title(f'BMI : {bmi}. You are over weight')    
