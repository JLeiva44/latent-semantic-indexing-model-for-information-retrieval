import string
import nltk
from nltk.corpus import stopwords
import re
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

def remove_html(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'',text)
     

def romove_url(text):     
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'',text)

def convert_to_lower_case(text : str):
    lower_case_text= text.lower()
    return lower_case_text

def remove_numbers(text):
    numbers = re.compile('\d+')
    return numbers.sub('',text)    

def remove_unnecesary_punctuation(text):
    unnecesary_punctuations = re.compile('[^\w\s]')
    return unnecesary_punctuations.sub(r'',text)

# def remove_white_spaces(text:str): # ver esto
#     no_space_text = text.strip()
#     return no_space_text

def remove_stop_words(text):
    stop_w = set(stopwords.words('english'))
    words = {word for word in text.split() if word not in stop_w}
    return words 

    
def remove_white_spaces(text):
    white_space = re.compile(r' ')
    return white_space.sub('',text)




