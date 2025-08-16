
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Car Display Project", layout="wide")

st.title(" Welcome to Car Display AI Project")
st.image("Car/image_dir/car4.jpg", use_column_width=True)
st.write("""
### Features:
- Browse cars by brand & price
- Find best bargain prices
- Explore dataset of used cars
""")



