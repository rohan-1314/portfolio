import streamlit as st
from send_email import send_email

st.title('Contact Me')
with st.form(key='form'):
    user_email = st.text_input(label='Your Email:')
    raw_message = st.text_area('Your message:')
    message = f"""\
subject:new email from {user_email} 

from: {user_email}
{raw_message}
"""
    submit = st.form_submit_button('submit')
    if submit:
        send_email(message)
        st.info('Your email was sent successfully.')
