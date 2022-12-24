import streamlit as st

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)
with col1:
    st.image('images/photo.jpeg')

with col2:
    st.title('Rohan Vagadiya')
    content = """
    Hi! I am Rohan and currently a student in 11th grade at the new tulip International school. I know HTML5,
    CSS3, Javascript and python. I love to read books and play squash.
    """
    st.info(content)
content2 = """
Below you can find some projects I have built. Feel free to contact me!
"""

st.write(content2)
