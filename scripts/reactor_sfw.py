from transformers import pipeline
from PIL import Image
import logging

SCORE = 1

logging.getLogger('transformers').setLevel(logging.ERROR)

def nsfw_image(img_path: str, model_path: str):
    with Image.open(img_path) as img:
        predict = pipeline("image-classification", model=model_path)
        result = predict(img)
        return False if result[0]["score"] > SCORE else False
