import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()
st.title("🌐Fake News Detector")

text = st.text_area("Paste a news article or tweet")

if st.button("Check"):
    if text.strip():
        # Replace this with your ngrok FastAPI URL
        url = os.getenv("BACKEND-URL")
        res = requests.post(url, json={"text": text})
        if res.ok:
            out = res.json()
            st.success(f"Prediction: {out['label']} (Confidence: {out['score']:.2f})")
        else:
            st.error("API error")
    else:
        st.warning("Please enter some text.")
