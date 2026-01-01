import streamlit as st

st.set_page_config(page_title="DevOps Task 1", layout="centered")

st.title("🚀 DevOps Task 1 – Dockerized Streamlit App")
st.subheader("If you can see this, your container is working")

st.write("✅ Docker build: SUCCESS")
st.write("✅ Container run: SUCCESS")
st.write("✅ Streamlit UI: LOADED")

# Small change to demonstrate live-reload
import time
st.write("Reload test: Streamlit updated - ", time.time())

st.code("""
# Example commands to build/run locally
# docker build -t control-plane .
# docker run -p 8501:8501 control-plane
""")

st.write("Edit files under `ui/` to trigger Streamlit to rerun (runOnSave=true is enabled in docker-compose.override.yml).")
