import streamlit as st


from util.directory.directory_assets import DirectoryAssets

dr = DirectoryAssets()

checklist = dr.return_content_from_file(dr.dir)


st.header('General Checklist')



with st.popover("Open popover"):
    name = st.text_area("New Checklist", height=400)
    if name :
        checklist = name
        dr.write_to_file(dr.dir, checklist)


for elem in checklist.split('\n'):
    st.checkbox(elem, key=elem)

