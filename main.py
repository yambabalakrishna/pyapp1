import streamlit as st
from PIL import Image
st.set_page_config(layout="wide")
image = Image.open('nn.jpg')
st.image(image, caption='it is my first web page deployment to cloud')
st.write("Welcome to the page")
