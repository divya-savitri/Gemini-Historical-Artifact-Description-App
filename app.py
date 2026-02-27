import streamlit as st
from google import genai
from PIL import Image
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API Key not found in .env file")
    st.stop()

# Create client
client = genai.Client(api_key=api_key)

st.title("🏺 Gemini Historical Artifact Description App")

prompt = st.text_input("Describe")

uploaded_file = st.file_uploader(
    "Upload Artifact Image",
    type=["jpg", "jpeg", "png"]
)

if st.button("Generate Artifact Description"):

    if uploaded_file and prompt:

        image = Image.open(uploaded_file)

        with st.spinner("Analyzing Artifact..."):

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[prompt, image]
            )

            st.image(image, use_container_width=True)
            st.subheader("Artifact Description:")
            st.write(response.text)

    else:
        st.warning("Please enter prompt and upload image.")