from pathlib import Path
import joblib


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"


# ============================================================
# STAGE CONFIGURATION
# ============================================================

STAGE_CONFIG = {

    "stage1": {
        "name": "Post-10th Grade - Stream Choice",

        "model": "stage1_model.pkl",
        "imputer": "stage1_imputer.pkl",
        "label_encoder": "stage1_label_encoder.pkl",

        "features": [
            "math_aptitude",
            "physics_interest",
            "biology_interest",
            "chemistry_interest",
            "logical_reasoning",
            "verbal_language_skill",
            "social_science_interest",
            "creativity_arts_interest",
            "business_finance_interest",
            "hands_on_practical_preference"
        ]
    },

    "stage2": {
        "name": "Post-12th / PUC - Higher Education Field",

        "model": "stage2_model.pkl",
        "imputer": "stage2_imputer.pkl",
        "label_encoder": "stage2_label_encoder.pkl",

        "features": [
            "math_score",
            "science_aptitude",
            "logical_reasoning",
            "verbal_communication_skill",
            "memorization_strength",
            "creativity_design_interest",
            "leadership_interest",
            "business_acumen_interest",
            "social_justice_interest",
            "technical_hands_on_interest"
        ]
    },

    "stage3": {
        "name": "Working Professional - Career Switch",

        "model": "stage3_model.pkl",
        "imputer": "stage3_imputer.pkl",
        "label_encoder": "stage3_label_encoder.pkl",

        "features": [
            "experience_level",
            "current_skill_relevance",
            "job_satisfaction",
            "risk_tolerance",
            "financial_flexibility",
            "domain_expertise_depth",
            "leadership_experience",
            "networking_strength",
            "desire_for_stability",
            "entrepreneurial_drive"
        ]
    },

    "stage4": {
        "name": "Postgraduate - Next Career Step",

        "model": "stage4_model.pkl",
        "imputer": "stage4_imputer.pkl",
        "label_encoder": "stage4_label_encoder.pkl",

        "features": [
            "research_aptitude",
            "publication_experience",
            "industry_internship_experience",
            "leadership_interest",
            "technical_depth",
            "teaching_interest",
            "risk_tolerance",
            "business_acumen",
            "patience_for_long_term_projects",
            "networking_industry_strength"
        ]
    }
}


# ============================================================
# MODEL LOADER
# ============================================================

def load_stage(stage):

    if stage not in STAGE_CONFIG:
        raise ValueError(f"Invalid stage: {stage}")

    config = STAGE_CONFIG[stage]

    stage_model_dir = MODEL_DIR / stage

    model_path = stage_model_dir / config["model"]
    imputer_path = stage_model_dir / config["imputer"]
    encoder_path = stage_model_dir / config["label_encoder"]

    # Check that files exist
    if not model_path.exists():
        raise FileNotFoundError(f"Model not found: {model_path}")

    if not imputer_path.exists():
        raise FileNotFoundError(f"Imputer not found: {imputer_path}")

    if not encoder_path.exists():
        raise FileNotFoundError(f"Label encoder not found: {encoder_path}")

    # Load artifacts
    model = joblib.load(model_path)
    imputer = joblib.load(imputer_path)
    label_encoder = joblib.load(encoder_path)

    return {
        "model": model,
        "imputer": imputer,
        "label_encoder": label_encoder,
        "features": config["features"],
        "name": config["name"]
    }