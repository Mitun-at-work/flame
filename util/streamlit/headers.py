import streamlit as st

class StreamLitTextModule :

    def __init__(self) -> None:
        print("Header Title Initialised")

    def get_header(self, title) :
        return st.title(title)
    
    def get_subheader(self, title) :
        return st.subheader(title)
    
    def get_caption(self, title) :
        return st.caption(title)
    
    def get_text(self, title) -> st.text:
        return st.text(title)
    
    def get_space(self) -> get_text:
        return st.text(" ")
    