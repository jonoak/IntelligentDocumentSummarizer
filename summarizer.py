import fitz  # PyMuPDF
import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import os

nltk.download('punkt')


def extract_text_from_pdf(pdf_path):
    text = ''
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text


def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext == '.txt':
        with open(file_path, 'r') as file:
            return file.read()
    return ''


def get_summary(file_path):
    text = extract_text(file_path)
    sentences = sent_tokenize(text)

    if len(sentences) <= 5:
        return ' '.join(sentences)

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(sentences)
    n_clusters = 5 if len(sentences) > 5 else len(sentences)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(X)

    summary = []
    for i in range(n_clusters):
        idx = kmeans.labels_.tolist().index(i)
        summary.append(sentences[idx])

    return ' '.join(summary)