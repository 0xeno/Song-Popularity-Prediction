import streamlit as st

class Home:
    def render(self):
        st.title("🎵 Song Popularity Prediction")
        st.markdown("""
        <h3>Selamat datang!</h3>
        <p>Aplikasi ini dapat membantu memprediksi seberapa populer sebuah lagu berdasarkan karakteristik lagu yang dimilikinya.</p>
        <p>Data source</p>
        <p>Kaggle : https://www.kaggle.com/datasets/yasserh/song- popularity-dataset</p>
        """, unsafe_allow_html=True)

        with st.expander("Attribute Info"):
            st.markdown("""
            - **acousticness** : A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic. 
            - **key** : The key the track is in. Measure from C to B.
            - **audio mode** : Mode indicates the modality (major or minor) of a track.   
            - **song duration** : The duration of the track in minute.    
            - **loudness** : The overall loudness of a track in decibels (dB). Values typically range between -60 and 0 dB.
            - **audio valence** : A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.  
            """)
