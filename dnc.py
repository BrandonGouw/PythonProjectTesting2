import pathlib
import platform
import streamlit as st
import sys
from fastai.vision.all import load_learner, PILImage

sys.modules["pathlib._local"] = pathlib
# Fix for loading Linux/Kaggle-exported .pkl models on Windows
if platform.system() == "Windows":
    pathlib.PosixPath = pathlib.WindowsPath

st.title("Cat vs. Dog Classifier")
st.write("Upload a photo of a cat or a dog and let the FastAI model predict what it is.")


# Cache the model so Streamlit doesn't reload it from disk on every UI interaction
@st.cache_resource
def load_model():
    return load_learner("cat_vs_dog_fastai2_7_19.pkl")

def cat_or_dog(x):
    return "cat" if x[0].isupper() else "dog"

model = load_model()

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert uploaded bytes to a PILImage that FastAI understands
    img = PILImage.create(uploaded_file)

    # Display the image on the webpage
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Run prediction
    pred_class, pred_idx, probs = model.predict(img)
    confidence = probs[pred_idx] * 100

    # Display results
    st.success(f"Prediction: **{str(pred_class).upper()}**")
    st.info(f"Confidence: **{confidence:.2f}%**")