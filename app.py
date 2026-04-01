import streamlit as st
import google.generativeai as genai

# ১. সরাসরি আপনার API Key এবং মডেল সেটআপ
API_KEY = "AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o"
# এটি সরাসরি আমার (Gemini) লেটেস্ট এবং সবচেয়ে ফাস্ট ভার্সন
MODEL_NAME = "gemini-1.5-flash" 

# ২. পেজ ডিজাইন (একদম ক্লিন এবং প্রফেশনাল)
st.set_page_config(page_title="Arabic Tarkib AI", layout="centered")
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stTextInput>div>div>input { font-size: 20px; text-align: right; direction: rtl; }
    .stButton>button { background-color: #008000; color: white; width: 100%; border-radius: 10px; height: 50px; font-size: 18px; }
    .tarkib-box { background-color: #f0fdf4; padding: 20px; border-radius: 15px; border-left: 8px solid #008000; font-size: 18px; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

st.title("🟢 সরাসরি আরবি তারকিব অ্যানালাইজার (AI)")
st.write("নিচে আপনার আরবি বাক্যটি লিখুন। সরাসরি Gemini AI আপনাকে তারকিব করে দিবে।")

# ৩. ইনপুট বক্স
user_sentence = st.text_input("", placeholder="যেমন: نَصَرَ زَيْدٌ عَمْرًا")

if st.button("তারকিব বের করুন"):
    if user_sentence:
        with st.spinner('সরাসরি AI এর সাথে সংযোগ করা হচ্ছে...'):
            try:
                # সরাসরি কনফিগারেশন
                genai.configure(api_key=API_KEY)
                model = genai.GenerativeModel(MODEL_NAME)
                
                # সরাসরি আমার (AI) কাছে আপনার প্রশ্ন পাঠানো
                prompt = f"""
                You are an expert Arabic grammarian. 
                Analyze the sentence: '{user_sentence}'
                Provide a complete and detailed 'Tarkib' (Syntactic Analysis) in Bengali.
                Follow the standard Madrasa (Dars-e-Nizami) style. 
                Break down each word's role (Fail, Fail, Maful, etc.) and mention the final Jumla type.
                """
                
                response = model.generate_content(prompt)
                
                # রেজাল্ট দেখানো
                st.success("বিশ্লেষণ সম্পন্ন!")
                st.markdown(f'<div class="tarkib-box">{response.text}</div>', unsafe_allow_html=True)
                
            except Exception as e:
                # যদি এরর আসে তবে সেটিও সরাসরি দেখাবে
                st.error(f"যান্ত্রিক ত্রুটি: {str(e)}")
                st.info("টিপস: আপনার API Key-টি Google AI Studio থেকে পুনরায় চেক করুন।")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")

st.markdown("---")
st.caption("আপনার এই অ্যাপটি এখন সরাসরি Google Gemini AI দ্বারা পরিচালিত।")
