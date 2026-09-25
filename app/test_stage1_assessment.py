from assessment_questions import get_stage1_questions
from assessment_scoring import calculate_feature_scores
from prediction_engine import predict_stage


# ============================================================
# LOAD QUESTIONS
# ============================================================

questions = get_stage1_questions()


# ============================================================
# SAMPLE STUDENT RESPONSES
# ============================================================

responses = {
    1: 7,
    2: 9,
    3: 7,

    4: 9,
    5: 7,
    6: 9,

    7: 3,
    8: 3,
    9: 5,

    10: 9,
    11: 7,
    12: 9,

    13: 9,
    14: 7,
    15: 9,

    16: 5,
    17: 7,
    18: 5,

    19: 3,
    20: 3,
    21: 5,

    22: 5,
    23: 7,
    24: 5,

    25: 3,
    26: 3,
    27: 5,

    28: 7,
    29: 9,
    30: 7
}


# ============================================================
# CALCULATE FEATURES
# ============================================================

feature_scores = calculate_feature_scores(
    responses,
    questions
)


# ============================================================
# RUN ML PREDICTION
# ============================================================

result = predict_stage(
    "stage1",
    feature_scores
)


# ============================================================
# DISPLAY RESULT
# ============================================================

print("=" * 60)
print("SKILLCOMPASS - COMPLETE STAGE 1 ASSESSMENT TEST")
print("=" * 60)

print("\nCalculated Feature Scores:")

for feature, score in feature_scores.items():
    print(f"{feature}: {score:.2f}")


print("\n" + "-" * 60)

print("\nAI Recommendation:")
print(result["recommendation"])


print("\nPrediction Probabilities:")

for class_name, probability in result["probabilities"].items():
    print(
        f"{class_name}: "
        f"{probability * 100:.2f}%"
    )


print("\n" + "=" * 60)
print("STAGE 1 ASSESSMENT TEST COMPLETED")
print("=" * 60)