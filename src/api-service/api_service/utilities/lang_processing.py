"""Language Processing Utilities."""
import string
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk import FreqDist

special_chars = "'´`–``’"
punctuation = string.punctuation + special_chars


def clean_data(sentence):
    """
    Clean the passed data.

    Split data into tokens, lemmatize tokens to get the word-stem of the token and
    finally remove punctuations and frequently used stop_words.
    ``stopwords.words("english")`` as default

    :param sentence: {string} - string of words and characters
    :return: {dict} cleaned_tokens - clean list of tokens
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = stopwords.words("english")
    cleaned_tokens = []

    tokenized_sentence = word_tokenize(sentence)

    for token, tag in pos_tag(tokens=tokenized_sentence):
        if tag.startswith("NN"):
            pos = "n"
        elif tag.startswith("VB"):
            pos = "v"
        else:
            pos = "a"

        token = lemmatizer.lemmatize(token, pos)

        if token not in punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token)

    return cleaned_tokens


def top_ten_words(sentence):
    """
    Generate a list of top ten frequent words with amount of occurrence.

    :param sentence: {string} - list of words and characters
    :return: {dict} - tuple of word and the frequency of occurrence in given sentence
    """
    freq_dist = FreqDist(clean_data(sentence=sentence))
    return freq_dist.most_common(10)
