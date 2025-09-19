import streamlit as st
st.title('Campusx')
col1, col2 = st.columns(2)

with col1:
    st.write('Hello world')

with col2:
    st.write("""
    Maruti Ertiga price for the base model starts at Rs. 10.40 Lakh and the top model price goes upto Rs. 15.72 Lakh 
    (on-road Bareilly). Ertiga price for 9 variants is listed below.
    """)