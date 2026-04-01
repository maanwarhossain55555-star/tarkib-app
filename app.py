import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Arabic Tarkib AI", layout="wide")

# এখানে আপনার নতুন তৈরি করা API Key-টি বসান
API_KEY = "আপনার_নতুন_এপিআই_কী_এখানে_দিন" 

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"API কনফিগারেশন এরর: {e}")

st.title("🌍 গ্লোবাল আরবি তারকিব অ্যানালাইজার (AI)")

user_input = st.text_input("আরবি বাক্যটি লিখুন:", placeholder="যেমন: نَصَرَ زَيْدٌ عَمْرًا")

if st.button("পূর্ণাঙ্গ তারকিব বের করুন"):
    if user_input:
        with st.spinner('AI বিশ্লেষণ করছে...'):
            try:
                prompt = f"Analyze the Arabic sentence '{user_input}' and provide a detailed Tarkib in Bengali following Madrasa tradition."
                response = model.generate_content(prompt)
                
                if response.text:
                    st.success("বিশ্লেষণ সম্পন্ন!")
                    st.write(response.text)
                else:
                    st.error("AI কোনো ফলাফল তৈরি করতে পারেনি।")
            except Exception as e:
                # এখানে এরর মেসেজটি দেখা যাবে
                st.error(f"দুঃখিত, সমস্যাটি হলো: {str(e)}")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")
