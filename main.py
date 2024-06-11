import streamlit as st

st.title('Welcome to Flame!')

# Sample DataSet
statergy_name = ['Silver Bullet with FVG', 'Silver Bullet with IVFVG' ]
statergy_date = ['2019-05-05', '2025-05-20']

# Container with statergy name
for idx in range(2) :
    container = st.container(border=True)
    
    # Continue Tetsing
    container.write(f"{statergy_name[idx]}")
    container.write(f"Last Tested on {statergy_date[idx]}")

    container.button('Continue', key=idx)

# Create New Statergy
st.text(' ')
if st.button("Create New Statergy", use_container_width=True):
    st.switch_page("pages/strategy.py")