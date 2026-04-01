import streamlit as st
import google.generativeai as genai

# ১. পেজ কনফিগারেশন
st.set_page_config(page_title="Arabic Tarkib AI", layout="wide")

# ২. আপনার সরাসরি দেওয়া API Key
API_KEY = "AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o"

# ৩. নিরাপদভাবে মডেল সেটআপ
genai.configure(api_key=API_KEY)
# এখানে আমরা সব ভার্সনে কাজ করে এমন মডেল ব্যবহার করছি
model = genai.GenerativeModel('gemini-pro') 

# ৪. ডিজাইন (CSS)
st.markdown("""
    <style>
    .arabic-text { font-size: 35px !important; direction: rtl; text-align: center; background-color: #f1f8e9; padding: 20px; border-radius: 10px; border: 2px solid #2e7d32; }
    .result-box { background-color: #ffffff; padding: 20px; border-radius: 10px; border-left: 5px solid #2e7d32; line-height: 1.8; color: black; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; font-weight: bold; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 গ্লোবাল আরবি তারকিব অ্যানালাইজার (AI)")

# ৫. ইনপুট ও প্রসেসিং
user_input = st.text_input("আরবি বাক্যটি এখানে লিখুন:", placeholder="যেমন: نَصَرَ زَيْدٌ عَمْرًا")

if st.button("পূর্ণাঙ্গ তারকিব বের করুন"):
    if user_input:
        with st.spinner('AI বিশ্লেষণ করছে...'):
            try:
                # সুনির্দিষ্ট ইনস্ট্রাকশন
                prompt = f"Analyze the Arabic sentence: '{user_input}' and provide a complete Tarkib in Bengali language following Madrasa (Dars-e-Nizami) style."
                
                response = model.generate_content(prompt)
                
                # রেজাল্ট দেখানো
                st.markdown(f'<div class="arabic-text">{user_input}</div>', unsafe_allow_html=True)
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.subheader("তারকিব বিশ্লেষণ:")
                st.write(response.text)
                st.markdown('</div>', unsafe_allow_html=True)
                
            except Exception as e:
                # এররটি সঠিকভাবে ধরার জন্য
                st.error(f"দুঃখিত, পুনরায় চেষ্টা করুন। সমস্যাটি হলো: {str(e)}")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")
