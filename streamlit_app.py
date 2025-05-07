import streamlit as st

st.set_page_config(page_title="LINE Coupon System", layout="centered")

params = st.query_params
user_id = params.get("userId")
display_name = params.get("name")
picture_url = params.get("pic")
action = params.get("action", "none")  # ได้ค่ามาจาก Rich Menu

st.title("🎫 ระบบคูปองอาหาร")

if user_id:
    st.success(f"✅ ยินดีต้อนรับ {display_name} (LINE ID: {user_id})")
    if picture_url:
        st.image(picture_url, width=100)

    st.markdown(f"🧭 **คุณกดเข้ามาจากปุ่ม:** `{action}`")

    if action == "use":
        st.header("🍽 ใช้คูปอง")
        # ... แสดง QR หรือระบบให้ร้านค้าตรวจสอบ
    elif action == "check":
        st.header("📊 ตรวจสอบคูปองของคุณ")
        # ... แสดงยอดคงเหลือหรือประวัติ
    elif action == "register":
        st.header("📝 ลงทะเบียนผู้ใช้ใหม่")
        # ... แบบฟอร์มสมัครสมาชิก / ผูก LINE ID
    else:
        st.info("ℹ️ ไม่ทราบประเภทการใช้งาน")
else:
    st.warning("⚠️ กรุณาเข้าสู่ระบบผ่าน LINE LIFF ก่อน")
