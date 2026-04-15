import streamlit as st
from transformers import pipeline
@st.cache_resource
def load_summarizer():
  return pipeline("summarization",model="sshleifer/distrilbart-cnn-12-6")
