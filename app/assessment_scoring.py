from collections import defaultdict


def calculate_feature_scores(responses, questions):
    """
    Convert individual question responses into
    the 10 ML feature scores.

    responses:
        Dictionary where:
        key   = question ID
        value = numerical score (1, 3, 5, 7, or 9)

    questions:
        List of question dictionaries from assessment_questions.py
    """

    feature_scores = defaultdict(list)

    for question in questions:
        question_id = question["id"]
        feature = question["feature"]

        if question_id not in responses:
            raise ValueError(
                f"Missing response for question {question_id}"
            )

        feature_scores[feature].append(
            responses[question_id]
        )

    final_scores = {}

    for feature, scores in feature_scores.items():

        final_scores[feature] = round(
            sum(scores) / len(scores),
            2
        )

    return dict(final_scores)