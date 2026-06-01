import streamlit as st
import numpy as np
from scipy.io.wavfile import write
import tempfile

st.title("🎵 AI Music Generator")

st.write("Click the button to generate simple AI music.")

sample_rate = 44100
duration = 3

if st.button("Generate Music"):

    frequency = np.random.randint(200, 1000)

    t = np.linspace(0, duration, int(sample_rate * duration))

    audio = np.sin(2 * np.pi * frequency * t)

    audio = np.int16(audio * 32767)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")

    write(temp_file.name, sample_rate, audio)

    st.audio(temp_file.name)