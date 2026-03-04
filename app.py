import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="My Professional AI Astro", page_icon="🔮")

# --- CUSTOM CSS FOR MOBILE LOOK ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #FF4B4B; color: white; }
    .main { background-color: #f5f7f9; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌟 My Professional AI Astro")
st.write("Aapka personal AI astrologer, hamesha aapke saath.")

# --- USER INPUT ---
name = st.text_input("Apna Naam Likhein:")
rashi = st.selectbox("Apni Rashi Chunein:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])

# --- SECTIONS ---
tab1, tab2 = st.tabs(["🆓 Free Rashifal", "💎 Paid Kundli Report"])

with tab1:
    if st.button("Aaj ka Rashifal Dekhein"):
        if name:
            st.success(f"Dost {name}, aaj ki {rashi} rashi ke mutabik aapko naye financial mauke mil sakte hain. Mehnat jari rakhein!")
        else:
            st.warning("Pehle apna naam likhein.")

with tab2:
    st.info("Iss feature mein AI aapki poori kundli aur career analysis karega.")
    st.write("💰 **Charge: Sirf ₹49**")
    
    # Yahan aap apna Payment Link (GPay/PhonePe/Razorpay) dal sakte hain
    st.markdown("[👉 Yahan Se Payment Karein (Click Here)](#)")
    
    transaction_id = st.text_input("Payment ke baad Transaction ID yahan likhein:")
    
    if st.button("Unlock Paid Report"):
        if len(transaction_id) > 5:
            st.success("Verification Successful! Aapki AI Report niche di gayi hai...")
            st.write("AI Analysis: Aapke grah batate hain ki aap ek bade tech project mein safal honge.")
        else:
            st.error("Sahi Transaction ID darj karein.")

st.divider()
st.caption("Developed by Dildar Hussain | Powered by AI")
