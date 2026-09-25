from prediction_engine import predict_stage


# ============================================================
# STAGE 1 — POST-10TH → STREAM CHOICE
# ============================================================

stage1_answers = {
    "math_aptitude": 9,
    "physics_interest": 9,
    "biology_interest": 3,
    "chemistry_interest": 8,
    "logical_reasoning": 9,
    "verbal_language_skill": 5,
    "social_science_interest": 3,
    "creativity_arts_interest": 4,
    "business_finance_interest": 3,
    "hands_on_practical_preference": 6
}


# ============================================================
# STAGE 2 — POST-12TH → HIGHER EDUCATION FIELD
# ============================================================

stage2_answers = {
    "math_score": 9,
    "science_aptitude": 9,
    "logical_reasoning": 8,
    "verbal_communication_skill": 6,
    "memorization_strength": 5,
    "creativity_design_interest": 4,
    "leadership_interest": 6,
    "business_acumen_interest": 4,
    "social_justice_interest": 3,
    "technical_hands_on_interest": 9
}


# ============================================================
# STAGE 3 — WORKING PROFESSIONAL → CAREER SWITCH
# ============================================================

stage3_answers = {
    "experience_level": 7,
    "current_skill_relevance": 8,
    "job_satisfaction": 5,
    "risk_tolerance": 7,
    "financial_flexibility": 6,
    "domain_expertise_depth": 8,
    "leadership_experience": 6,
    "networking_strength": 6,
    "desire_for_stability": 4,
    "entrepreneurial_drive": 7
}


# ============================================================
# STAGE 4 — POSTGRADUATE → NEXT CAREER STEP
# ============================================================

stage4_answers = {
    "research_aptitude": 9,
    "publication_experience": 8,
    "industry_internship_experience": 5,
    "leadership_interest": 6,
    "technical_depth": 9,
    "teaching_interest": 7,
    "risk_tolerance": 4,
    "business_acumen": 4,
    "patience_for_long_term_projects": 9,
    "networking_industry_strength": 5
}


# ============================================================
# RUN TESTS
# ============================================================

tests = [
    ("stage1", stage1_answers),
    ("stage2", stage2_answers),
    ("stage3", stage3_answers),
    ("stage4", stage4_answers)
]


print("=" * 60)
print("SKILLCOMPASS - ALL STAGES PREDICTION TEST")
print("=" * 60)


for stage, answers in tests:

    print()
    print("-" * 60)

    try:
        result = predict_stage(stage, answers)

        print("Stage:")
        print(result["stage_name"])

        print()
        print("Recommendation:")
        print(result["recommendation"])

        print()
        print("Prediction probabilities:")

        for class_name, probability in result["probabilities"].items():
            print(f"{class_name}: {probability * 100:.2f}%")

        print()
        print("STATUS: SUCCESS")

    except Exception as e:

        print()
        print("STATUS: FAILED")
        print(f"Error: {e}")


print()
print("=" * 60)
print("ALL STAGES TEST COMPLETED")
print("=" * 60)