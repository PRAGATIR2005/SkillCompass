# ============================================================
# SKILLCOMPASS - STAGE 1 ASSESSMENT QUESTIONS
# Post-10th Grade → Stream Choice
# ============================================================


# ------------------------------------------------------------
# RESPONSE OPTIONS
# ------------------------------------------------------------

ABILITY_OPTIONS = [
    {
        "label": "Very Low",
        "score": 1
    },
    {
        "label": "Low",
        "score": 3
    },
    {
        "label": "Average",
        "score": 5
    },
    {
        "label": "High",
        "score": 7
    },
    {
        "label": "Very High",
        "score": 9
    }
]


INTEREST_OPTIONS = [
    {
        "label": "Strongly Dislike / Not Interested",
        "score": 1
    },
    {
        "label": "Dislike / Slightly Interested",
        "score": 3
    },
    {
        "label": "Neutral",
        "score": 5
    },
    {
        "label": "Like / Interested",
        "score": 7
    },
    {
        "label": "Strongly Like / Very Interested",
        "score": 9
    }
]


# ------------------------------------------------------------
# STAGE 1 QUESTIONS
# ------------------------------------------------------------

STAGE1_QUESTIONS = [

    # ========================================================
    # MATHEMATICAL APTITUDE
    # ========================================================

    {
        "id": 1,
        "question": (
            "How comfortable are you with solving "
            "multi-step mathematical problems?"
        ),
        "feature": "math_aptitude",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 2,
        "question": (
            "When you face a difficult mathematics problem, "
            "how willing are you to try different methods "
            "to solve it?"
        ),
        "feature": "math_aptitude",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 3,
        "question": (
            "How confident are you when working with numbers, "
            "equations, percentages, or calculations?"
        ),
        "feature": "math_aptitude",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },


    # ========================================================
    # PHYSICS INTEREST
    # ========================================================

    {
        "id": 4,
        "question": (
            "How interested are you in understanding how "
            "motion, force, energy, and electricity work?"
        ),
        "feature": "physics_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 5,
        "question": (
            "How interested are you in learning why "
            "everyday physical phenomena happen?"
        ),
        "feature": "physics_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 6,
        "question": (
            "How much do you enjoy experiments or activities "
            "involving physical concepts?"
        ),
        "feature": "physics_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },


    # ========================================================
    # BIOLOGY INTEREST
    # ========================================================

    {
        "id": 7,
        "question": (
            "How interested are you in learning about "
            "the human body and how it functions?"
        ),
        "feature": "biology_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 8,
        "question": (
            "How interested are you in studying plants, "
            "animals, microorganisms, and ecosystems?"
        ),
        "feature": "biology_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 9,
        "question": (
            "How much do you enjoy learning about living "
            "organisms and biological processes?"
        ),
        "feature": "biology_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },


    # ========================================================
    # CHEMISTRY INTEREST
    # ========================================================

    {
        "id": 10,
        "question": (
            "How interested are you in understanding chemical "
            "reactions and changes in substances?"
        ),
        "feature": "chemistry_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 11,
        "question": (
            "How interested are you in learning why different "
            "materials have different properties?"
        ),
        "feature": "chemistry_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 12,
        "question": (
            "How much do you enjoy chemistry experiments or "
            "activities involving substances and reactions?"
        ),
        "feature": "chemistry_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },


    # ========================================================
    # LOGICAL REASONING
    # ========================================================

    {
        "id": 13,
        "question": (
            "How comfortable are you solving puzzles that "
            "require identifying patterns?"
        ),
        "feature": "logical_reasoning",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 14,
        "question": (
            "When given several clues, how confident are you "
            "in using them to determine the correct answer?"
        ),
        "feature": "logical_reasoning",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 15,
        "question": (
            "How much do you enjoy problems where you have "
            "to think logically rather than memorize an answer?"
        ),
        "feature": "logical_reasoning",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },


    # ========================================================
    # VERBAL & LANGUAGE SKILL
    # ========================================================

    {
        "id": 16,
        "question": (
            "How comfortable are you expressing your ideas "
            "clearly through speaking or writing?"
        ),
        "feature": "verbal_language_skill",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 17,
        "question": (
            "How much do you enjoy reading, writing, debating, "
            "presentations, or learning languages?"
        ),
        "feature": "verbal_language_skill",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 18,
        "question": (
            "How confident are you when explaining an idea "
            "to another person using words?"
        ),
        "feature": "verbal_language_skill",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },


    # ========================================================
    # SOCIAL SCIENCE INTEREST
    # ========================================================

    {
        "id": 19,
        "question": (
            "How interested are you in learning about history, "
            "society, government, and culture?"
        ),
        "feature": "social_science_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 20,
        "question": (
            "How interested are you in understanding how "
            "people and communities behave?"
        ),
        "feature": "social_science_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 21,
        "question": (
            "How much do you enjoy discussing social issues "
            "and different viewpoints?"
        ),
        "feature": "social_science_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },


    # ========================================================
    # CREATIVITY & ARTS INTEREST
    # ========================================================

    {
        "id": 22,
        "question": (
            "How much do you enjoy drawing, designing, writing "
            "creatively, music, or other artistic activities?"
        ),
        "feature": "creativity_arts_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 23,
        "question": (
            "When given an open-ended task, how much do you "
            "enjoy creating your own original idea?"
        ),
        "feature": "creativity_arts_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 24,
        "question": (
            "How interested are you in visual design, creative "
            "expression, or creating something in your own style?"
        ),
        "feature": "creativity_arts_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },


    # ========================================================
    # BUSINESS & FINANCE INTEREST
    # ========================================================

    {
        "id": 25,
        "question": (
            "How interested are you in understanding how "
            "businesses earn money and manage resources?"
        ),
        "feature": "business_finance_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 26,
        "question": (
            "How interested are you in entrepreneurship, "
            "selling ideas, or starting a business?"
        ),
        "feature": "business_finance_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 27,
        "question": (
            "How interested are you in budgeting, saving, "
            "investment, or financial decision-making?"
        ),
        "feature": "business_finance_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },


    # ========================================================
    # HANDS-ON PRACTICAL PREFERENCE
    # ========================================================

    {
        "id": 28,
        "question": (
            "How much do you enjoy building, assembling, "
            "repairing, or working with physical objects?"
        ),
        "feature": "hands_on_practical_preference",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 29,
        "question": (
            "When learning something new, how much do you "
            "prefer practical activities or experiments?"
        ),
        "feature": "hands_on_practical_preference",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 30,
        "question": (
            "How much do you enjoy learning by actually doing "
            "something rather than only reading or listening?"
        ),
        "feature": "hands_on_practical_preference",
        "type": "interest",
        "options": INTEREST_OPTIONS
    }

]


# ------------------------------------------------------------
# HELPER FUNCTION
# ------------------------------------------------------------

def get_stage1_questions():
    """
    Return all Stage 1 assessment questions.
    """
    return STAGE1_QUESTIONS