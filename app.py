import pandas as pd
import streamlit as st
from google import genai
from google.genai import types
client = genai.Client()
st.title('Chat with your CSV')
file = st.file_uploader('Upload a CSV file', type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())
    question = st.text_input('Ask a question about your data')
    if question:
        context = (
            'Columns: ' + ', '.join(df.columns) + '\n\n'
            'First 20 rows:\n' + df.head(20).to_string() + '\n\n'
            'Summary statistics:\n' + df.describe(include='all').to_string()
        )
        response = client.models.generate_content(
            model='gemma-4-26b-a4b-it',
            config=types.GenerateContentConfig(
                system_instruction='You are a data analyst. Answer using only the data given. Say so if the data is not enough.'
            ),
            contents=context + '\n\nQuestion: ' + question,
        )
        st.write(response.text)

