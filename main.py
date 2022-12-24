import streamlit as st

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)
import pandas as pd

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
df = pd.read_csv("data.csv", sep=';')
st.write(content2)
col3,empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[source code]({row['url']})")
