import streamlit as st
from core.metrics import collect_metrics
from core.executor import execute_command
from core.health import health_check

st.set_page_config("DevOps Control Plane", layout="wide")
st.title("⚙️ DevOps Control Plane")

tab1, tab2, tab3 = st.tabs(["Metrics", "Operations", "Health"])

with tab1:
    st.subheader("System Metrics")
    st.json(collect_metrics())

with tab2:
    st.subheader("Operational Commands")
    cmd = st.text_input("Command")
    if st.button("Execute"):
        st.code(execute_command(cmd))

with tab3:
    st.subheader("Health Status")
    st.json(health_check())
