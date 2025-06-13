
import streamlit as st
from spindle_model import run_spindle_app
from slide_model import run_slide_app

st.set_page_config(page_title="Machine Health Predictor", layout="wide")

page = st.sidebar.selectbox("Select Model", ["Spindle Runout Prediction", "Slide Backlash Prediction"])

if page == "Spindle Runout Prediction":
    run_spindle_app()

elif page == "Slide Backlash Prediction":
    run_slide_app()
