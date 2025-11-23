def compute_aggregate_hazard_score(hazards):
    """
    Compute the aggregate hazard score from individual hazard scores.

    Parameters:
    hazard_scores (dict): A dictionary where keys are hazard types and values are their respective scores.

    Returns:
    float: The aggregate hazard score.
    """
    score = 0

    if hazards["flood_depth_estimate"] >.15:
        score += .4
        
    score += hazards["fire_probability"] * .4
    
    obj_labels = [obj['label'] for obj in hazards['objects']]
    if 'car' in obj_labels and 'person' in obj_labels:
        score += .2
        

    return min(score, 1.0)