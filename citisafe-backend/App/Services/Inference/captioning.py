from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import io

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
proccessor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

def generate_caption(image_bytes):
    """
    Generate a caption for the input image bytes.

    Args:
        image_bytes (bytes): The input image in bytes.

    Returns:
        str: The generated caption for the image.
    """
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    pixel_values = proccessor(images=image, return_tensors="pt").pixel_values

    output_ids = model.generate(pixel_values, max_length=20)
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return caption