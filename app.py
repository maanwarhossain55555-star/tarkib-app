import streamlit as st
import google.generativeai as genai

# ১. পেজ সেটআপ
st.set_page_config(page_title="Arabic Tarkib AI", layout="wide")

# ২. সরাসরি আপনার দেওয়া API Key
API_KEY = "AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o"

# ৩. নিরাপদভাবে মডেল কনফিগারেশন
try:
    genai.configure(api_key=API_KEY)
    # আপনার লাইব্রেরির সাথে যে মডেল কাজ করবে সেটি খুঁজে বের করা
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"Error: {e}")

# ৪. মাদরাসা নোটের মতো ডিজাইন (CSS)
st.markdown("""
    <style>
    .main { background-color: #f9f9f9; }
    .arabic-text { font-size: 35px !important; direction: rtl; text-align: center; background-color: #e8f5e9; padding: 20px; border-radius: 10px; border: 2px solid #2e7d32; margin: 10px 0; }
    .result-box { background-color: #ffffff; padding: 20px; border-radius: 10px; border-left: 5px solid #2e7d32; line-height: 1.8; color: #333; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; border-radius: 8px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 গ্লোবাল আরবি তারকিব অ্যানালাইজার (AI)")
st.write("আপনার আরবি বাক্যটি নিচে লিখুন।")

# ৫. ইনপুট বক্স
user_input = st.text_input("এখানে আরবি বাক্য দিন:", placeholder="যেমন: نَصَرَ زَيْدٌ عَمْرًا")

if st.button("পূর্ণাঙ্গ তারকিব বের করুন"):
    if user_input:
        with st.spinner('AI তারকিব তৈরি করছে...'):
            try:
                # AI কে পরিষ্কার ইনস্ট্রাকশন দেওয়া
                prompt = f"""
                Analyze the Arabic sentence: '{user_input}'
                Provide a detailed 'Tarkib' (Syntactic Analysis) in Bengali language.
                Follow the standard Madrasa/Dars-e-Nizami style.
                1. Word-by-word grammatical role.
                2. Connections (Fail, Maful, Mudaaf, etc.).
                3. Final Jumla type.
                """
                response = model.generate_content(prompt)
                
                # রেজাল্ট দেখানো
                st.markdown(f'<div class="arabic-text">{user_input}</div>', unsafe_allow_html=True)
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.subheader("তারকিব বিশ্লেষণ:")
                st.write(response.text)
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error("দুঃখিত, পুনরায় চেষ্টা করুন।")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")
