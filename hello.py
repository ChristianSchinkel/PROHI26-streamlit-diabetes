"""This is a Streamlit app that dislplays a tile
for the diabetes lab.
"""
import streamlit as st

st.write("# Diabetes lab 🧪🧫")

page1 = st.Page("tablepage.py",
                title="Tablepage",
                icon="🕺🏻")
page2 = st.Page("histograms.py",
                title="Histograms",
                icon="📈")
page3 = st.Page("optimization.py",
                title="Bar Charts",
                icon="📊")
page4 = st.Page("prescriptive.py",
                title="Prescriptive",
                icon="🎯")

pages = [page1, page2, page3, page4]

st.navigation(pages).run()
