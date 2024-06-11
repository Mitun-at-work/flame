import random
import streamlit as st


st.title('ICT Silver Bullet')
st.write('')
col1, col2, col3, col4 = st.columns(4)

col1.metric('Total Trades', 100)
col2.metric('Win Rate', '50%')
col3.metric('Avg. Win', '$1000')
col4.metric('Avg. Loss', '$500')


principal = 100 * 1000
profit_curve = [principal + random.randint(-5000, 5000) for x in range(15)]
profits = []
st.text('')

for idx in range(1, len(profit_curve)) :
    profits.append(profit_curve[idx] - profit_curve[idx - 1])


my_expander = st.expander(label='Analytics')



my_expander.text('Account Curve')

my_expander.line_chart(profit_curve,
              use_container_width=True,
              height= 500,
              )

my_expander.subheader('Profit Stat')
my_expander.bar_chart(profits)
