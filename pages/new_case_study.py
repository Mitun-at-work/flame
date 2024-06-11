import streamlit as st  

st.set_page_config(page_title="Case Study", page_icon=":moneybag:", layout="wide")
if st.button("Back"):
   st.switch_page("pages/case_study.py")

st.title("Create New BackTesting Strategy")
st.write('')
case_study_name = st.text_input("Strategy Name")
st.write('')

col1, col2 = st.columns(2)
st.write('')

# col1.success("Bullish")
col1.markdown("Monthly Mark Ups")
monthly = col1.file_uploader("Monthly")
if monthly : st.image(monthly)




# col2.success("Bullish")
col2.write("Weekly Mark Ups")
weekly = col2.file_uploader("Weekly File")



col1.write('Daily Mark Ups')
daily = col1.file_uploader("Daily File")

st.write('')

# col2.write("Monthly Mark Ups")
# col2.file_uploader("Monthly File")


col2.write('DXY Mark Ups')
dxy = col2.file_uploader("DXY File")

st.button("Create Strategy", key="create_strategy", use_container_width=True)