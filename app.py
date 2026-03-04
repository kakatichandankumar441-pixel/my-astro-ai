import streamlit as st
import google.generativeai as genai

# API Config
API_KEY = "AIzaSyCJjcVQx1SeuvefGZe-UiD3bc1eQKCOxDM"
genai.configure(api_key=API_KEY)

# Page Styling
st.set_page_config(page_title="Chandan AI Hub", page_icon="🚀", layout="centered")

# Custom CSS for better look
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #4CAF50; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=100) # Logo
    st.title("Settings ⚙️")
    language = st.selectbox("Language / ভাষা / भाषा", ["Assamese", "Bengali", "Hindi", "English", "Bodo"])
    mode = st.radio("Service Type:", ["Astro Expert 🔮", "Coding Guru 💻", "Business & Marketing 📈"])
    st.divider()
    st.info("Developed by: Chandan Kumar Kakati")

st.title(f"🚀 {mode}")
st.write(f"Hello Dost! Aapka AI Assistant ab **{language}** mein taiyar hai.")

# Input
user_input = st.text_area("Aapka sawal yahan likhein:", placeholder="E.g. Coding sikhao ya bhavishya batao...")

if st.button("Generate Answer ✨"):
    if user_input:
        with st.spinner('AI Process Kar Raha Hai...'):
            try:
                model = genai.GenerativeModel('gemini-pro')
                # Strict language instruction
                prompt = f"Act as: {mode}. User: Chandan. Language: Strictly respond in {language}. Question: {user_input}."
                response = model.generate_content(prompt)
                
                st.success(f"Response in {language}:")
                full_text = response.text
                st.write(full_text)
                
                # Voice Simulation (Google TTS)
                audio_link = f"https://translate.google.com/translate_tts?ie=UTF-8&q={full_text[:200]}&tl=hi&client=tw-ob"
                st.audio(audio_link, format="audio/mp3")
                
            except Exception as e:
                st.error("Nayi API Key activate hone mein 2 min lagte hain. Phir se try karein!")
    else:
        st.warning("Kuch toh likhiye dost!")

# Business Monetization
st.divider()
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 💎 Premium Plan")
    st.write("Full Support: ₹199")
with col2:
    upi_id = "my-astroai@ptaxis"
    st.markdown(f"[📱 Pay via UPI](upi://pay?pa={upi_id}&pn=Chandan&am=199)")

st.caption("© 2026 Chandan Kumar Kakati | All Rights Reserved")
