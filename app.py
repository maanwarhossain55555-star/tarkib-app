import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# পেজ টাইটেল এবং কনফিগারেশন
st.set_page_config(page_title="ANWAR CALLIGRAPHY", layout="centered")

# ফন্ট লোড করার ফাংশন
def get_font_base64(font_path):
    try:
        if os.path.exists(font_path):
            with open(font_path, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()
    except Exception:
        return None
    return None

# ফন্ট ফাইলের নাম (নিশ্চিত করুন এটি আপনার মূল ডিরেক্টরিতে আছে)
font_filename = "MarhabanArabicDEMO-Bold.otf" 
font_base64 = get_font_base64(font_filename)

# ইন্টারফেস টাইটেল
st.markdown("<h1 style='text-align: center; color: white;'>ANWAR CALLIGRAPHY</h1>", unsafe_allow_html=True)

user_input = st.text_area("আরবি টেক্সট লিখুন:", placeholder="مثال: بسم الله الرحمن الرحيم", height=100)

if not font_base64:
    st.error(f"'{font_filename}' ফাইলটি পাওয়া যায়নি। দয়া করে ফাইলটি আপনার GitHub রিপোজিটরিতে আপলোড করুন।")

# ক্যালিগ্রাফি টেমপ্লেট
html_template = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        @font-face {{
            font-family: 'AnwarMarhaban';
            src: url(data:font/opentype;base64,{font_base64 if font_base64 else ""});
        }}
        
        body {{ 
            background-color: #0e1117; 
            margin: 0; 
            display: flex; 
            flex-direction: column; 
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}
        
        #capture-area {{
            background-color: #000;
            padding: 70px;
            border-radius: 15px;
            text-align: center;
            min-width: 650px;
            min-height: 320px;
            display: flex;
            justify-content: center;
            align-items: center;
            border: 2px solid #333;
            box-shadow: 0 15px 35px rgba(0,0,0,0.6);
        }}

        .calligraphy {{
            font-family: 'AnwarMarhaban', serif;
            font-size: 130px;
            color: #FFFFFF;
            margin: 0;
            padding: 0;
            line-height: 0.7; /* Marhaban ফন্টের গ্যাপ কমানোর জন্য */
            display: inline-block;
            text-shadow: 0 0 15px rgba(255,255,255,0.15);
        }}

        .download-btn {{
            margin-top: 30px;
            padding: 15px 45px;
            background-color: #1a73e8;
            color: white;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-size: 18px;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        .download-btn:hover {{
            background-color: #1557b0;
            transform: translateY(-2px);
        }}
    </style>
</head>
<body>

    <div id="capture-area">
        <div class="calligraphy">{user_input}</div>
    </div>

    <button class="download-btn" onclick="downloadImage()">Download HD Design</button>

    <script>
        function downloadImage() {{
            const area = document.getElementById('capture-area');
            html2canvas(area, {{ 
                backgroundColor: "#000000",
                scale: 4, /* সর্বোচ্চ ক্লিয়ার ইমেজের জন্য */
                useCORS: true
            }}).then(canvas => {{
                let link = document.createElement('a');
                link.download = 'Anwar_Calligraphy_Design.png';
                link.href = canvas.toDataURL("image/png");
                link.click();
            }});
        }}
    </script>
</body>
</html>
"""

if st.button("ডিজাইন দেখুন"):
    if user_input.strip() == "":
        st.warning("আগে কিছু আরবি লিখুন!")
    else:
        components.html(html_template, height=650)

st.markdown("---")
st.caption("© 2026 ANWAR CALLIGRAPHY | High-Quality Arabic Typography")
