import streamlit as st

st.title('BMI calculator')

height = st.number_input('Enter Height')

weight = st.number_input('Enter Weight')

calculate = st.button('calculate BMI')

if(calculate):
    bmi = weight/height**2*10000
    if(bmi<10):
        st.title(f'BMI : {bmi}. You are underweight')
    elif(bmi>10 and bmi>20):
        st.title(f'BMI : {bmi}. You are normalweight')
    else:
        st.title(f'BMI : {bmi}. You are overweight')    
