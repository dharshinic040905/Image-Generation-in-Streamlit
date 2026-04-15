# 🎨 AI Image Generator using Pollinations API (Streamlit)

## 📌 Overview
This project is a simple **AI-powered image generation web app** built using **Streamlit and Python**.  
It generates images from text prompts using the **Pollinations AI image API** and displays them instantly in the web interface.

## 🚀 Features
- ✍️ Text-to-image generation
- 🌐 Uses free Pollinations AI API
- 🖼️ Automatically displays generated image in Streamlit
- ⚡ Simple and lightweight UI
- 📥 Saves generated image locally

## 🛠️ Tech Stack
Python • Streamlit • Requests • Pollinations AI API

## ⚙️ How It Works
1. User defines a text prompt  
2. Prompt is encoded into a URL  
3. Request is sent to Pollinations AI API  
4. Image is generated and downloaded  
5. Image is saved and displayed in Streamlit  

## 📂 Code Flow
- Create Streamlit UI  
- Define prompt  
- Generate API URL using `requests.utils.quote()`  
- Fetch image using `requests.get()`  
- Save image as `w.png`  
- Display image using `st.image()`  

## ▶️ Run the Project
```bash
git clone https://github.com/your-username/image-generator.git
cd image-generator
pip install streamlit requests
streamlit run app.py
