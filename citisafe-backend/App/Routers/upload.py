from fastapi import APIRouter, UploadFile
from App.Services.Inference.object_detection import detect_objects
from App.Services.Inference.depth_estimation import estimate_depth
from App.Services.Inference.aggregate_hazard_score import compute_aggregate_hazard_score
from App.Services.Inference.captioning import generate_caption
from App.Services.Inference.fire_classifier import detect_fire

router = APIRouter(tags=["Hazard Analysis"])

@router.post("/analysis")
async def upload_image(file: UploadFile = file(...)):
    """
    Upload an image for hazard analysis.
    """
    # Read the uploaded file
    image_data = await file.read()

    # Perform object detection
    objects = detect_objects(image_data)

    # Perform depth estimation
    depth_map = estimate_depth(image_data)

    # Generate image caption
    caption = generate_caption(image_data)

    # Detect fire hazards
    fire_prob = detect_fire(image_data)
    
    hazards = {
        "objects": objects,
        "flood_depth_estimate": depth_map,
        "fire_probability": fire_prob,
        "description": caption
    }

    # Aggregate hazard scores
    severity = compute_aggregate_hazard_score(hazards)

    return {
        "hazards": hazards,
        "severity": severity
    }
