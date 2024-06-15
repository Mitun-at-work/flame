import os
import uuid
import streamlit as st  
from model.case_study_model import CaseStudyModel
from constants.const import image_links
from time import sleep
from datetime import datetime


# Generates Case Study View
class CaseStudyView :

    def save_case_study(self, case_study_model : CaseStudyModel) :
        # Generate RandomId to store images and notes
        random_id = uuid.uuid4().int

        # Copying Image in the Case Study/ Random ID/ Image.png
        # Generate the destination folder link 
        destination_folder = f'{self.case_study_path}/{case_study_model.case_study}/{random_id}'

        # Creating a directory for storing data
        os.mkdir(destination_folder)

        with open(f'{destination_folder}/image.png', 'wb') as file :
            file.write(case_study_model.image_byte)

        # Storing the Text format in the Document Folder
        # Generate Folder Link

        # Create a title file
        with open(f'{destination_folder}/title.txt', 'w') as title : 
            title.write(f"{case_study_model.title} \n")

        # Create a Notes file
        with open(f'{destination_folder}/notes.txt', 'w') as notes : 
            notes.write(case_study_model.notes)

        # Create a Info file
        with open(f'{destination_folder}/info.txt', 'w') as info : 
            now = datetime.now()
            time = now.time()
            created_time = f'{time.hour} : {time.minute}'
            created_date = f'{now.year}/{now.month}/{now.day}'

            info.write(f'{created_date}\n')
            info.write(f'{created_time}\n')

    def render_view(self): 
        st.title("Case Study")
        st.text("")

        # Create a New Case Study
        col1, col2 = st.columns(2)

        with col1.popover(label='New Case Study') :
            # Name of Case Study
            case_study_name = st.text_input(label="Case Study Name")
            if case_study_name :
                # Verifying the Case Study Already exists
                if not case_study_name in os.listdir(f"{self.case_study_path}") :
                    # Creating new directory
                    os.mkdir(f"{self.case_study_path}/{case_study_name}")
                    st.rerun()
        
        if col2.button("Refresh") :
            st.rerun()

        st.divider()
        with st.popover(label="Save In") :
            study = st.selectbox(
                label= 'Case Study',
                options= self.case_studies,
            )

        files = ''
        # If Images were'nt selected Pick Image is Visible    
        if not image_links  : 
            files = st.file_uploader(accept_multiple_files= False, label= "File", type= '.png')
            if files : 
                # Upload the image links and refresh
                image_links.append(files)
                st.rerun()

        # Display Images when they are picked
        else : 
            for i in image_links :
                st.image(image= i)
            
            # Delete the Image, Refresh  and Displays the Picked Image
            if st.button(label="Delete") :
                image_links.pop()
                st.rerun()

        st.text("")

        # Case Study Title
        if  files != '' : return
        study_title = st.text_input("Title")

        # Case Study Notes
        study_notes = st.text_area(label="Notes")

        # Save Case Study Button
        if not (study_title and study_notes) : return

            # Verify the fields are not empty
        if study_notes and study_title and study and image_links: 

            # Generating Case Study Model 
            model = CaseStudyModel(
                case_study= study,
                image_byte= image_links[0].getbuffer(),
                notes= study_notes,
                title= study_title,
                date= '',
                time=''
                        )

            # Model passed to Save Function
            if st.button("Save Case Study") :
                self.save_case_study(case_study_model= model)
                st.success("Case Study Saved Sucessfully")
                sleep(2)
                image_links.pop()
                st.rerun()

    def __init__(self) -> None:

        # Initialise Case Study Paramters
        self.case_study_path = ".config/case"

        # Create Configuration FIles 
        if not 'case' in os.listdir('.config') :
            os.mkdir(self.case_study_path)
        
        self.case_studies = os.listdir(self.case_study_path)

# Rendering Case Study
if __name__ == '__main__' :
    CaseStudyView().render_view()