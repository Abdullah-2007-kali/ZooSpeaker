# ---------------------------
# RUN
# ---------------------------
from tkinter.filedialog import askopenfilename
from tkinter import Tk
from cnn_ import CnnModel
from audiomodel import AuidoModel

Tk().withdraw()
filename = askopenfilename(title="Choose an image", filetypes=[("Images", "*.jpg *.png *.jpeg")])

model_path = "C:/Users/Abdullah/Downloads/animal_classifier_model (1)/animal_classifier_model.keras"

cnn = CnnModel(model_path, filename)
cnn.load_model()
cnn.image_processing()
class_id = cnn.predict_model()

audio = AuidoModel("data_text_audio.json")
audio.open_file()
audio.search_text(class_id)
audio.text_to_speech()