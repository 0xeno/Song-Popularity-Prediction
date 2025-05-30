import streamlit as st
from pages.home import Home
from pages.prediksi import Prediction
from pages.rekomendasi import Recommendation
from utils.style import apply_custom_styles

# Apply global CSS styling
apply_custom_styles()

# Sidebar for navigation
st.sidebar.title("Menu")
selection = st.sidebar.radio("Pilih Halaman:", ["Home", "Prediksi", "Rekomendasi"])

# Page routing
if selection == "Home":
    page = Home()
elif selection == "Prediksi":
    page = Prediction()
elif selection == "Rekomendasi":
    page = Recommendation()

page.render()
