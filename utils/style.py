def apply_custom_styles():
    import streamlit as st
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Roboto', sans-serif;
            background-color: #0F172A;
            color: #F8FAFC;
        }

        h1 {
            color: #3B82F6;
        }

        h3, h2 {
            color: #06B6D4;
        }

        .stButton>button {
            background-color: #3B82F6;
            color: white;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
