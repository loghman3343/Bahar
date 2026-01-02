import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bahar System", layout="wide")

if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🔐 ورود به سیستم بهار")
    user = st.text_input("نام کاربری")
    pw = st.text_input("رمز عبور", type="password")
    if st.button("ورود"):
        if user == "admin" and pw == "1234":
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("اشتباه است")
else:
    st.title("🗓️ سامانه هوشمند چیدمان شیفت")
    st.success("خوش آمدید! کد بهار با موفقیت لود شد.")
    # بقیه کد اینجا اجرا می‌شود
