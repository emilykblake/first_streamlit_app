import streamlit as st
import pandas as pd

st.title('New Diner Menu')

st.header('Br-egg-fast')
st.text('🐔 Eggs Benedict')
st.text('🐔 Eggs Florentine')
st.text('🐔 Eggs Royale')

st.header('Other Normal Breakfast Things')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv(r"https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)
