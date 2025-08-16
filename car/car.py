# import streamlit as st
# from PIL import Image

# # Page config
# st.set_page_config(page_title="Car Display Project", layout="wide")

# # Sidebar menu
# st.sidebar.title("Car Display Project")
# menu = ["Home", "Pick Your Car", "Best Bargain Price"]
# choice = st.sidebar.radio("Navigate", menu)

# # Homepage
# if choice == "Home":
#     st.title("🚗 Welcome to Car Display AI Project")
#     st.image("Car/image_dir/car4.jpg", use_column_width=True)
#     st.write("""
#     ### Features:
#     - Browse cars by brand & price
#     - Find best bargain prices
#     - Explore dataset of used cars
#     """)
# elif choice == "Pick Your Car":
#     from pages import Pick_Your_Car
#     Pick_Your_Car.run()
# elif choice == "Best Bargain Price":
#     from pages import Best_Bargain_Price
#     Best_Bargain_Price.run()
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Car Display Project", layout="wide")

st.title("🚗 Welcome to Car Display AI Project")
st.image("Car/image_dir/car4.jpg", use_column_width=True)
st.write("""
### Features:
- Browse cars by brand & price
- Find best bargain prices
- Explore dataset of used cars
""")



