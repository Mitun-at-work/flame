import streamlit as st  

class CheckListView :

    def __init__(self) -> None:
        self.path = ".config/check_list.txt"

    def get_check_list(self) -> list:
        with open(self.path, 'r') as file : 
            content =  file.read()

        return content.split("\n")
    
    def update_check_list(self, content : str) : 
        with open(self.path, 'w') as file : 
            file.write(content)

    def render_view(self) :
        st.title("Check List")

        with st.popover('Edit', use_container_width= True,) as file :
            check_list = st.text_area(label='')
            if check_list : 
                self.update_check_list(content= check_list)

        st.title('')

        checks = self.get_check_list() 

        for idx in range(len(checks)):
            st.checkbox(label= checks[idx], key=f'{idx}')
            st.divider()

if __name__ == "__main__" :
    CheckListView().render_view()