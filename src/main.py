import os

import streamlit as st

from doc_chat_util import get_answer

working_dir = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title="Chat with PDF",
    page_icon='0',
    layout='centered'
)

st.title("Document QnA - Llama3.1 - Ollama")

uploaded_file = st.file_uploader(label="Uplopad your file .. ", type=['pdf'])

user_query = st.text_input("Ask your question")


if st.button("Run"):
    bytes_data = uploaded_file.read()
    file_name = uploaded_file.name
    # Save the file to working directory
    file_path = os.path.join(working_dir,file_name)
    with open(file_path, 'wb') as f:
        f.write(bytes_data)

    answer =get_answer(file_name, user_query)

    st.success(answer)