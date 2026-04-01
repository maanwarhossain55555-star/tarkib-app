import streamlit as st
import google.generativeai as genai

# সরাসরি আপনার API Key
API_KEY = "AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o"

# সরাসরি সংযোগ পদ্ধতি
try:
    genai.configure(api_key=API_KEY)
    # এখানে কোনো ভার্সন ছাড়াই সরাসরি মডেল সেটআপ
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"এআই সংযোগে সমস্যা: {e}")

st.set_page_config(page_title="Arabic Tarkib AI")
st.title("🟢 সরাসরি আরবি তারকিব অ্যানালাইজার (AI)")

user_input = st.text_input("আরবি বাক্যটি লিখুন:")

if st.button("তারকিব বের করুন"):
    if user_input:
        with st.spinner('সরাসরি AI বিশ্লেষণ করছে...'):
            try:
                # সরাসরি আমার কাছে নির্দেশ পাঠানো
                prompt = f"Analyze the Arabic sentence: '{user_input}' and provide a detailed Tarkib in Bengali following Madrasa tradition."
                response = model.generate_content(prompt)
                
                if response.text:
                    st.success("বিশ্লেষণ সম্পন্ন!")
                    st.write(response.text)
            except Exception as e:
                # এররটি পরিষ্কারভাবে দেখাবে
                st.error(f"যান্ত্রিক ত্রুটি: {str(e)}")
    else:
        st.warning("আগে একটি বাক্য লিখুন।")
