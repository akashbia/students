# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 22:20:54 2022

@author: HP
"""

import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore or predict",("Explore","predict"))

if page == "Explore":
    show_explore_page()
else:
    show_predict_page()
    
    
 