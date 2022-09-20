# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 17:56:22 2022

@author: SYSTEMarket
"""

import streamlit  as st
st.title("my magic title")
my_text = st.text("A random magic text for you")
my_button = st.button("Run ML computation")
#my_date = st.date_input("When's your birthday",datetime.date(2019, 7, 6))


if my_button:
    st.title("The model is trunning ...")
#if my_date:
#    st.write('Your birthday is:', d)
