def predict_voice_type(features):
    # Dummy logic for now
    confidence = 0.85
    label = "AI-generated" if confidence > 0.8 else "Human"

    explanation = "Unnatural spectral consistency detected"

    return label, confidence, explanation
