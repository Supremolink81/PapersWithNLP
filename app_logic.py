import gradio as gr
import tempfile
from inference import *

def analyze_paper(paper_file: tempfile._TemporaryFileWrapper) -> str:

    """
    Wrapper function to analyze a given research paper. 

    Args:

        `tempfile._TemporaryFileWrapper paper_file`: the file with the research paper to analyze.

    Returns:

        - a summarization of the paper (`str`)

        - a list of topics assigned to the paper (`list[str]`)

        - a question answering system to allow a user to ask questions about the paper (???)
    """

    paper_content: str = preprocess_text_file(paper_file)

    return paper_content

def preprocess_text_file(text_file: tempfile._TemporaryFileWrapper) -> str:

    """
    Takes the string content out of a text file.

    Args:

        `tempfile._TemporaryFileWrapper text_file`: the text file to take the content from.

    Returns:

        a string representing the content of the text file.
    """

    text_file.seek(0)

    return text_file.readlines()