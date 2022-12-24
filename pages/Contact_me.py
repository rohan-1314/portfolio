import streamlit as st

st.title('Contact Me')
with st.form(key='form'):
    email_add = st.text_input(label='Your Email:')
    message= st.text_area('Your message:')
    submit = st.form_submit_button('submit')