from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import base64
import uuid
import os

from ml.preprocessing.audio_preprocess import preprocess_audio
from ml.feature_extraction.mfcc import extract_mfcc
from ml.inference.predict import predict_voice_type

# ✅ Create router FIRST
router = APIRouter()

# =========================
# Request Schema
# =========================
class AudioRequest(BaseModel):
    audio_base64: str
    language: str | None = "en"


# =========================
# Helper function
# =========================
def decode_audio(audio_base64: str) -> str:
    """
    Decodes base64 audio and saves it as a temporary .wav file
    """
    try:
        audio_bytes = base64.b64decode(audio_base64)

        os.makedirs("temp_audio", exist_ok=True)
        file_path = f"temp_audio/{uuid.uuid4()}.wav"

        with open(file_path, "wb") as f:
            f.write(audio_bytes)

        return file_path

    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid audio data")


# =========================
# Prediction Endpoint
# =========================
@router.post("/predict")
def predict_voice(data: AudioRequest):
    try:
        # Decode audio
        audio_path = decode_audio(data.audio_base64)

        # Preprocess
        y, sr = preprocess_audio(audio_path)

        # Feature extraction
        features = extract_mfcc(y, sr)

        # Inference
        label, confidence, explanation = predict_voice_type(features)

        return {
            "classification": label,
            "confidence": round(float(confidence), 2),
            "language": data.language,
            "explanation": explanation
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
