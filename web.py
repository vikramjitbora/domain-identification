import glob
import os
import pandas as pd
import streamlit as st

from functions import get_dataframe, get_sentences

NUM_SENT = 3
FILEPATHS = glob.glob('Hindi Dataset/train/*.txt')
DOMAINS = ('Select', 'Politics', 'Sports', 'International', 'Local', 'India')

# Read in an existing dataframe of data and labels or create one
df = get_dataframe()

st.title('Domain Identification for NLP')

try:
    filepath = FILEPATHS[0]
    with open(filepath, encoding='utf-8') as file:
        text = file.read()
        # Extract sentences from the text
        with st.form(filepath, clear_on_submit=True):
            display = get_sentences(text, NUM_SENT)
            st.text_area('Text to analyse', display)

            label = st.selectbox(
                'Please select the right category for above text',
                DOMAINS, index=0
            )
            if label != 'Select':
                st.write('You selected: ', label)

            submitted = st.form_submit_button("Submit")
            if submitted:
                if display in df['data'].values:
                    df.loc[df.data == display, 'labels'] = label
                else:
                    new_row = {'data': [display], 'labels': [label]}
                    df = pd.concat([df, pd.DataFrame(new_row)], ignore_index=True)
    df.to_csv('data.csv', index=False)

    next_button = st.button('Next')
    if next_button:
        if display in df['data'].values:
            os.remove(filepath)
        st.experimental_rerun()
except IndexError:
    st.write('Data files are not present in your location')
