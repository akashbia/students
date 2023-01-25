# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 23:10:21 2022

@author: HP
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# to catch the data use it later

@st.cache
def load_data():
    dataset = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\BIA\students.csv")
    return dataset

def plot_hrs_scores():
    ds = load_data()
    fig = plt.figure(figsize = (10,5))
    plt.scatter("Hours","Scores",data=ds)
    plt.title("Hours vs Percentage")
    plt.xlabel("Hours studied")
    plt.ylabel("percentage scores")
    st.pyplot(fig)
    
def show_explore_page():
    st.title("Explore student study hours data")
    
    st.write(""" ### student study hours vs marks obtained""")
    plot_hrs_scores()
    

    
    