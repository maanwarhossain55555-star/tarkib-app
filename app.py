import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(page_title="Marhaban Calligraphy Creator", layout="centered")

# ফন্ট ফাইলটি লোড করার ফাংশন
def get_font_base64(font_path):
    with open(font_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ফন্ট ফাইলের নাম নিশ্চিত করুন (আপনার আপলোড করা ফাইল অনুযায়ী)
font_filename = "MarhabanArabicDEMO-Bold.otf" 

# ফন্টটি যদি একই ফোল্ডারে থাকে তবে এটি কাজ করবে
if os.path.exists(font_filename):
    font_base64 = get_font_base64(font_filename)
else:
    # ফাইল না পেলে এরর এড়াতে খালি রাখা হলো
    font_base64 = ""
    st.warning("ফন্ট ফাইলটি পাওয়া যায়নি। অনুগ্রহ করে নিশ্চিত করুন যে 'MarhabanArabicDEMO-Bold.otf' ফাইলটি আপনার GitHub-এর মূল ফোল্ডারে আছে।")

st.markdown("<h2 style='text-align: center; color: white;'>Marhaban Arabic Calligraphy</h2>", unsafe_allow_html=True)

user_input = st.text_area("আরবি লিখুন:", placeholder="مثال: الجامعیة الغفوریة...", height=100)

html_template = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        @font-face {{
            font-family: 'Marhaban';
            src: url(data:font/opentype;base64,{font_base64});
        }}
        
        body {{ 
            background-color: #0e1117; 
            margin: 0; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
        }}
        
        #capture-area {{
            background-color: #000;
            padding: 60px 100px;
            border-radius: 15px;
            text-align: center;
            width: fit-content;
            margin-top: 20px;
            border: 1px solid #333;
        }}

        .calligraphy {{
            font-family: 'Marhaban', sans-serif;
            font-size: 100px;
            color: #FFFFFF;
            line-height: 1.2;
            margin: 0;
            white-space: nowrap;
            /* হালকা ৩D শ্যাডো যা লেখাকে নষ্ট করবে না */
            text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
        }}

        .btn-download {{
            margin-top: 30px;
            padding: 12px 30px;
            background-color: #1e88e5;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }}
    </style>
</head>
<body>

    <div id="capture-area">
        <p class="calligraphy">{user_input}</p>
    </div>

    <button class="btn-download" onclick="downloadImage()">Download HD Photo</button>

    <script>
        function downloadImage() {{
            const area = document.getElementById('capture-area');
            html2canvas(area, {{ 
                backgroundColor: "#000000",
                scale: 3 
            }}).then(canvas => {{
                let link = document.createElement('a');
                link.download = 'marhaban_calligraphy.png';
                link.href = canvas.toDataURL();
                link.click();
            }});
        }}
    </script>
</body>
</html>
"""

if st.button("ডিজাইন তৈরি করুন"):
    if user_input.strip() == "":
        st.error("অনুগ্রহ করে কিছু লিখুন!")
    else:
        components.html(html_template, height=550)
