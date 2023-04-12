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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Lets add a select capability so we can choose fruit
fruits_selected = st.multiselect("Please select your fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the data on the page
st.dataframe(fruits_to_show)

# New section to display fruityvice api response
st.header('Fruityvice Fruit Advice!')
fruit_choice = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# take the json version of the response and normalize
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# output it on the screen as a table
st.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)
#
