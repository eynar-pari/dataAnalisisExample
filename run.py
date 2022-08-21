import pandas as pd
import streamlit as st

st.title("Mojix Bootcam - Excercise 3")

uploaded_file_expected = st.file_uploader("Expected Choose expected file")
uploaded_file_counted = st.file_uploader("Choose a counted file")

if uploaded_file_expected is not None:
  df = pd.read_csv(uploaded_file_expected)

if uploaded_file_counted is not None:
  df = pd.read_csv(uploaded_file_counted)
