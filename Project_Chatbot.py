import streamlit as st

st.set_page_config(page_title="Chatbot")
st.title("Chatbot")
st.write("Tulis namamu di bawah ini untuk lanjut...")

nama_pembuat = "Aby", "Abyan", "Abyansyah", "aby", "abyan", "abyansyah"
jawaban = st.text_input("Siapa namamu?")

if jawaban:
    jawaban_bersih = jawaban.strip().lower()
    
    if jawaban_bersih == nama_pembuat:
        st.warning("Itu nama pembuat botnya, coba jawab ulang pakai namamu sendiri!")
    else:
        st.markdown(f"Chatbot: Hai **{jawaban.capitalize()}**, satu kata buat kamu... **KAMEL.**")