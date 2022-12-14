import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Bootcam Mojix", page_icon="📊", initial_sidebar_state="expanded",layout="wide",
)

st.title('Bootcam MOJIX - Eynar Pari')
st.header('Select your CSV or use the default (just for testing) ')

uploaded_file_expected = st.file_uploader("Expected Choose expected file", type=".csv")
uploaded_file_counted = st.file_uploader("Choose a counted file", type=".csv")

st.markdown("----")
df_expected = None
df_counted = None

use_default_file = st.checkbox(
    "Use the data used in the class 04 ", False, help="default"
)

if use_default_file:
    df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)
    df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)

start_button = st.button("Start") 
    
if start_button :
    if uploaded_file_expected :
        df_expected = pd.read_csv(uploaded_file_expected, encoding="latin-1", dtype=str)
    if uploaded_file_counted:
        df_counted = pd.read_csv(uploaded_file_counted, encoding="latin-1", dtype=str)
    # remove duplicates
    df_counted = df_counted.drop_duplicates("RFID")
    df_B = df_counted.groupby("Retail_Product_SKU").count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})
    make_choice = st.sidebar.selectbox('Select your RFID:', df_B)

    st.write('Result without Duplicates:', df_B)
    # aggregate
    my_cols_selected = ["Retail_Product_Color",
                        "Retail_Product_Level1",
                        "Retail_Product_Level1Name",
                        "Retail_Product_Level2Name",
                        "Retail_Product_Level3Name",
                        "Retail_Product_Level4Name",
                        "Retail_Product_Name",
                        "Retail_Product_SKU",
                        "Retail_Product_Size",
                        "Retail_Product_Style",
                        "Retail_SOHQTY"]

    df_A = df_expected[my_cols_selected]    
    df_discrepancy = pd.merge(df_A, df_B, how="outer", left_on="Retail_Product_SKU", right_on="Retail_Product_SKU", indicator=True)
    df_discrepancy['Retail_CCQTY'] = df_discrepancy['Retail_CCQTY'].fillna(0)
    df_discrepancy["Retail_CCQTY"] = df_discrepancy["Retail_CCQTY"].astype(int)
    df_discrepancy["Retail_SOHQTY"] = df_discrepancy["Retail_SOHQTY"].fillna(0).astype(int)
    df_discrepancy["Diff"] = df_discrepancy["Retail_CCQTY"] - df_discrepancy["Retail_SOHQTY"]
    df_discrepancy.loc[df_discrepancy["Diff"]<0, "Unders"] = df_discrepancy["Diff"] * (-1)
    df_discrepancy["Unders"] = df_discrepancy["Unders"].fillna(0).astype(int)
    df_final = df_discrepancy.groupby("Retail_Product_Level1Name").sum()
    st.write('Agregate Final:', df_final)

