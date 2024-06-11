from .__init__ import *

# This is a class that renders a view for a case study
class CaseStudyView :

    def get_case_study_container_layout(self) :

        with streamlit_container.get_container() :

            streamlit_title.get_subheader("EURUSD 25th May 2021 - 25th June 2021")
            streamlit_title.get_caption("Created on 25th June 2021")
            streamlit_button.get_button(content='View', expanded=False)


    def render_view(self) :
        # Header Title
        streamlit_title.get_header("Case Study")

        # Space
        streamlit_title.get_space()

        # Render Case Study Layouts
        for idx in range(3) :
            self.get_case_study_container_layout()


        # New Case Study Button
        streamlit_button.get_button(content="New Case Study", expanded=True) 


    # Render View of Initialisation
    def __init__(self) -> None:
        self.render_view()


if __name__ == "__main__" :
    CaseStudyView()