import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Bootcam Mojix", page_icon="📊", initial_sidebar_state="expanded"
)

uploaded_file_expected = st.file_uploader("Expected Choose expected file")
uploaded_file_counted = st.file_uploader("Choose a counted file")

use_example_file = st.checkbox(
    "Show the chart original data", False, help="be sure to upload the files"
)

if uploaded_file_expected is not None:
    df_expected = pd.read_csv(uploaded_file_expected)
if uploaded_file_counted is not None:    
    df_counted = pd.read_csv(uploaded_file_counted)

if use_example_file:

    if uploaded_file_expected is not None:
        st.markdown("### Expected Data preview")
        st.write(df_expected)
    else:
        st.write("please upload the expected file")  
    

    if uploaded_file_counted is not None:
        st.markdown("### Counted Data preview")
        st.write(df_counted)
    else:    
        st.write("please upload the counted file") 

    
    
if uploaded_file_expected is not None and  uploaded_file_counted is not None:
    removeDuplicate = st.checkbox(
    "Show data without duplicate", False, help="be sure to upload the files"
    )
    # remove duplicates
    df_counted = df_counted.drop_duplicates("RFID")
    df_B = df_counted.groupby("Retail_Product_SKU").count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})
    make_choice = st.sidebar.selectbox('Select your RFID:', df_B)
    if removeDuplicate:
        st.write('Results:', df_B)
    
S
else:
    st.write("there is no data") 
      





