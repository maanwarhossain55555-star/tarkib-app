import streamlit as st
import google.generativeai as genai

# অ্যাপ কনফিগারেশন
st.set_page_config(page_title="Arabic Tarkib AI", layout="wide")

# আপনার API Key সরাসরি বসানো
API_KEY = "AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o"

# স্টাইল এবং ডিজাইন
st.markdown("""
    <style>
    .arabic-text { font-size: 35px !important; direction: rtl; text-align: center; background-color: #f1f8e9; padding: 20px; border-radius: 10px; border: 2px solid #2e7d32; }
    .result-box { background-color: #ffffff; padding: 20px; border-radius: 10px; border-left: 5px solid #2e7d32; line-height: 1.8; color: black; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; font-weight: bold; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 গ্লোবাল আরবি তারকিব অ্যানালাইজার (AI)")

# ইনপুট
sentence = st.text_input("আরবি বাক্যটি এখানে লিখুন:", placeholder="যেমন: نَصَرَ زَيْدٌ عَمْرًا")

if st.button("পূর্ণাঙ্গ তারকিব বের করুন"):
    if sentence:
        with st.spinner('AI বিশ্লেষণ করছে, দয়া করে একটু অপেক্ষা করুন...'):
            try:
                # API সেটআপ এবং মডেল কল
                genai.configure(api_key=API_KEY)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # AI এর জন্য সুনির্দিষ্ট নির্দেশ
                prompt = f"Analyze the Arabic sentence: '{sentence}' and provide a detailed Tarkib in Bengali language following Madrasa tradition (Dars-e-Nizami style)."
                
                response = model.generate_content(prompt)
                
                if response.text:
                    st.markdown(f'<div class="arabic-text">{sentence}</div>', unsafe_allow_html=True)
                    st.markdown('<div class="result-box">', unsafe_allow_html=True)
                    st.subheader("বিশ্লেষণ ফলাফল:")
                    st.write(response.text)
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.error("AI কোনো উত্তর দিতে পারেনি।")
            except Exception as e:
                st.error(f"দুঃখিত, পুনরায় চেষ্টা করুন। সমস্যাটি হলো: {str(e)}")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")
