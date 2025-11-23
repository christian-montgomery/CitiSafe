from transformers import DetrForObjectDetection, DetrImageProcessor
from PIL import Image
import io
import torch

processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-101")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-101")

def detect_objects(image_bytes, threshold=0.7):
    """
    Perform object detection on the input image bytes.

    Args:
        image_bytes (bytes): The input image in bytes.

    Returns:
        List[Dict]: A list of detected objects with their labels and confidence scores.
    """
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    # Post-process the outputs to get the detected objects
    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(
        outputs, target_sizes=target_sizes, threshold=threshold
        )[0]

    detected_objects = []
    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        detected_objects.append({
            "label": model.config.id2label[label.item()],
            "score": score.item(),
            "box": [float(x) for x in box.tolist()]
        })

    return detected_objects