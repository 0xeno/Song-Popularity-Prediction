import streamlit as st
import pandas as pd

class Recommendation:
    def render(self):
        st.title("🎧 Refrensi Lagu")

        df = pd.read_csv("data/Song_data_cleaned.csv")

        st.markdown("### Filter Berdasarkan Karakteristik")

        col1, col2, col3 = st.columns(3)

        with col1:
            mood = st.selectbox("Mood Lagu", ["","Happy", "Chill", "Sad"])
            production = st.selectbox("Tipe Produksi", ["","Acoustic", "Electronic", "Major Key Song", "Minor Key Song"])

        with col2:
            duration = st.selectbox("Durasi Lagu", ["","Short", "Average", "Long"])
            volume = st.selectbox("Tingkat Volume", ["","Quiet", "Normal", "Loud"])
        with col3:
            key = st.selectbox("Nada Dasar", ["", "C", "D", "E", "F", "G", "A", "B", "F#", "Bb", "Eb"])
        filtered_df = df.copy()
        if st.button("Filter"):
            # Filter mood
            if mood == "Happy":
                filtered_df = filtered_df[(filtered_df["audio_valence"] > 0.6) & (filtered_df["loudness"] > -10)]
            elif mood == "Chill":
                filtered_df = filtered_df[(filtered_df["audio_valence"] > 0.4) & (filtered_df["loudness"] <= -10)]
            elif mood == "Sad":
                filtered_df = filtered_df[filtered_df["audio_valence"] < 0.4]
        
            # Filer Production
            if production == "Acoustic":
                filtered_df = filtered_df[filtered_df['acousticness'] > 0.7]
            elif production == "Electronic":
                filtered_df = filtered_df[filtered_df['acousticness'] < 0.3]
            elif production == "Major Key Song":
                filtered_df = filtered_df[filtered_df['audio_mode_encoded'] == 1]
            elif production == "Minor Key Song":
                filtered_df = filtered_df[filtered_df['audio_mode_encoded'] == 0]

            # Filter durasi
            if duration == "Short":
                filtered_df = filtered_df[filtered_df["song_duration_min"] < 120000]
            elif duration == "Average":
                filtered_df = filtered_df[(filtered_df["song_duration_min"] >= 120000) & (filtered_df["song_duration_min"] <= 270000)]
            elif duration == "Long":
                filtered_df = filtered_df[filtered_df["song_duration_min"] > 270000]

            # Filter volume
            if volume == "Quiet":
                filtered_df = filtered_df[filtered_df["loudness"] < -20]
            elif volume == "Normal":
                filtered_df = filtered_df[(filtered_df["loudness"] >= -20) & (filtered_df["loudness"] <= -10)]
            elif volume == "Loud":
                filtered_df = filtered_df[filtered_df["loudness"] > -10]
        
            if key:
                key_mapping = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11, "F#": 6, "Bb": 10, "Eb": 3}
                filtered_df = filtered_df[filtered_df['key_encoded'] == key_mapping[key]]
    
        search = st.text_input("Search your song :")
        if search:
            filtered_df = filtered_df[filtered_df['song_name'].str.contains(search, case=False, na=False)]

        filtered_df = filtered_df.sort_values(by='song_popularity', ascending=False)

        st.dataframe(filtered_df.head(5))
