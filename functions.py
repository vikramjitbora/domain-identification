import pandas as pd
import re


def get_dataframe(file='data.csv'):
    """
    This will read an existing dataframe from location mentioned in file. If
    file path doesnt exist, it will create a dataframe with 'data' and 'labels'
    columns
    :param file: file path to read the dataframe if it exists
    :return: Pandas Dataframe object
    """
    try:
        data = pd.read_csv('data.csv')
    except FileNotFoundError:
        data = pd.DataFrame(columns=['data', 'labels'])
    return data


def get_sentences(text_data, number_sentences):
    """
    Function to get number of sentences from the data. If number entered is greater
    than total number of sentences, it will return the entire paragraph
    :param text_data: A paragraph of text data
    :param number_sentences: Number of sentences to extract (Int)
    :return: A string object with the required number of sentences
    """
    sentences = re.split(r' *[।?!]', text_data)
    sentences = [sentence.replace('\n', '') for sentence in sentences]
    if len(sentences) < number_sentences:
        return '।'.join(sentences)
    else:
        return '।'.join(sentences[:number_sentences])
