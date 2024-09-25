import re
import string
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

stop_words = stopwords.words("english")
custom_stopwords = ['c', 'u', 'hor', 'lar']
stop_words = stop_words + custom_stopwords
ps = PorterStemmer()


def clean_text(text):
    """Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers."""
    # remove html tags
    text = re.sub('<.*?>+', '', text)
    # lowercase the text
    text = str(text).lower()
    # remove text inside []
    text = re.sub('\[.*?\]', '', text)
    # remove links
    text = re.sub('https?://\S+|www\.\S+', '', text)
    # remove punctuations
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    # remove
    text = re.sub('\n', '', text)
    # remove the numbers
    text = re.sub(r'\d+', '', text)
    return text

# stopword removal function
def remove_stopwords(text):
    words = text.split()
    # Filter out stopwords
    filtered_text = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_text)


# function for stemming
def stemming(text):
    text = ' '.join(ps.stem(word) for word in text.split(' '))
    return text


# All preprocessing at one place
def preprocess(text):
    text = clean_text(text)
    text = remove_stopwords(text)
    text = stemming(text)
    return text
