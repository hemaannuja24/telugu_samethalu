import streamlit as st
from datetime import datetime
from pytz import timezone
from ai_classifier import classify_proverb
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

            
# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = st.secrets["GOOGLE_SERVICE_ACCOUNT"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
sheet = client.open("Telugu Proverbs Treasury").sheet1


# Streamlit Config
st.set_page_config(page_title="తెలుగు సామెతల ఖజానా", page_icon="📜", layout="centered")

# Page Header
st.title("📜 తెలుగు సామెతల ఖజానా")
st.markdown("### మీకు తెలిసిన సామెతను పంచుకోండి ✍️")
st.markdown("వెనుక తరాల నుండి ముందుకు, మన తెలుగు జ్ఞానాన్ని భద్రపరుద్దాం.")
st.markdown("<hr style='border:1px solid #555'>", unsafe_allow_html=True)


# Safe reset handling after rerun
if "reset_form" in st.session_state and st.session_state["reset_form"]:
    st.success("ధన్యవాదాలు! మీ సామెత జత చేయబడింది.")
    st.balloons()
    st.session_state["reset_form"] = False  # reset the flag

    # 👁️ View button
    st.markdown("""
        <div style='text-align:center; margin-top:1em'>
            <a href="https://docs.google.com/spreadsheets/d/1J3j-IwOJr3iZlB9x_bc-7v3_L8QQE1_cZa45aA6V140" target="_blank">
                👁️ <b>అన్ని సామెతలను వీక్షించండి</b>
            </a>
        </div>
    """, unsafe_allow_html=True)

# Initialize session state inputs
for key in ["proverb_input", "meaning_input", "context_input"]:
    if key not in st.session_state:
        st.session_state[key] = ""

# Proverb Form
with st.form("proverb_form"):
    st.subheader("📥 కొత్త సామెతను జత చేయండి")
    col1, col2 = st.columns(2)
    with col1:
        proverb = st.text_area("**సామెత (Proverb)**", max_chars=100, height=100, key="proverb_input")
    with col2:
        meaning = st.text_area("**భావం (Meaning)**", max_chars=300, height=100, key="meaning_input")

    context = st.text_input("**సందర్భం (Context / Usage Example – Optional)**", max_chars=150, key="context_input")
    submitted = st.form_submit_button("✅ సామెతను జత చేయండి")

    if submitted:
        if proverb.strip() and meaning.strip():
            text_for_classification = proverb + " " + meaning
            category = classify_proverb(text_for_classification)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            india = timezone('Asia/Kolkata')
            timestamp = datetime.now(india).strftime("%Y-%m-%d %H:%M:%S")

            # Save to Google Sheet
            sheet.append_row([proverb.strip(), meaning.strip(), context.strip(), category, timestamp])

            st.session_state["reset_form"] = True
            st.rerun()
        else:
            st.error("దయచేసి సామెత మరియు భావం రెండూ నమోదు చేయండి.")
