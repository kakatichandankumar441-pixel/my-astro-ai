import streamlit as st
import google.generativeai as genai

# --- CONFIG ---
# Aapki nayi API Key yahan set kar di hai
API_KEY = "AIzaSyCJjcVQx1SeuvefGZe-UiD3bc1eQKCOxDM"
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Professional AI Astro", page_icon="🔮")

st.title("🔮 Professional AI Astro")
st.write("Aapka personal AI astrologer jo har sawal ka jawab deta hai.")

# User Summary se aapka naam
name = st.text_input("Apna Naam Likhein:", value="Chandan kumar kakati")
rashi = st.selectbox("Apni Rashi Chunein:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])

tab1, tab2 = st.tabs(["💬 AI Se Baat Karein", "💎 Premium Report"])

with tab1:
    user_ques = st.text_input("Apna sawal yahan likhein (e.g. Mera career kaisa rahega?):")
    if st.button("AI Se Jawab Payein"):
        if user_ques:
            with st.spinner('Sitari ki chaal dekhi ja rahi hai...'):
                try:
                    # Sabse fast model use kar rahe hain
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = f"You are a professional Vedic Astrologer. A person named {name} with rashi {rashi} is asking: {user_ques}. Give a detailed, helpful, and positive answer in Hindi (Hinglish mix)."
                    response = model.generate_content(prompt)
                    st.success("✨ AI Ka Jawab:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Thoda technical issue hai: {str(e)}")
        else:
            st.warning("Dost, sawal toh puchiye!")

with tab2:
    st.header("Premium Kundli Analysis")
    st.write("Career aur Love life ki puri jankari ke liye report unlock karein.")
    st.write("💰 **Fee: Sirf ₹49**")
    
    # Aapka updated UPI ID
    upi_id = "my-astroai@ptaxis"
    pay_url = f"upi://pay?pa={upi_id}&pn=ChandanKakati&am=49&cu=INR"
    
    st.markdown(f'<a href="{pay_url}" style="background-color:green; color:white; padding:12px; border-radius:10px; text-decoration:none; display:block; text-align:center; font-weight:bold;">📱 PhonePe/GPay Se Pay Karein</a>', unsafe_allow_html=True)
    
    st.caption("Payment ke baad screenshot WhatsApp par bhejein.")

st.divider()
st.caption(f"Developed by {name} | Powered by Google Gemini AI")
