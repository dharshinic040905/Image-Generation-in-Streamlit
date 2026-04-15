import streamlit as st
import requests
st.title("Image Generation")
prompt="Generate a image of girl with stars in the background."
url="https://image.pollinations.ai/prompt/"+requests.utils.quote(prompt)
img=requests.get(url).content
with open("w.png","wb") as f:
    f.write(img)
    st.image("w.png")




