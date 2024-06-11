import streamlit as st  


if st.button("Home ❤️"):
   st.switch_page("main.py")

st.title("Create New BackTesting Strategy")


with st.form("my_form", clear_on_submit=True, border=10):

    name = st.text_input("Enter the title of the strategy", placeholder="Titile")

    account_size = st.text_input("Enter the Account Size", placeholder="Account Size",)

    description = st.text_area("Enter the description of the strategy", placeholder= 'Description')

    checklist = st.text_area("Enter the checklist", placeholder= 'Checklists', height=250)

    form_button = st.form_submit_button("Create Strategy", use_container_width=True)

    if form_button:
       if name and account_size and description and checklist:
        st.success("Strategy Created Successfully")
       else :
          st.error("Please fill the required fields")



class StatergyView :

   def __init__(self) -> None:
      pass