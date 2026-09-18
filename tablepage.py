"""Data Tables Page"""
import streamlit as st
from lab_helpers_diabetes import load_data

df = load_data()["train"]

st.write("# Training data")
st.dataframe(df)
