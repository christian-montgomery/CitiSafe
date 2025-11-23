def compute_aggregate_hazard_score(hazards):
    """
    Compute the aggregate hazard score from individual hazard scores.

    Parameters:
    hazard_scores (dict): A dictionary where keys are hazard types and values are their respective scores.

    Returns:
    float: The aggregate hazard score.
    """
    score = 0.0

    # Flood weighting 0.4 max
    flood_depth = hazards.get("flood_depth_estimate", 0)
    if flood_depth >= 0.15: score += 0.2
    if flood_depth >= 0.25: score += 0.2
        
    # Fire weighting 0.4 max
    fire_prob = hazards.get("fire_probability", 0)
    score += min(fire_prob * 0.4, 0.4)
    
    # Accident detection weighting 0.2 max
    labels = [obj['label'].lower() for obj in hazards.get("objects", [])]
    if "car" in labels and "person" in labels:
        score += 0.2

    return min(score, 1.0)