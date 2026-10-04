import streamlit as st

# --- PRESENTATION LAYER: PAGE CONFIG ---
st.set_page_config(
    page_title="Pet Adoption Explorer",
    page_icon="🐾",
    layout="wide"
)

# --- SIDEBAR MENU ---
st.sidebar.title("🐾 Pet Adoption Explorer")
st.sidebar.caption("ระบบค้นหาและลงทะเบียนรับเลี้ยงสัตว์เลี้ยง")

menu = st.sidebar.radio(
    "เลือกเมนูการทำงาน:",
    ["หน้าแรก (Home)", "ค้นหาสัตว์เลี้ยง", "ยื่นคำขอรับเลี้ยง"]
)

# --- PAGE 1: HOME ---
if menu == "หน้าแรก (Home)":
    st.title("Welcome to Pet Adoption Explorer 🐶🐱")
    st.write("ยินดีต้อนรับสู่ระบบค้นหาและลงทะเบียนบ้านใหม่ให้สัตว์เลี้ยง")
    st.info("โปรเจกต์นี้พัฒนาตามสถาปัตยกรรม 3-Layer Architecture")

# --- PAGE 2: SEARCH (Input Validation DoD) ---
elif menu == "ค้นหาสัตว์เลี้ยง":
    st.title("🔍 ค้นหาสัตว์เลี้ยง")
    
    # Input Validation: .strip().lower()
    raw_input = st.text_input("ป้อนชื่อหรือสายพันธุ์ที่ต้องการค้นหา:")
    cleaned_keyword = raw_input.strip().lower()
    
    if cleaned_keyword:
        st.success(f"กำลังค้นหาด้วยคำว่า: '{cleaned_keyword}'")
    elif raw_input:
        st.warning("กรุณาป้อนข้อความที่ไม่ใช่ช่องว่าง")

# --- PAGE 3: ADOPTION FORM ---
elif menu == "ยื่นคำขอรับเลี้ยง":
    st.title("📝 ฟอร์มยื่นคำขอรับเลี้ยง")
    st.write("ระบบยื่นคำขอจะเปิดใช้งานใน Sprint 2-3")
