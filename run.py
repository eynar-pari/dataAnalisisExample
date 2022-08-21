import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt  


st.title('CSV Reader')
file = st.file_uploader('upload a csv',type="csv")
st.write(df)


#
#  to execute
# py -m streamlit run hello.py