import pandas as pd

from model_loader import load_stage


# ============================================================
# PREDICT USER OUTCOME
# ============================================================

def predict_stage(stage, answers):
    """
    Predict the recommended outcome for a user's selected stage.

    Parameters
    ----------
    stage : str
        User's locked stage, e.g. "stage1", "stage2".

    answers : dict
        Dictionary containing the user's answers.

    Returns
    -------
    dict
        Prediction result containing:
        - recommended outcome
        - probabilities
        - input values
        - stage information
    """

    # --------------------------------------------------------
    # Load stage-specific model
    # --------------------------------------------------------

    stage_data = load_stage(stage)

    model = stage_data["model"]
    imputer = stage_data["imputer"]
    label_encoder = stage_data["label_encoder"]
    features = stage_data["features"]

    # --------------------------------------------------------
    # Validate input features
    # --------------------------------------------------------

    missing_features = [
        feature for feature in features
        if feature not in answers
    ]

    if missing_features:
        raise ValueError(
            f"Missing answers for: {missing_features}"
        )

    # --------------------------------------------------------
    # Create dataframe in EXACT training feature order
    # --------------------------------------------------------

    input_data = pd.DataFrame(
        [[answers[feature] for feature in features]],
        columns=features
    )

    # --------------------------------------------------------
    # Apply same imputer used during training
    # --------------------------------------------------------

    input_imputed = imputer.transform(input_data)
    input_imputed = pd.DataFrame(
    input_imputed,
    columns=features
)

    # --------------------------------------------------------
    # Model prediction
    # --------------------------------------------------------

    prediction_encoded = model.predict(input_imputed)[0]

    # Convert encoded class back to original class name
    prediction_label = label_encoder.inverse_transform(
        [prediction_encoded]
    )[0]

    # --------------------------------------------------------
    # Prediction probabilities
    # --------------------------------------------------------

    probabilities = model.predict_proba(input_imputed)[0]

    probability_dict = {}

    for class_index, probability in zip(
        model.classes_,
        probabilities
    ):
        class_name = label_encoder.inverse_transform(
            [class_index]
        )[0]

        probability_dict[class_name] = float(probability)

    # Sort probabilities from highest to lowest
    probability_dict = dict(
        sorted(
            probability_dict.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )

    # --------------------------------------------------------
    # Return complete result
    # --------------------------------------------------------

    return {
        "stage": stage,
        "stage_name": stage_data["name"],
        "recommendation": prediction_label,
        "probabilities": probability_dict,
        "answers": answers
    }