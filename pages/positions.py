import streamlit as st  
import pandas as pd


class PositionView :

    def __init__(self) :
        self.df = pd.read_csv(".config/entry.csv")

        self.df.add('EURUSD')

    def render_view(self) :
        col1, col2, col3 = st.columns(3)

        col1.button('Home', key='Home')
        col2.button('Analytics', key='Analytics')
        col3.button('Check List', key='Check List') 


        st.write(' ')
        st.header('ICT Silver Bullet')


        with st.form("my_form", clear_on_submit=True, border=10):


            instrument = st.selectbox(
            "Instrument",
            ("EURUSD", "JPYUSD", "BTCUSDT"))


            order_type = st.selectbox(
                "Order Type",
                ['Buy','Sell']
            )

            entry = st.number_input("Entry Price", format="%.4f", key='entry')

            target = st.number_input("Target Pips", min_value= 10, max_value= 1000, key='target')
            
            sl = st.number_input("Stop Pips", min_value= 10, max_value= 1000, key='Stop')

            closed_price = st.number_input("Closed Pips",min_value= -1 * sl, max_value= target ** 2 ,step=1, key='closed_price')

            date = st.date_input("Date", key='date')

            session = st.selectbox(
                "Session",
                ['Asian','London', 'New York AM', 'New York PM']
            )

            quality = st.selectbox(
                "Quality",
                ['A+','A', 'B']
            )

            profit = st.text_input("Profit", key='profit')



            description = st.text_area("Description", key='description')


            files = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'], key='image', accept_multiple_files=True)


            form_button = st.form_submit_button("Create", use_container_width=True)


            if instrument and order_type and entry and target and  sl and closed_price and date and session and quality and profit and description and files and form_button :

                st.success("Sucess")
                self.df.add(instrument)

            else :
                st.warning("Complete Fields")
            
            st.write(self.df)



if __name__ == "__main__" :
    PositionView().render_view()



