from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image
import io

proccessor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

def answer_question(image_bytes, question):
    """
    Answer a question based on the input image bytes.

    Args:
        image_bytes (bytes): The input image in bytes.
        question (str): The question to be answered about the image.

    Returns:
        str: The answer to the question.
    """
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    inputs = proccessor(image, question, return_tensors="pt")
    outputs = model(**inputs)
    
    index = outputs.logits.argmax(-1).item()
    answer = model.config.id2label[index]
    
    return answer