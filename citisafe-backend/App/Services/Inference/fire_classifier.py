from transformers import AutoProcessor, AutoModelForImageClassification
from PIL import Image
import io
import torch.nn.functional as F

processor = AutoProcessor.from_pretrained("google/vit-base-patch16-224")
model = AutoModelForImageClassification.from_pretrained("google/vit-base-patch16-224")

FIRE_KEYWORDS = ['fire', 'flame', 'smoke']

def detect_fire(image_bytes):
    """
    Perform fire classification on the input image bytes.

    Args:
        image_bytes (bytes): The input image in bytes.

    Returns:
        float: The probability of fire presence in the image.
    """
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    probs = F.softmax(outputs.logits, dim=1)
    top_prob, top_index = probs.max(dim=1)
    
    label = model.config.id2label[top_index.item()].lower()
    prob = float(top_prob.item())
    
    if any(keyword in label for keyword in FIRE_KEYWORDS):
        return prob
    return 0.0