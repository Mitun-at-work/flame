import streamlit as st
import uuid

class StreamLitButtonModule :

    def __init__(self) -> None:
        pass

    def get_random_id(self) -> int:
        return uuid.uuid4().int 

    def get_button(self, content : str, expanded : bool = True) : 
        random_button_id = self.get_random_id()
        return st.button(content, use_container_width= expanded, key= random_button_id )
