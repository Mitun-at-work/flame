import streamlit as st

class HackView :

    def __init__(self) : 
        # st.set_page_config(layout="wide")
        pass



    def render_view(self) :
        st.title('Progress')
        st.subheader('')

        monthly = st.file_uploader('Monthly MarkUp')
        st.subheader('')

        weekly = st.file_uploader('Weekly MarkUp')
        st.subheader('')

        daily = st.file_uploader('Daily MarkUp')
        st.subheader('')

        divergence = st.file_uploader('Divergence Mark Ups')
        st.subheader('')

        with st.popover('Save', use_container_width= True) :
            st.text_input('Instrument Name')

 


if __name__ == '__main__' :
    HackView().render_view()