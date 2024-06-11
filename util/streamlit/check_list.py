import streamlit as st


class StreamLitCheckListModule :

    def __init__(self) -> None:
        pass

    def get_check_box(self, content : str) :
        return st.checkbox(content, key=content)