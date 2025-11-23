from fastapi import APIRouter, UploadFile
from App.Services.Inference.object_detection import detect_objects
from App.Services.Inference.depth_estimation import estimate_depth
from App.Services.Inference.aggregate_hazard_score import aggregate_hazard_scores
from App.Services.Inference.captioniong import generate_caption
from App.Services.Inference.fire_classifier import detect_fire

router = APIRouter(tags=["Upload / Analysis"])

@router.post("/upload")
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
    severity = aggregate_hazard_scores(hazards)

    return {
        "hazards": hazards,
        "severity_score": severity,
        "description": caption
    }
