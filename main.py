import streamlit as st
from PIL import Image
image = Image.open('nn.jpeg')
st.image(image, caption='Sunrise by the mountains')
