import streamlit as st
st.title('Campusx')
col1, col2 = st.columns(2)

with col1:
    st.image("img.png")

with col2:
    st.write("""
    Hi, my name is Nitish. I am an educational content creator on YouTube with 150K+ Subscribers in the domain of 
    Data Science. I have been in the tech industry for the past 10 years and taught more than 50,000 students offline. 
    I am passionate about data and take pride in creating content that simplifies complex topics.
    """)

st.header('Coureses Offered')
st.subheader('Data Science')
st.subheader('Data Analysis')
st.subheader('Data Engineering')