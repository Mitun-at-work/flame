from .__init__ import *


class CheckListView :

    def __init__(self) -> None:
        self.page_title = 'General Checklist'
        self.check_list_content = streamlit_directory.return_content_from_file(streamlit_directory.dir)
        self.check_list_points = self.check_list_content.split('\n')


    def generate_check_list(self, content : str) : 
        streamlit_directory.write_to_file(streamlit_directory.dir, content)

    def update_check_list(self, content : str) : 
        self.check_list_points = content.split('\n')

    def render_view(self) : 
        streamlit_title.get_subheader(self.page_title)

        for check_point in self.check_list_points : 
            streamlit_check_list.get_check_box(content= check_point)   

        
        # with st.popover("Open popover"):
        #     name = st.text_area("New Checklist", height=400)
        #     if name :
        #         checklist = name
        #         dr.write_to_file(dr.dir, checklist)


if __name__ == '__main__' :
    print("Called")
    CheckListView().render_view()