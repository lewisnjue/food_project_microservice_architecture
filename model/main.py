from PIL import Image
import io
from fastapi import FastAPI, UploadFile
import onnxruntime as ort
from preprocessing import preprocess_image
import numpy as np
import pickle



app = FastAPI()


onnx_model_path = "food_model.onnx"
ort_session = ort.InferenceSession(onnx_model_path)

with open('label.pkl', 'rb') as file:
    loaded_labels = pickle.load(file)


labels = loaded_labels
labels = {int(v): k for k, v in loaded_labels.items()}
@app.post("/predict")
async def predict(file: UploadFile):
    image_bytes = await file.read()

    input_tensor = preprocess_image(image_bytes)
    input_tensor = input_tensor.astype(np.float32)

    ort_inputs = {ort_session.get_inputs()[0].name: input_tensor}
    ort_outputs = ort_session.run(None, ort_inputs)

    logits = ort_outputs[0]

    probs = np.exp(logits) / np.sum(np.exp(logits), axis=-1, keepdims=True)
    predicted_idx = int(np.argmax(probs))
    confidence = float(np.max(probs))
    predicted_label = labels.get(predicted_idx, "Unknown")

    return {
        "label": predicted_label,
        "confidence": confidence
    }
