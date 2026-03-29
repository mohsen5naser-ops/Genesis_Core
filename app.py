import streamlit as st
import pandas as pd
import requests

# إعدادات الصفحة العصرية
st.set_page_config(page_title="Genesis Sovereign UI", page_icon="🌐", layout="wide")

# التصميم الداكن
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: white; }
    .stButton>button { background-color: #38bdf8; color: white; border-radius: 20px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ مركز السيطرة الشاملة - Genesis")
st.write("مراقبة الكيان المستقل في السحابة")

# جلب البيانات من مستودعك (الرابط العالمي)
url = "https://raw.githubusercontent.com/mohsen5naser-ops/Genesis_Core/main/universal_knowledge.db"

try:
    response = requests.get(url)
    if response.status_code == 200:
        st.subheader("📊 سجل المعرفة المكتسبة")
        data = response.text.splitlines()[-5:] # عرض آخر 5 سجلات
        for entry in reversed(data):
            st.info(entry)
    else:
        st.warning("جاري مزامنة البيانات من السيرفر العالمي...")
except:
    st.error("فشل الاتصال بنواة GitHub")

# أزرار التحكم
st.sidebar.header("غرفة العمليات")
if st.sidebar.button("تحديث النواة الآن"):
    st.sidebar.success("تم إرسال أمر التحديث للسيرفر!")

if st.sidebar.button("إصدار مفتاح API جديد"):
    st.sidebar.warning("جاري توليد مفتاح سيادي...")

st.sidebar.markdown("---")
st.sidebar.write("الحالة: **نشط** 🟢")
