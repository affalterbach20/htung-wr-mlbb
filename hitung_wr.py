import streamlit as st
from PIL import Image
import math as m

st.title("Kalkulator Winrate Mobile Legends Bang Bang")
st.image("logoml.jpeg",width=430)
st.text("")

a = st.text_input("Masukkan total match anda: (contoh: 400)")
b = st.text_input("Masukkan total win rate anda: (contoh: 65.5)")
c = st.text_input("Masukkan win rate yang anda inginkan: (contoh: 80)")
tot_match = 0
tot_wr = 0
wr_ding = 0
if a > "0":
    tot_match = float(a)
if b > "0":
    tot_wr = float(b)
if c > "0":
    wr_ding = float(c)
tot_win = tot_match*(tot_wr/100)
tot_lose = tot_match*((100-tot_wr)/100)
sis_wr = 100-wr_ding
wr_dbt = 100/sis_wr
d = tot_lose*wr_dbt
tot = d-tot_match
tot_akhir = m.ceil(tot)
hitung = st.button("Hitung")
if hitung:
    if tot_match and tot_wr and wr_ding > 0:
        st.success(f"Anda harus memenang sebanyak = {tot_akhir} pertandingan tanpa kalah untuk mencapai win rate = {wr_ding}")
        st.success("Semoga beruntung!!")
        st.balloons()
    else:
        st.success("Anda harus mengisi (total match, total win rate, win rate yang anda inginkan) terlebih dahulu!!")
        
