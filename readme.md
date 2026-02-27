# 🏺 Gemini Historical Artifact Description App

A Streamlit web application that generates detailed descriptions for historical artifacts from uploaded images.

---

## 📌 Project Overview

This application allows users to:

- Input a descriptive prompt for the artifact
- Upload an image of a historical artifact
- Generate an AI-based description using a Vision-Language model
- Display both the uploaded image and the generated description in a clean interface

---

## ⚠️ Important Note on Model Selection

Originally, this project was intended to use **Google's Gemini API** for artifact analysis.  

However, due to **billing and free-tier quota limitations**, API requests were blocked (HTTP 429: RESOURCE_EXHAUSTED).  

To ensure a **fully working demo** without API keys or billing, the project was migrated to an **open-source Vision-Language model**:

**Salesforce BLIP (Bootstrapping Language-Image Pretraining)**

This allows the app to run **locally** and **offline**, providing artifact descriptions reliably.

---

## 🧠 Model Used

- **Model:** `Salesforce/blip-image-captioning-base`  
- **Framework:** Hugging Face Transformers  
- **Execution:** Local inference (CPU/GPU)

---

## 🛠 Technologies Used

- Python  
- Streamlit  
- Hugging Face Transformers  
- PyTorch  
- Pillow (for image handling)

---

## 🚀 How to Run the Project

1️⃣ Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Gemini-Historical-Artifact-Description-App.git
cd Gemini-Historical-Artifact-Description-App