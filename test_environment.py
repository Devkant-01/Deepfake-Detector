import torch
import cv2
import librosa
import numpy
import pandas
import sklearn
import fastapi

print("===== ENVIRONMENT TEST =====")
print("Python: OK")
print("PyTorch:", torch.__version__)
print("OpenCV:", cv2.__version__)
print("Librosa:", librosa.__version__)
print("NumPy:", numpy.__version__)
print("Pandas:", pandas.__version__)
print("Scikit-learn:", sklearn.__version__)
print("CUDA Available:", torch.cuda.is_available())
print("============================")