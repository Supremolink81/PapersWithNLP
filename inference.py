import transformers
from gensim.models import HdpModel
from gensim.corpora.dictionary import Dictionary
from nltk.corpus import stopwords

stopword_collection: set[str] = set(stopwords.words("english"))

#text_summarization_model: transformers.Pipeline = transformers.pipeline(model="kworts/BARTxiv")

def remove_stopwords(corpus: list[list[str]]):

    """
    Removes stopwords from a given corpus of documents.

    Stop words are taken from NLTK's stopword list for the English language.

    Args:

        `list[list[str]] corpus`: the corpus to remove stop words from, each document being represented as a list of words.

    Returns:

        The corpus with all the stopwords removed.
    """

    return [[word for word in document if word not in stopword_collection] for document in corpus]