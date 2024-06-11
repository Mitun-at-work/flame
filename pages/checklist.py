import streamlit as st

st.header('General Checklist')


st.title('')


month = st.checkbox('Monthly Bias', key='mb')
week = st.checkbox('Weekly Bias', key='wb')
daily = st.checkbox('Daily Bias', key='db')
dol = st.checkbox('Draw on Liquidity', key='robot')
dealing_range = st.checkbox('Dealing Range', key='dr')
high = st.checkbox('HTF High/Low Taken', key='htf')
pd = st.checkbox('Mark PD Arrays', key='pd')
cisd = st.checkbox('CISD in LTF', key='cisd')

if month and week and daily and dol and dealing_range and high and cisd and pd:
    st.success("Wait For an Entry")



