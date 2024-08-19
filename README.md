# Intelligent Document Summarizer
![image](image.jpg)


## Overview

The Intelligent Document Summarizer is a web application built with Flask that extracts and summarizes text from uploaded documents in PDF or TXT format. The summarization process uses Natural Language Processing (NLP) techniques and machine learning algorithms to generate concise and meaningful summaries.

## Features

- Upload documents in PDF or TXT format.
- Extract text from the uploaded documents.
- Generate summaries using KMeans clustering and TF-IDF vectorization for important sentences.
- Download the generated summary as a TXT file.

## Technologies Used

- Python
- Flask
- PyMuPDF (for PDF text extraction)
- NLTK (for sentence tokenization)
- scikit-learn (for TF-IDF vectorization and KMeans clustering)
- Bootstrap (for responsive UI design)

## File Structure

```
Intelligent-Document-Summarizer/
│
├── app.py                # Main application file for Flask
├── summarizer.py         # Contains summarization logic
├── templates/
│   └── index.html       # HTML template for the web interface
├── uploads/             # Directory to store uploaded files
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Setup and Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/Intelligent-Document-Summarizer.git
    cd Intelligent-Document-Summarizer
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application**:

    ```bash
    python app.py
    ```

5. **Open your web browser and go to** `http://127.0.0.1:5000`

## Usage

1. **Home Page**: You will be presented with an upload form.
2. **Upload a File**: Click on the file input and select a PDF or TXT file to upload.
3. **Summarize**: Click the "Summarize" button to generate a summary of the document.
4. **View Summary**: The summary will be displayed below the form.
5. **Download Summary**: If you wish to keep the summary, click the "Download" button to save it as a TXT file.

## Functionality Detail

### `app.py`

- **Flask Routes**:
  - `/` : Renders the home page with upload form.
  - `/upload` : Handles file upload and summarization.
  - `/download` : Allows for downloading the generated summary.

### `summarizer.py`

- **Functions**:
  - `extract_text_from_pdf(pdf_path)` : Extracts text from PDF using PyMuPDF.
  - `extract_text(file_path)` : Determines file type and extracts text.
  - `get_summary(file_path)` : Summarizes the extracted text using TF-IDF and KMeans clustering.

## Dependencies

Ensure you have the following dependencies installed. Refer to `requirements.txt` for exact versions:

- Flask
- PyMuPDF
- NLTK
- scikit-learn
- numpy
- Bootstrap (for front-end, loaded via CDN)

## Notes

- Make sure the `uploads/` directory exists in your project root. The application will create it if it doesn't exist.
- `summarizer.py` will automatically download the necessary NLTK data files (e.g., `punkt`) during execution.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)
- [NLTK](https://www.nltk.org/)
- [scikit-learn](https://scikit-learn.org/stable/)