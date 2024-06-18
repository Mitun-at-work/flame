import streamlit as st
from os import listdir, removedirs
from constants.const import case_study_folder
from model.case_study_model import CaseStudyModel



class Study:
    
    def __init__(self) -> None:
        # Initialising Folder Path
        self.case_folder_path = '.config/case'
        self.case_folder = listdir(self.case_folder_path)

    def get_content(self, folder_link : str) -> CaseStudyModel:

        with open(f'{folder_link}/title.txt') as title :
            case_title = title.read()

        with open(f'{folder_link}/notes.txt') as note :
            case_content = note.read()

        with open(f'{folder_link}/info.txt') as info :
            case_info = info.read().split('\n')
            case_date = case_info[0]
            case_time = case_info[1]
        
   
        
        model = CaseStudyModel(
            title= case_title,
            notes= case_content,
            image_byte= f"{folder_link}/image.png",
            case_study= folder_link,
            date= case_date,
            time= case_time
        )

        return model
    
    def ren(self, file_link) :
        print(file_link)

    def render_view(self) :
        # Title of the Page
        st.title("Research")

        if not self.case_folder : 
            st.title("Nothing Here") 
            return
        
        # Selecting the Study Folder
        folder = st.selectbox('Study',
                        options= self.case_folder,
                        label_visibility= 'hidden',
                        ) 

        # Case File Link
        case_files_link = f"{self.case_folder_path}/{folder}"
        
        if st.button('Delete') :
            for i in case_files_link :
                removedirs(f'{case_files_link}/{i}')

        # Folders with Random ID
        files = listdir(case_files_link)

        # Generate View
        for folder in listdir(f'{case_files_link}') :

            case_study = self.get_content(f"{case_files_link}/{folder}")
            case_study_container = st.container(border= True)
            case_study_container.title(case_study.title)
            case_study_container.caption(f'Created On {case_study.date} \n {case_study.time}')
            case_study_container.image(case_study.image_byte)
            case_study_container.subheader(case_study.notes)

if __name__ == '__main__' :
    Study().render_view()