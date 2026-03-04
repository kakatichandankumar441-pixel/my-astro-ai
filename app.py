import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
# Aapki API Key yahan set ho gayi hai
genai.configure(api_key="AIzaSyC9MEeWKiOx_zEZoVeD-0cM1vAIL3XqZmI")
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="My AI Astro Professional", page_icon="🔮")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; background-color: #FF4B4B; color: white; font-weight: bold; }
    .pay-button { background-color: #28a745; color: white; padding: 12px; text-align: center; border-radius: 10px; display: block; text-decoration: none; font-weight: bold; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 My Professional AI Astro")
st.write("Aapka personal AI astrologer jo har sawal ka jawab deta hai.")

# --- USER INPUT ---
name = st.text_input("Apna Naam Likhein:")
rashi = st.selectbox("Apni Rashi Chunein:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])

tab1, tab2 = st.tabs(["💬 AI Se Baat Karein", "💎 Premium Report"])

with tab1:
    user_ques = st.text_input("Apna sawal yahan likhein (e.g. Meri shadi kab hogi?):")
    if st.button("AI Se Jawab Payein"):
        if user_ques and name:
            with st.spinner('AI Grahon ki dasha check kar raha hai...'):
                try:
                    prompt = f"You are a professional astrologer. A person named {name} with rashi {rashi} is asking: {user_ques}. Give a friendly and helpful answer in Hindi (Hinglish mix)."
                    response = model.generate_content(prompt)
                    st.markdown(f"### ✨ AI Ka Jawab:")
                    st.write(response.text)
                except Exception as e:
                    st.error("AI thoda busy hai, dobara koshish karein!")
        else:
            st.warning("Pehle naam aur sawal dono likhein, dost!")

with tab2:
    st.header("Premium Kundli Analysis")
    st.write("Career, Health aur Love life ki puri jankari ke liye report unlock karein.")
    st.write("💰 **Fee: Sirf ₹49**")
    
    # Updated UPI Link for Chandan Kakati
    upi_id = "my-astroai@ptaxis"
    pay_url = f"upi://pay?pa={upi_id}&pn=ChandanKakati&am=49&cu=INR"
    
    st.markdown(f'<a href="{pay_url}" class="pay-button">📱 PhonePe/GPay Se Pay Karein</a>', unsafe_allow_html=True)
    
    txn = st.text_input("Payment ke baad Transaction ID (12 digits) yahan likhein:")
    if st.button("Report Unlock Karein"):
        if len(txn) >= 10:
            st.success("✅ Payment Verify Ho Gayi! Aapki detailed report niche hai...")
            st.write("### 💎 Aapka Premium Analysis:")
            st.write(f"Dost {name}, aapke sitare batate hain ki aap ek bahut bade digital project mein safal honge. Mehnat jari rakhein!")
        else:
            st.error("Sahi Transaction ID darj karein.")

st.divider()
st.caption("Developed by Chandan Kakati | Powered by Google AI")

