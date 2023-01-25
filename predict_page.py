# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 23:56:50 2022

@author: HP
"""

import streamlit as st
import pickle
import numpy as np

def load_model():
    with open("saved_steps.pkl", "rb")as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor_loaded = data["model"]
hours = data["hours"]

def  show_predict_page():
    st.title("student's Score Prediction")
    
    st.write(""" ### we need some information to predict the marks """)
    
    hrs = st.text_input("Enter Numbers of Hours  you study:","")
    
    ok = st.button ("calculate marks")
    if ok:
        X = np.array([[hrs]])
        X = X.astype(float)
        
        marks = regressor_loaded.predict(X)
        st.subheader(f"The estimated marks are {marks[0]:.2f}")
        
show_predict_page()
    