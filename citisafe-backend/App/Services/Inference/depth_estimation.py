from transformers import DPTForDepthEstimation, DPTImageProcessor
from PIL import Image
import io
import numpy as np

processor = DPTImageProcessor.from_pretrained("Intel/dpt-large")
model = DPTForDepthEstimation.from_pretrained("Intel/dpt-large")

def estimate_depth(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    
    inputs = processor(images=img, return_tensors="pt")
    outputs = model(**inputs)
    
    depth = outputs.predicted_depth.squeeze().detach.numpy()
    
    depth_norm = (depth - depth.min()) / (depth.max() - depth.min())
    
    flood_estimate = float(np.mean(depth_norm))
    
    return flood_estimate