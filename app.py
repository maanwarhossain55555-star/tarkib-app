import streamlit as st
import google.generativeai as genai

# ১. অ্যাপ কনফিগারেশন
st.set_page_config(page_title="Arabic Tarkib AI", layout="wide")

# ২. আপনার API Key সরাসরি কনফিগার করা
API_KEY = "AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o"

# ৩. লেটেস্ট মডেল কনফিগারেশন
genai.configure(api_key=API_KEY)
# আমরা এখানে gemini-1.5-pro ব্যবহার করছি যা সবচেয়ে শক্তিশালী
model = genai.GenerativeModel('gemini-1.5-pro')

# ৪. ডিজাইন (CSS)
st.markdown("""
    <style>
    .arabic-font { font-size: 35px !important; direction: rtl; text-align: center; background-color: #f0f2f6; padding: 20px; border-radius: 15px; border: 2px solid #2e7d32; }
    .tarkib-box { border: 2px solid #1b5e20; padding: 15px; border-radius: 10px; background-color: #ffffff; line-height: 1.8; color: black; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; font-weight: bold; height: 3em; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 গ্লোবাল আরবি তারকিব অ্যানালাইজার (AI)")
st.write("যেকোনো আরবি বাক্য লিখুন, AI এটি মাদরাসা স্টাইলে বিশ্লেষণ করে দিবে।")

# ৫. ইনপুট ও প্রসেসিং
sentence = st.text_input("আপনার আরবি বাক্যটি এখানে দিন:", placeholder="যেমন: نَصَرَ زَيْدٌ عَمْرًا")

if st.button("পূর্ণাঙ্গ তারকিব বের করুন"):
    if sentence:
        with st.spinner('AI বিশ্লেষণ করছে, দয়া করে ১০-১৫ সেকেন্ড অপেক্ষা করুন...'):
            try:
                # সুনির্দিষ্ট ইনস্ট্রাকশন
                prompt = f"""
                Analyze the Arabic sentence: '{sentence}'
                Task: Provide a complete 'Tarkib' (Syntactic Analysis) in Bengali.
                Format: 
                - Word-by-word analysis.
                - Grammatical roles (Fail, Maful, etc.).
                - Final Jumla type.
                Follow the standard Dars-e-Nizami or Madrasa method.
                """
                
                response = model.generate_content(prompt)
                
                st.markdown(f'<div class="arabic-font">{sentence}</div>', unsafe_allow_html=True)
                st.markdown('<div class="tarkib-box">', unsafe_allow_html=True)
                st.subheader("বিশ্লেষণ ফলাফল:")
                st.write(response.text)
                st.markdown('</div>', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"দুঃখিত, একটি টেকনিক্যাল সমস্যা হয়েছে। অনুগ্রহ করে নিশ্চিত করুন যে আপনার API Key টি সচল আছে।")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")
