import numpy as np 
import io 
from PIL import Image 
IMAGE_HEIGHT = 224
IMAGE_WIDTH = 224

RESCALE_FACTOR = 0.00392156862745098  # Equivalent to dividing by 255
IMAGE_MEAN = [0.5, 0.5, 0.5]
IMAGE_STD = [0.5, 0.5, 0.5]

def preprocess_image(image_bytes: bytes) -> np.ndarray:
    """
    Preprocess an image for inference with ONNX model.

    Args:
        image_bytes (bytes): Raw image bytes

    Returns:
        np.ndarray: Preprocessed image tensor in NCHW format
    """
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT), resample=Image.BILINEAR)

    img_array = np.array(image).astype(np.float32)

    img_array *= RESCALE_FACTOR  # Same as dividing by 255

    img_array = (img_array - IMAGE_MEAN) / IMAGE_STD

    img_array = np.transpose(img_array, (2, 0, 1))

    img_array = np.expand_dims(img_array, axis=0)

    return img_array





