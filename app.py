import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

# Streamlit page setup
st.set_page_config(page_title="Gemini Historical Artifact Description App")
st.title("🏺 Gemini Historical Artifact Description App")
st.write("Upload an artifact image and get a detailed AI-generated description.")

# Load BLIP model (cached for speed)
@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()

# Input prompt
prompt = st.text_input("Describe", "Enter a description prompt for this artifact")

# File uploader
uploaded_file = st.file_uploader("Upload Artifact Image", type=["jpg", "jpeg", "png"])

# Generate description button
if st.button("Generate Artifact Description"):
    if uploaded_file is not None and prompt.strip() != "":
        image = Image.open(uploaded_file).convert("RGB")

        with st.spinner("Analyzing artifact..."):
            # Process image + prompt
            inputs = processor(image, prompt, return_tensors="pt")
            output = model.generate(**inputs)
            description = processor.decode(output[0], skip_special_tokens=True)

        # Display uploaded image and AI description
        st.image(image, caption="Uploaded Artifact", use_container_width=True)
        st.subheader("Artifact Description:")
        st.write(description)
    else:
        st.warning("Please enter a prompt and upload an image.")