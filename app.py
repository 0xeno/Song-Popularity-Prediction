import streamlit as st
from fitur.home import Home
from fitur.prediksi import Prediction
from fitur.rekomendasi import Recommendation
from utils.style import apply_custom_styles

# Apply global CSS styling
apply_custom_styles()

# Sidebar for navigation
st.sidebar.title("Menu")
selection = st.sidebar.radio("Pilih Halaman:", ["Home", "Prediksi", "Refrensi"])

# Page routing
if selection == "Home":
    page = Home()
elif selection == "Prediksi":
    page = Prediction()
elif selection == "Rekomendasi":
    page = Recommendation()

page.render()
