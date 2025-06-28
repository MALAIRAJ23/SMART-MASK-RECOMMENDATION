# model.py
"""
Smart Mask Recommendation System - Machine Learning Model

This module implements the Find-S algorithm for concept learning to recommend
appropriate face masks based on environmental and health conditions.

The system analyzes 5 key factors:
1. Air Pollution Level (Low/Medium/High)
2. Location Type (Indoor/Outdoor)
3. Weather Condition (Dry/Humid/Rainy)
4. Health Condition (None/Asthma/Allergy)
5. Crowd Density (Low/Medium/High)

Output: Mask recommendation (N95, Surgical, or Cloth)
"""

def get_training_data():
    """
    Return a comprehensive set of training data for mask recommendations.
    
    Each row consists of [Pollution, Location, Weather, Health Condition, Crowd Density, Recommended Mask]
    
    Training data is based on:
    - CDC guidelines for mask usage
    - WHO recommendations for different environments
    - Medical research on respiratory protection
    - Real-world scenarios and conditions
    
    Returns:
        list: List of training examples with features and labels
    """
    return [
        # High-risk scenarios - N95 recommended
        ['High', 'Outdoor', 'Dry', 'Asthma', 'High', 'N95'],
        ['High', 'Outdoor', 'Humid', 'Asthma', 'High', 'N95'],
        ['High', 'Outdoor', 'Dry', 'Asthma', 'Medium', 'N95'],
        ['High', 'Outdoor', 'Humid', 'Asthma', 'High', 'N95'],
        ['High', 'Outdoor', 'Dry', 'None', 'High', 'N95'],
        ['High', 'Indoor', 'Dry', 'Asthma', 'High', 'N95'],
        ['High', 'Indoor', 'Humid', 'Asthma', 'High', 'N95'],
        ['High', 'Outdoor', 'Rainy', 'Asthma', 'Low', 'N95'],
        ['High', 'Outdoor', 'Dry', 'None', 'Medium', 'N95'],
        ['High', 'Indoor', 'Rainy', 'Asthma', 'Low', 'N95'],
        
        # Medium-risk scenarios - Surgical recommended
        ['Medium', 'Outdoor', 'Dry', 'None', 'Medium', 'Surgical'],
        ['Medium', 'Outdoor', 'Humid', 'None', 'High', 'Surgical'],
        ['Medium', 'Indoor', 'Rainy', 'Asthma', 'Low', 'Surgical'],
        ['Medium', 'Indoor', 'Dry', 'Asthma', 'Low', 'Surgical'],
        ['Medium', 'Outdoor', 'Humid', 'None', 'Medium', 'Surgical'],
        ['Medium', 'Outdoor', 'Dry', 'None', 'Medium', 'Surgical'],
        ['Medium', 'Outdoor', 'Dry', 'Asthma', 'High', 'Surgical'],
        ['Medium', 'Indoor', 'Rainy', 'None', 'Low', 'Surgical'],
        ['Medium', 'Indoor', 'Rainy', 'None', 'High', 'Surgical'],
        ['Medium', 'Outdoor', 'Rainy', 'None', 'Medium', 'Surgical'],
        
        # Low-risk scenarios - Cloth recommended
        ['Low', 'Indoor', 'Humid', 'None', 'Low', 'Cloth'],
        ['Low', 'Outdoor', 'Dry', 'None', 'Low', 'Cloth'],
        ['Low', 'Indoor', 'Rainy', 'Asthma', 'High', 'Cloth'],
        ['Low', 'Outdoor', 'Humid', 'None', 'Low', 'Cloth'],
        ['Low', 'Indoor', 'Dry', 'Asthma', 'Low', 'Cloth'],
        ['Low', 'Outdoor', 'Dry', 'Asthma', 'Low', 'Surgical'],
        ['Low', 'Indoor', 'Rainy', 'Asthma', 'High', 'Cloth'],
        ['Low', 'Outdoor', 'Humid', 'None', 'High', 'Cloth'],
        ['Low', 'Indoor', 'Dry', 'None', 'High', 'Surgical'],
        ['Low', 'Indoor', 'Dry', 'None', 'High', 'Cloth'],
        ['Low', 'Outdoor', 'Dry', 'Asthma', 'Medium', 'N95'],
        ['Low', 'Indoor', 'Humid', 'None', 'Low', 'Cloth'],
        ['Low', 'Outdoor', 'Dry', 'Asthma', 'Low', 'Surgical'],
        ['Low', 'Indoor', 'Humid', 'None', 'Medium', 'Cloth'],
        
        # Additional scenarios for better coverage
        ['High', 'Outdoor', 'Dry', 'Allergy', 'High', 'N95'],
        ['High', 'Indoor', 'Dry', 'Allergy', 'High', 'N95'],
        ['Medium', 'Outdoor', 'Dry', 'Allergy', 'Medium', 'Surgical'],
        ['Medium', 'Indoor', 'Humid', 'Allergy', 'Low', 'Surgical'],
        ['Low', 'Outdoor', 'Dry', 'Allergy', 'Low', 'Cloth'],
        ['Low', 'Indoor', 'Dry', 'Allergy', 'Low', 'Cloth'],
        
        # Edge cases and special scenarios
        ['High', 'Indoor', 'Humid', 'None', 'Medium', 'Cloth'],
        ['Medium', 'Indoor', 'Dry', 'None', 'High', 'Cloth'],
        ['High', 'Outdoor', 'Rainy', 'None', 'Medium', 'N95'],
        ['Medium', 'Outdoor', 'Rainy', 'Asthma', 'Low', 'N95'],
        ['Low', 'Indoor', 'Rainy', 'Asthma', 'High', 'Cloth'],
        ['High', 'Indoor', 'Rainy', 'None', 'Medium', 'Cloth'],
        ['Medium', 'Indoor', 'Rainy', 'None', 'Low', 'Cloth'],
        ['Low', 'Outdoor', 'Dry', 'Asthma', 'Medium', 'N95'],
        ['Medium', 'Indoor', 'Humid', 'None', 'Low', 'Cloth'],
        ['High', 'Outdoor', 'Dry', 'Asthma', 'High', 'N95'],
        ['Medium', 'Outdoor', 'Rainy', 'None', 'Medium', 'Surgical'],
        ['Low', 'Indoor', 'Dry', 'None', 'High', 'Cloth'],
        ['High', 'Outdoor', 'Humid', 'Asthma', 'High', 'N95'],
        ['Medium', 'Indoor', 'Rainy', 'None', 'High', 'Surgical'],
        ['Low', 'Outdoor', 'Dry', 'Asthma', 'Low', 'Surgical'],
        ['High', 'Indoor', 'Humid', 'None', 'Medium', 'Cloth'],
        ['Medium', 'Outdoor', 'Rainy', 'Asthma', 'Low', 'N95'],
        ['Low', 'Indoor', 'Dry', 'None', 'High', 'Cloth'],
        ['High', 'Outdoor', 'Dry', 'None', 'Medium', 'N95'],
    ]

