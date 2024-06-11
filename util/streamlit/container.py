import streamlit as st

class StreamLitContainerModule :

    def __init__(self) -> None:
        pass

    def get_container(self) :
        return st.container(border= True)