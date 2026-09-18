"""The Histograms page of the diabetes lab."""
import streamlit as st
from lab_helpers_diabetes import FEATURES, load_data
from matplotlib.figure import Figure

df = load_data()["train"]

st.write("# Histograms")

feature = st.selectbox("Feature", FEATURES)

fig = Figure()
ax = fig.subplots()
ax.hist(df[feature])
ax.set_xlabel(feature)
ax.set_ylabel("Count")
ax.set_title(f"Histogram of {feature}")

st.pyplot(fig)
