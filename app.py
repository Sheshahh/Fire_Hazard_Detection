import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("fire_hazard_cnn.keras")

# Page settings
st.set_page_config(page_title="Fire Hazard Detection", page_icon="🔥")

st.title("🔥 Fire Hazard Detection using CNN")
st.write("Upload an image to classify it as Fire Hazard or Non Hazard.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_container_width=True)

    img = image.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)[0][0]

    if prediction >= 0.5:
        st.error("🔥 Fire Hazard Detected")
        st.write(f"Confidence: {prediction*100:.2f}%")
    else:
        st.success("✅ Non Hazard")
        st.write(f"Confidence: {(1-prediction)*100:.2f}%")