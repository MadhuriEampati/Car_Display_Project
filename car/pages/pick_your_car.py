# import streamlit as st
# import pandas as pd

# def run():
#     st.header("Pick Your Car 🚘")

#     # Load dataset
#     try:
#         df = pd.read_csv("Car/Cardata.csv")
#     except FileNotFoundError:
#         st.error("Dataset not found! Please ensure Cardata.csv is inside Car/ folder.")
#         return

#     # Car brand dropdown
#     brand = st.selectbox("Select Car Brand", df['CarName'].unique())

#     # Price slider (in lakhs)
#     price_range = st.slider("Select Price Range (in lakhs)", 0, 50, (5, 15))

#     # Filter dataset
#     filtered = df[
#         (df['CarName'] == brand) &
#         (df['price'] >= price_range[0] * 100000) &
#         (df['price'] <= price_range[1] * 100000)
#     ]

#     if not filtered.empty:
#         st.success("Cars found matching your criteria:")
#         st.dataframe(filtered)
#     else:
#         st.warning("No cars found for selected criteria.")
import streamlit as st
import pandas as pd

st.header("Pick Your Car 🚘")

df = pd.read_csv("Car/Cardata.csv")

brand = st.selectbox("Select Car Brand", df['CarName'].unique())
price_range = st.slider("Select Price Range (in lakhs)", 0, 50, (5, 15))

filtered = df[
    (df['CarName'] == brand) &
    (df['price'] >= price_range[0] * 100000) &
    (df['price'] <= price_range[1] * 100000)
]

if not filtered.empty:
    st.success("Cars found matching your criteria:")
    st.dataframe(filtered)
else:
    st.warning("No cars found for selected criteria.")
