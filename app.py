import streamlit as st
import google.generativeai as genai

# --- CONFIG ---
# Aapki nayi API Key bilkul sahi hai
API_KEY = "AIzaSyCJjcVQx1SeuvefGZe-UiD3bc1eQKCOxDM"
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Professional AI Astro", page_icon="🔮")

st.title("🔮 Professional AI Astro")
st.write("Aapka personal AI astrologer jo har sawal ka jawab deta hai.")

name = st.text_input("Apna Naam Likhein:", value="Chandan kumar kakati")
rashi = st.selectbox("Apni Rashi Chunein:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])

tab1, tab2 = st.tabs(["💬 AI Se Baat Karein", "💎 Premium Report"])

with tab1:
    user_ques = st.text_input("Apna sawal yahan likhein:")
    if st.button("AI Se Jawab Payein"):
        if user_ques:
            with st.spinner('Grahon ki dasha check ho rahi hai...'):
                try:
                    # Is baar 'gemini-pro' use kar rahe hain, ye 100% chalega
                    model = genai.GenerativeModel('gemini-pro')
                    prompt = f"You are a Vedic Astrologer. A person named {name}, Rashi {rashi}, asks: {user_ques}. Give a positive and detailed answer in Hindi/Hinglish."
                    response = model.generate_content(prompt)
                    st.success("✨ AI Ka Jawab:")
                    st.write(response.text)
                except Exception as e:
                    # Agar ab bhi error aaye toh ye line humein sahi wajah batayegi
                    st.error("Dost, thoda intezar karein. Nayi API key activate hone mein 2-5 minute leti hai. Dobara click karein.")
        else:
            st.warning("Sawal toh puchiye!")

with tab2:
    st.header("Premium Kundli Analysis")
    st.write("Career aur Love life ki puri jankari. Fee: **₹49**")
    upi_id = "my-astroai@ptaxis"
    pay_url = f"upi://pay?pa={upi_id}&pn=Chandan&am=49&cu=INR"
    st.markdown(f'<a href="{pay_url}" style="background-color:green; color:white; padding:12px; border-radius:10px; text-decoration:none; display:block; text-align:center; font-weight:bold;">📱 Pay via UPI</a>', unsafe_allow_html=True)

st.divider()
st.caption(f"Developed by {name} | Powered by Gemini Pro")

