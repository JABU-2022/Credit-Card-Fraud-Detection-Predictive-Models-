# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle 
import streamlit as st
import tensorflow.keras as keras
from keras.models import load_model


# load the saved model

loaded_model1 = load_model("D:/Credit_card_fraud-detection/model1.h5")


# create a function for prediction

def credit_card_fraud_prediction(input_data) :
    
    # change the input data to numpy array 
    
    input_data_as_numpy_array = np.asarray(input_data)
    
    #reshape the array as we are prediction for one instance 
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model1.predict(input_data_reshaped)
    
    print(prediction)
    
    if (prediction[0] == 0):
        
        return 'The data is legit'
    else:
        return 'the data is fraud'
    
    
def main():
    
    #Giving a title 
    
    st.title('Credit card fraud prediction webapp')
    
    # Getting the input data from the user
    
    
    Time = st.text_input("Time")
    V1 = st.text_input("V1")
    V2 = st.text_input("V2")
    V3 = st.text_input("V3")
    V4 = st.text_input("V4")
    V5 = st.text_input("V5")
    V6 = st.text_input("V6")
    V7 = st.text_input("V7")
    V8 = st.text_input("V8")
    V9 = st.text_input("V9")
    V10 = st.text_input("V10")
    V11 = st.text_input("V11")
    V12 = st.text_input("V12")
    V13 = st.text_input("V13")
    V14 = st.text_input("V14")
    V15 = st.text_input("V15")
    V16 = st.text_input("V16")
    V17 = st.text_input("V17")
    V18 = st.text_input("V18")
    V19 = st.text_input("V19")
    V20 = st.text_input("V20")
    V21 = st.text_input("V21")
    V22 = st.text_input("V22")
    V23 = st.text_input("V23")
    V24 = st.text_input("V24")
    V25 = st.text_input("V25")
    V26 = st.text_input("V26")
    V27 = st.text_input("V27")
    V28 = st.text_input("V28")
    Amount = st.text_input("Amount")
    
    
    # code for prediction
    testing = ''
    
    # creating a button for prediction
    
    if st.button('Data test result'):
        testing = credit_card_fraud_prediction([Time,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount])
        
        
    st.success(testing) 
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    