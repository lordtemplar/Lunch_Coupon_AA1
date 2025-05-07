import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="LINE LIFF Profile", layout="centered")

st.title("👤 ข้อมูลจาก LINE LIFF")
st.markdown("หน้านี้จะแสดงข้อมูลผู้ใช้งานจาก LINE LIFF เมื่อลิงก์จาก Rich Menu")

# อ่าน LIFF_ID จาก secrets
LIFF_ID = st.secrets["LIFF_ID"]

# ฝัง LIFF_ID ลงใน HTML template
with open("liff_component.html", "r", encoding="utf-8") as f:
    liff_html = f.read().replace("{{LIFF_ID}}", LIFF_ID)

components.html(liff_html, height=600)
