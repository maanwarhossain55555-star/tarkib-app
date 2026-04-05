import streamlit as st
import streamlit.components.v1 as components

# পেজ সেটআপ
st.set_page_config(page_title="ANWAR CALLIGRAPHY", layout="centered")

# ইন্টারফেস ডিজাইন (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.stButton > button {
        width: 100%; background-color: #1a73e8; color: white;
        font-weight: bold; border-radius: 8px; height: 3.5em; border: none;
    }
    .stTextArea textarea {
        border-radius: 10px; background-color: #161b22; color: white;
        border: 1px solid #30363d; text-align: right; font-size: 18px;
    }
    h1 { color: #ffffff; text-align: center; margin-bottom: 0px; }
    .sub-brand { text-align: center; color: #8b949e; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>ANWAR CALLIGRAPHY</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-brand'>Premium Arabic Calligraphy Generator</p>", unsafe_allow_html=True)

# টেক্সট ইনপুট
user_input = st.text_area("আপনার আরবি টেক্সট এখানে লিখুন:", placeholder="مثال: بسم الله الرحمن الرحيم", height=100)

# গুগল ফন্ট থেকে একটি সুন্দর ক্যালিগ্রাফি ফন্ট (Reem Kufi) ব্যবহার করা হয়েছে
# যাতে আপনার আর কোনো ফাইল আপলোড করতে না হয়
html_template = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <link href="https://fonts.googleapis.com/css2?family=Reem+Kufi:wght@700&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        body {{ background-color: #0e1117; margin: 0; display: flex; flex-direction: column; align-items: center; padding: 10px; }}
        #capture-area {{
            background-color: #000; padding: 80px 50px; border-radius: 15px;
            text-align: center; min-width: 600px; min-height: 250px;
            display: flex; justify-content: center; align-items: center;
            border: 1px solid #333; box-shadow: 0 25px 60px rgba(0,0,0,0.9);
        }}
        .calligraphy {{
            font-family: 'Reem Kufi', sans-serif; font-size: 100px; color: #FFFFFF;
            margin: 0; line-height: 1.2; text-shadow: 0 0 15px rgba(255,255,255,0.1);
        }}
        .download-btn {{
            margin-top: 30px; padding: 14px 50px; background-color: #238636;
            color: white; border: none; border-radius: 30px; cursor: pointer;
            font-size: 16px; font-weight: bold; transition: 0.3s;
        }}
        .download-btn:hover {{ background-color: #2ea043; }}
    </style>
</head>
<body>
    <div id="capture-area"><div class="calligraphy">{user_input}</div></div>
    <button class="download-btn" onclick="downloadImage()">Download HD Image</button>
    <script>
        function downloadImage() {{
            const area = document.getElementById('capture-area');
            html2canvas(area, {{ backgroundColor: "#000000", scale: 4 }}).then(canvas => {{
                let link = document.createElement('a');
                link.download = 'Anwar_Calligraphy.png';
                link.href = canvas.toDataURL();
                link.click();
            }});
        }}
    </script>
</body>
</html>
"""

if st.button("ডিজাইন তৈরি করুন"):
    if not user_input.strip():
        st.warning("আগে কিছু লিখুন!")
    else:
        components.html(html_template, height=600)

st.markdown("---")
st.caption("© 2026 ANWAR CALLIGRAPHY")
