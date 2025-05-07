import streamlit as st

st.set_page_config(page_title="LINE LIFF Profile", layout="centered")

st.title("👤 ข้อมูลผู้ใช้จาก LINE LIFF")

user_id = st.experimental_get_query_params().get("userId", [None])[0]

if user_id:
    st.success(f"✅ คุณเข้าสู่ระบบด้วย LINE แล้ว\n\n🆔 LINE User ID: `{user_id}`")
else:
    st.warning("⚠️ ไม่พบข้อมูลผู้ใช้ กรุณาเข้าสู่ระบบผ่าน LINE LIFF ก่อน")
