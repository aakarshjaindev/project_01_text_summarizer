# Text Summarizer API

A powerful and efficient text summarization service built with FastAPI and Transformers. Convert long texts into concise, meaningful summaries with state-of-the-art NLP models.

## Description

This API service leverages the power of Hugging Face's Transformers library to provide high-quality text summarization. It's designed for developers, content managers, and businesses who need to process large volumes of text efficiently.

## Features

- **Fast Processing**: Optimized for quick response times
- **Flexible Input**: Handles various text lengths and formats
- **Customizable Parameters**: Control summary length and style
- **RESTful API**: Easy integration with any application
- **Production-Ready**: Built with FastAPI for reliability and performance

## API Endpoints

### Summarize Text


## How to run locally

## How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/aakarshjaindev/project_01_text_summarizer.git
    cd project_01_text_summarizer
    ```

2.  **Create and activate the virtual environment:**
    (This project uses `uv`, but `pip` will also work with the `requirements.txt` file).
    ```bash
    uv venv --seed
    # On Windowsn
    .\.venv\Scripts\activate
    # On macOS/Linux
    # source .venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    uv pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```

5.  **Access the interactive docs** by navigating to `http://127.0.0.1:8000/docs` in your browser.