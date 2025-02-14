import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("Combined_Card_Collection.csv")
    df.columns = df.columns.str.lower().str.strip()  # Standardize column names
    return df

df = load_data()

# Title
st.title("MTG Card Collection Search")

# Text box for input
search_input = st.text_area("Paste card names below (one per line):")

# Dropdown for filtering
owner_filter = st.selectbox("Filter by owner:", ["Show Both", "Only Joe", "Only Eric"])

# Search function
if st.button("Search"):
    if search_input:
        search_terms = [card.strip() for card in search_input.split("\n") if card.strip()]
        
        # Filter based on search terms
        filtered_df = df[df["name"].isin(search_terms)]
        
        # Apply owner filter
        if owner_filter == "Only Joe":
            filtered_df = filtered_df[filtered_df["owner"] == "My Collection"]
        elif owner_filter == "Only Eric":
            filtered_df = filtered_df[filtered_df["owner"] == "Eric's Collection"]

        # Display results
        if filtered_df.empty:
            st.warning("No matching cards found.")
        else:
            st.dataframe(filtered_df)
    else:
        st.warning("Please enter card names to search.")
