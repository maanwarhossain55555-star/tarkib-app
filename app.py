import streamlit as st
import google.generativeai as genai

# ১. পেজ সেটআপ
st.set_page_config(page_title="Arabic Tarkib AI", layout="wide")

# ২. আপনার API Key
API_KEY = "AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o"

# ৩. এআই কনফিগারেশন (সফল হওয়ার জন্য শক্তিশালী পদ্ধতি)
genai.configure(api_key=API_KEY)

# সচল মডেল খুঁজে নেওয়ার ফাংশন
def get_working_model():
    models_to_try = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
    for m in models_to_try:
        try:
            model = genai.GenerativeModel(m)
            # চেক করা মডেলটি সচল কি না
            model.generate_content("Hi", generation_config={"max_output_tokens": 1})
            return model
        except:
            continue
    return None

# ৪. মাদরাসা নোটের মতো ডিজাইন (CSS)
st.markdown("""
    <style>
    .arabic-text { font-size: 35px !important; direction: rtl; text-align: center; background-color: #f1f8e9; padding: 20px; border-radius: 10px; border: 2px solid #2e7d32; }
    .result-box { background-color: #ffffff; padding: 20px; border-radius: 10px; border-left: 5px solid #2e7d32; color: black; line-height: 1.8; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; font-weight: bold; border-radius: 10px; height: 50px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 গ্লোবাল আরবি তারকিব অ্যানালাইজার (AI)")

# ৫. ইনপুট বক্স
user_input = st.text_input("আরবি বাক্যটি এখানে লিখুন:", placeholder="যেমন: نَصَرَ زَيْدٌ عَمْرًا")

if st.button("পূর্ণাঙ্গ তারকিব বের করুন"):
    if user_input:
        with st.spinner('AI তারকিব তৈরি করছে...'):
            try:
                working_model = get_working_model()
                if working_model:
                    prompt = f"Analyze the Arabic sentence: '{user_input}' and provide a detailed Tarkib in Bengali following Madrasa tradition (Dars-e-Nizami style)."
                    response = working_model.generate_content(prompt)
                    
                    st.markdown(f'<div class="arabic-text">{user_input}</div>', unsafe_allow_html=True)
                    st.markdown('<div class="result-box">', unsafe_allow_html=True)
                    st.subheader("বিশ্লেষণ ফলাফল:")
                    st.write(response.text)
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.error("দুঃখিত, কোনো এআই মডেলের সাথে সংযোগ করা যাচ্ছে না। দয়া করে আপনার API Key সচল আছে কি না চেক করুন।")
            except Exception as e:
                st.error("পুনরায় চেষ্টা করুন।")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")
