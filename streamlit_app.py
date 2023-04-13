import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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

# create a repeatable code block (function)
def get_fruityvice_response(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

# New section to display fruityvice api response
st.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_response(fruit_choice)
    st.dataframe(back_from_function)
except URLError as e:
  st.error()

st.header("The fruit load list contains:")
# snowflake related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("Select * from fruit_load_list")
    return my_cur.fetchall()
  
# add a button to load the fruit
if st.button("Get Fruit Load List"):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = my_cur.fetchall()
  st.dataframe(my_data_rows)
  
# dont run anything past here while we troubleshoot
st.stop()

# allow user to add a fruit to the list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return "thanks for adding" + new_fruit

add_my_fruit = st.text_input("What fruit would you like to add?")
if st.buttom("Add a Fruit to the List"):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  st.text(back_from_function)
