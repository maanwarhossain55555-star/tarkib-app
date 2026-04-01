import streamlit as st
import google.generativeai as genai

# ১. অ্যাপের কনফিগারেশন
st.set_page_config(page_title="Arabic Tarkib AI", layout="wide")

# ২. সরাসরি আপনার দেওয়া API Key ব্যবহার করা
# আপনার কী: AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o
genai.configure(api_key="AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o")

# ৩. ডিজাইন করার জন্য CSS (মাদরাসা নোটের মতো লুক)
st.markdown("""
    <style>
    .arabic-font { 
        font-size: 40px !important; 
        direction: rtl; 
        text-align: center; 
        font-family: 'Amiri', serif; 
        background-color: #f0f2f6; 
        padding: 25px; 
        border-radius: 15px; 
        border: 2px solid #2e7d32; 
        margin-bottom: 20px;
    }
    .tarkib-box { 
        border: 2px solid #1b5e20; 
        padding: 20px; 
        border-radius: 10px; 
        background-color: #ffffff; 
        line-height: 1.8;
        font-size: 18px;
    }
    .stButton>button {
        width: 100%;
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
        height: 3.5em;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 গ্লোবাল আরবি তারকিব অ্যানালাইজার (AI)")
st.write("যেকোনো আরবি বাক্য লিখুন, AI এটি বিশ্লেষণ করে মাদরাসা স্টাইলে তারকিব করে দেবে।")

# ৪. ইনপুট বক্স
sentence = st.text_input("আপনার আরবি বাক্যটি এখানে দিন:", placeholder="যেমন: نَصَرَ زَيْدٌ عَمْرًا")

if st.button("পূর্ণাঙ্গ তারকিব বের করুন"):
    if sentence:
        try:
            # ৫. AI কে সঠিক ইনস্ট্রাকশন দেওয়া
            model = genai.GenerativeModel('gemini-pro')
            prompt = f"""
            Analyze the following Arabic sentence and provide a detailed 'Tarkib' (Syntactic Analysis) in Bengali.
            Use traditional Madrasa style:
            1. Word by word analysis (Ism, Fil, Harf).
            2. Identifying relationships (Fail, Maful, Mudaaf, Shart, etc.).
            3. Final Jumla type.
            Sentence: {sentence}
            """
            
            with st.spinner('AI বিশ্লেষণ করছে, দয়া করে অপেক্ষা করুন...'):
                response = model.generate_content(prompt)
                
                # ফলাফল দেখানো
                st.markdown(f'<div class="arabic-font">{sentence}</div>', unsafe_allow_html=True)
                st.markdown('<div class="tarkib-box">', unsafe_allow_html=True)
                st.subheader("বিশ্লেষণ ফলাফল:")
                st.write(response.text)
                st.markdown('</div>', unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"দুঃখিত, একটি কারিগরি সমস্যা হয়েছে। দয়া করে কিছুক্ষণ পর চেষ্টা করুন।")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")
