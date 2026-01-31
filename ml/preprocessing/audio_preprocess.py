import librosa
import numpy as np

def preprocess_audio(file_path):
    y, sr = librosa.load(file_path, sr=16000)
    return y, sr
