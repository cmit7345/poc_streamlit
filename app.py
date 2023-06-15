import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


# Generate fake data func
def generate_data():
    categories = ["A", "B", "C", "D", "E"]
    values = np.random.randint(1, 50, size=5)
    return pd.DataFrame({"Category": categories, "Value": values})


# App Layout
st.title("POC Streamlit")
chart_type = st.sidebar.selectbox("Select Chart Type",
                                  ("Pie Chart", "Histogram"))

if chart_type == "Pie Chart":
    data = generate_data()
    fig = px.pie(data, values="Value", names="Category")
    st.plotly_chart(fig)
else:
    data = generate_data()
    fig = px.histogram(data, x="Category", y="Value", nbins=len(data))
    st.plotly_chart(fig)
