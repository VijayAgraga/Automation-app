# app/app.py

import streamlit as st
from scripts import script1, script2

st.set_page_config(page_title="Automation Scripts GUI")

def main_page():
    st.title('Automation Scripts GUI')
    st.subheader('Select a script to run')

    # Create a grid layout for the cards
    cols = st.columns(3)

    with cols[0]:
        if st.button('Script 1'):
            st.session_state.page = 'script1'
    with cols[1]:
        if st.button('Script 2'):
            st.session_state.page = 'script2'
    with cols[2]:
        if st.button('Script 3'):
            st.session_state.page = 'script3'

def script1_page():
    st.title('Script 1')
    param1 = st.text_input('Enter parameter 1')
    param2 = st.text_input('Enter parameter 2')
    if st.button('Run Script 1'):
        result = script1.run(param1, param2)
        st.write(result)
    if st.button('Back'):
        st.session_state.page = 'main'

def script2_page():
    st.title('Script 2')
    uploaded_file = st.file_uploader('Upload a file')
    if uploaded_file and st.button('Run Script 2'):
        result = script2.run(uploaded_file)
        st.write(result)
    if st.button('Back'):
        st.session_state.page = 'main'

def script3_page():
    st.title('Script 3')
    st.write("Script 3 is not yet implemented.")
    if st.button('Back'):
        st.session_state.page = 'main'

# Routing
if 'page' not in st.session_state:
    st.session_state.page = 'main'

if st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'script1':
    script1_page()
elif st.session_state.page == 'script2':
    script2_page()
elif st.session_state.page == 'script3':
    script3_page()

#changes
