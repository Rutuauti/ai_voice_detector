import base64
import uuid

def decode_audio(base64_audio: str) -> str:
    audio_bytes = base64.b64decode(base64_audio)
    file_path = f"temp_{uuid.uuid4()}.mp3"

    with open(file_path, "wb") as f:
        f.write(audio_bytes)

    return file_path
