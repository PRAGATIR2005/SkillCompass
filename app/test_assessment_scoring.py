from assessment_questions import get_stage1_questions
from assessment_scoring import calculate_feature_scores


questions = get_stage1_questions()


# ------------------------------------------------------------
# SAMPLE RESPONSES
# ------------------------------------------------------------

responses = {

    # math_aptitude
    1: 7,
    2: 9,
    3: 7,

    # physics_interest
    4: 9,
    5: 7,
    6: 9,

    # biology_interest
    7: 3,
    8: 3,
    9: 5,

    # chemistry_interest
    10: 9,
    11: 7,
    12: 9,

    # logical_reasoning
    13: 9,
    14: 7,
    15: 9,

    # verbal_language_skill
    16: 5,
    17: 7,
    18: 5,

    # social_science_interest
    19: 3,
    20: 3,
    21: 5,

    # creativity_arts_interest
    22: 5,
    23: 7,
    24: 5,

    # business_finance_interest
    25: 3,
    26: 3,
    27: 5,

    # hands_on_practical_preference
    28: 7,
    29: 9,
    30: 7
}


# ------------------------------------------------------------
# CALCULATE FEATURE SCORES
# ------------------------------------------------------------

feature_scores = calculate_feature_scores(
    responses,
    questions
)


# ------------------------------------------------------------
# DISPLAY RESULTS
# ------------------------------------------------------------

print("=" * 60)
print("SKILLCOMPASS - STAGE 1 SCORING TEST")
print("=" * 60)

print()

for feature, score in feature_scores.items():
    print(f"{feature}: {score:.2f}")

print()

print("=" * 60)
print("TOTAL FEATURES:", len(feature_scores))
print("=" * 60)