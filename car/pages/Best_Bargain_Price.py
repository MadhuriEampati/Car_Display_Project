# import streamlit as st
# import pandas as pd

# def run():
#     st.header("Best Bargain Price 💰")

#     try:
#         df = pd.read_csv("Car/Cardata.csv")
#     except FileNotFoundError:
#         st.error("Dataset not found! Please ensure Cardata.csv is inside Car/ folder.")
#         return

#     car_name = st.selectbox("Choose Car", df['CarName'].unique())
#     cars = df[df['CarName'] == car_name]

#     if not cars.empty:
#         min_price = cars['price'].min()
#         max_price = cars['price'].max()
#         st.success(f"Best bargain for {car_name}: ₹{min_price:,} (Max observed: ₹{max_price:,})")
#     else:
#         st.error("Car not found in dataset.")
import streamlit as st
import pandas as pd

st.header("Best Bargain Price 💰")

df = pd.read_csv("Car/Cardata.csv")

car_name = st.selectbox("Choose Car", df['CarName'].unique())
cars = df[df['CarName'] == car_name]

if not cars.empty:
    min_price = cars['price'].min()
    max_price = cars['price'].max()
    st.success(f"Best bargain for {car_name}: ₹{min_price:,} (Max observed: ₹{max_price:,})")
else:
    st.error("Car not found in dataset.")
