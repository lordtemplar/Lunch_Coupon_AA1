import streamlit as st

st.set_page_config(page_title="LINE LIFF Profile", layout="centered")

st.title("👤 ข้อมูลผู้ใช้จาก LINE LIFF")

params = st.query_params  # ✅ อัปเดตแล้ว

user_id = params.get("userId")
display_name = params.get("name")
picture_url = params.get("pic")

if user_id:
    st.success("✅ คุณเข้าสู่ระบบด้วย LINE แล้ว")
    st.markdown(f"🆔 **LINE User ID:** `{user_id}`")

    if display_name:
        st.markdown(f"👤 **Display Name:** `{display_name}`")
    if picture_url:
        st.image(picture_url, width=150)
else:
    st.warning("⚠️ ไม่พบข้อมูลผู้ใช้ กรุณาเข้าสู่ระบบผ่าน LINE LIFF ก่อน")
