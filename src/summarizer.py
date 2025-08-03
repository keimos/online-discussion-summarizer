from transformers import pipelines

class Summarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.summarizer = pipelines("summarization", model=model_name)

    def summarize(self, text, max_length: int = 80, min_length: int =25) -> str:
        result = self.summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False,
            truncation=True
        )
        return result[0]['summary_text']