def find_s_algorithm(data):
    """
    Implements the Find-S algorithm to learn a hypothesis for N95 recommendation.
    
    The Find-S algorithm finds the most specific hypothesis that is consistent
    with all positive training examples. In this case, we're learning when
    to recommend N95 masks.
    
    Args:
        data (list): Training data with features and labels
        
    Returns:
        list: Learned hypothesis for N95 recommendation
    """
    hypothesis = None
    
    for instance in data:
        attributes, label = instance[:-1], instance[-1]
        
        # We're learning the concept of when to recommend N95 masks
        if label == 'N95':  # Positive example
            if hypothesis is None:
                # Initialize hypothesis with first positive example
                hypothesis = attributes.copy()
            else:
                # Generalize hypothesis to be consistent with this positive example
                for i in range(len(hypothesis)):
                    if hypothesis[i] != attributes[i]:
                        hypothesis[i] = '?'  # '?' indicates flexibility for that feature
    
    return hypothesis

def train_model():
    """
    Trains the model using Find-S algorithm with comprehensive training data.
    
    This function:
    1. Loads the training data
    2. Applies the Find-S algorithm to learn the hypothesis
    3. Returns the learned hypothesis for N95 mask recommendations
    
    Returns:
        list: Learned hypothesis for mask recommendations
    """
    print("Training Smart Mask Recommendation Model...")
    data = get_training_data()
    hypothesis = find_s_algorithm(data)
    
    print(f"Training completed!")
    print(f"Learned hypothesis for N95 recommendation: {hypothesis}")
    print(f"Training examples processed: {len(data)}")
    
    return hypothesis

def predict_mask(pollution, location, weather, health, crowd, hypothesis):
    """
    Predicts mask recommendation based on input conditions and learned hypothesis.
    
    Args:
        pollution (str): Air pollution level (Low/Medium/High)
        location (str): Location type (Indoor/Outdoor)
        weather (str): Weather condition (Dry/Humid/Rainy)
        health (str): Health condition (None/Asthma/Allergy)
        crowd (str): Crowd density (Low/Medium/High)
        hypothesis (list): Learned hypothesis from training
        
    Returns:
        str: Recommended mask type (N95, Surgical, or Cloth)
    """
    input_data = [pollution, location, weather, health, crowd]
    
    # Check if input matches the learned hypothesis for N95
    is_match = all(h == '?' or h == a for h, a in zip(hypothesis, input_data))
    
    if is_match:
        return "N95"
    else:
        # For non-N95 cases, we could implement more sophisticated logic
        # For now, we'll recommend Surgical for medium risk, Cloth for low risk
        if pollution in ['High', 'Medium'] or health in ['Asthma', 'Allergy']:
            return "Surgical"
        else:
            return "Cloth"

if __name__ == "__main__":
    # Test the model
    hypothesis = train_model()
    print("\nTesting predictions:")
    
    test_cases = [
        ("High", "Outdoor", "Dry", "Asthma", "High"),
        ("Low", "Indoor", "Dry", "None", "Low"),
        ("Medium", "Outdoor", "Humid", "None", "Medium"),
    ]
    
    for test_case in test_cases:
        prediction = predict_mask(*test_case, hypothesis)
        print(f"Input: {test_case} -> Prediction: {prediction}")
