import streamlit as st

st.title("anisnovianti")
st.write(
    "ini punya anis."
)
st.image("d5bd46347ff8022d4ab51895216282aa.jpg", width=200)

st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st. write(f"{angka} adalah Bilangan Ganjil")
