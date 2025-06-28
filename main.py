from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

# Define the request body model using Pydantic for data validation
class TextToSummarize(BaseModel):
    text: str

# Create the FastAPI app instance
app = FastAPI()

# Load the summarization pipeline from Hugging Face.
# This model is downloaded and cached on the first run.
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Define the summarization endpoint
@app.post("/summarize/")
def summarize_text(item: TextToSummarize):
    """
    Accepts a long text and returns a concise summary.
    """
    summary = summarizer(item.text, max_length=150, min_length=40, do_sample=False)

    # The pipeline returns a list of dictionaries, we extract the summary text from the first element.

    # Return the summary
    return {"summary": summary[0]["summary_text"]}
    
# Optional: Define a root endpoint for health checks
@app.get("/")
def read_root():
    return {"status": "API is running"}


