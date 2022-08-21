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

if use_example_file:

    if uploaded_file_expected is not None:
        df_expected = pd.read_csv(uploaded_file_expected)
    else:
        st.write("please upload the expected file")  
    

    if uploaded_file_counted is not None:
        df_counted = pd.read_csv(uploaded_file_counted)
    else:    
        st.write("please upload the counted file") 

    st.markdown("### Expected Data preview")
    st.write(df_expected)
    st.markdown("### Counted Data preview")
    st.write(df_counted)


# remove duplicates
#df_counted = df_counted.drop_duplicates("RFID")
#df_B = df_counted.groupby("Retail_Product_SKU").count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})

#st.write(df_B)

