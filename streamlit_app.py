import streamlit as st

st.set_page_config(page_title="LINE Coupon System", layout="centered")

st.title("🎫 ระบบคูปองอาหาร")

# รับค่าจาก query string
params = st.query_params

user_id = params.get("userId")
display_name = params.get("name")
picture_url = params.get("pic")
action = (params.get("action") or "").lower()

# แสดงข้อมูลผู้ใช้
if user_id:
    st.success(f"✅ ยินดีต้อนรับ {display_name} (LINE ID: {user_id})")
    if picture_url:
        st.image(picture_url, width=100)
    st.markdown(f"🔍 ค่า action ที่ได้รับ: `{action}`")

    # เปลี่ยนเนื้อหาตาม action
    if action == "redeem":
        st.header("🍽 ใช้คูปอง")
        st.write("โปรดแสดงหน้าจอนี้ให้ร้านค้าสแกน QR หรือยืนยันสิทธิ์")
    elif action == "check":
        st.header("📊 ตรวจสอบคูปอง")
        st.write("ระบบกำลังดึงยอดคงเหลือหรือประวัติการใช้คูปอง...")
    elif action == "register":
        st.header("📝 ลงทะเบียนผู้ใช้ใหม่")
        st.write("กรุณากรอกข้อมูลเพื่อผูกบัญชี LINE กับระบบคูปอง")
    else:
        st.info("ℹ️ ไม่ทราบประเภทการใช้งาน")
else:
    st.warning("⚠️ กรุณาเข้าสู่ระบบผ่าน LINE LIFF ก่อน")
