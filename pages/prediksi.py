import streamlit as st
import joblib

class Prediction:
    def __init__(self):
        self.model = joblib.load("best_regression_model_20250529_131743.joblib")
        
    def render(self):
        st.title("🔍 Prediksi Popularitas Lagu")
        st.markdown("Masukkan fitur-fitur lagu di bawah ini:")

        col1, col2 = st.columns(2)

        with col1:
            acousticness = st.number_input("Acousticness", min_value=0.0, max_value=1.0, step=0.01)
            audio_mode = st.selectbox("Audio Mode",(0,1))
            loudness = st.number_input("Loudness", min_value=-60.0, max_value=0.0, step=0.1)

        with col2:
            key = st.selectbox("key",('C','D♭','D','E♭','E','F','G♭','G','A♭','A','B♭','B'))
            song_duration = st.number_input("song duration", min_value=0.0, max_value=5.0, step=0.01)
            valence = st.number_input("Audio Valence", min_value=0.0, max_value=1.0, step=0.01)

        if st.button("Prediksi"):
            # Simulasi prediksi model
            result = Prediction.prediksi(acousticness, key, audio_mode, song_duration, loudness, valence)
            st.markdown(f"**Skor popularitas lagu anda adalah {result}**")
            
    def prediksi(self,acousticness, key, audio_mode, song_duration, loudness, valence):
        # key preprocessing
        key_mapping = {
            'C': 0,
            'D♭': 1,
            'D': 2,
            'E♭': 3,
            'E': 4,
            'F': 5,
            'G♭': 6,
            'G': 7,
            'A♭': 8,
            'A': 9,
            'B♭': 10,
            'B': 11
        }
        key_encoded = key_mapping[key]
        features = [[
        acousticness,
        key_encoded,
        audio_mode,
        song_duration,
        loudness,
        valence
    ]]
        preidction = self.model.predict(features)
        return preidction[0]