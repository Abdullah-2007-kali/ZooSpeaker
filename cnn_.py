import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import json
import edge_tts
import asyncio
import pygame


# ---------------------------
# CNN MODEL
# ---------------------------
class CnnModel:
    def __init__(self, model_path, image_path):
        self.model_path = model_path
        self.image_path = image_path
        self.class_names = [
            "class1", "class2", "class3", "class4", "class5",
            "class6", "class7", "class8", "class9", "class10"
        ]

    def load_model(self):
        self.model = tf.keras.models.load_model(self.model_path)

    def image_processing(self):
        img = image.load_img(self.image_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        self.img_array = np.expand_dims(img_array, axis=0)

    def predict_model(self):
        arr = tf.keras.applications.mobilenet_v2.preprocess_input(self.img_array)
        pred = self.model.predict(arr)
        self.class_id = int(np.argmax(pred))
        print("Prediction:", self.class_names[self.class_id])
        return self.class_id
