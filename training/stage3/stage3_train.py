"""
Stage 3 model: Working professional career-switch recommendation
(Stay_Same_Role_New_Company / Switch_To_Adjacent_Role / Upskill_Same_Domain /
 Complete_Career_Change / Pursue_Entrepreneurship)
Same pipeline structure as Stage 1.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import json

RNG = np.random.default_rng(42)

FEATURES = [
    "experience_level", "current_skill_relevance", "job_satisfaction", "risk_tolerance",
    "financial_flexibility", "domain_expertise_depth", "leadership_experience",
    "networking_strength", "desire_for_stability", "entrepreneurial_drive"
]

CLASS_PROFILES = {
    "Stay_Same_Role_New_Company": [6.0, 8.0, 3.0, 5.0, 5.0, 7.0, 5.0, 6.0, 7.5, 2.5],
    "Switch_To_Adjacent_Role":    [5.5, 6.0, 4.0, 6.0, 5.5, 5.5, 5.0, 6.0, 6.0, 4.0],
    "Upskill_Same_Domain":        [4.5, 4.0, 6.0, 4.5, 4.5, 6.5, 4.0, 4.5, 7.0, 3.0],
    "Complete_Career_Change":     [5.0, 2.5, 2.5, 7.5, 6.0, 4.0, 4.5, 5.0, 3.5, 5.5],
    "Pursue_Entrepreneurship":    [6.5, 6.0, 4.0, 9.0, 7.5, 7.0, 7.5, 7.5, 2.0, 9.5],
}

N_PER_CLASS = 220
NOISE_STD = 1.3
MISSING_RATE = 0.03

def generate_dataset():
    rows = []
    for label, profile in CLASS_PROFILES.items():
        for _ in range(N_PER_CLASS):
            sample = np.array(profile) + RNG.normal(0, NOISE_STD, size=len(profile))
            sample = np.clip(sample, 0, 10)
            rows.append(list(sample) + [label])
    df = pd.DataFrame(rows, columns=FEATURES + ["recommended_path"])
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    mask = RNG.random(df[FEATURES].shape) < MISSING_RATE
    arr = df[FEATURES].to_numpy(copy=True)
    arr[mask] = np.nan
    df[FEATURES] = arr
    return df

def preprocess(df):
    imputer = SimpleImputer(strategy="mean")
    X = pd.DataFrame(imputer.fit_transform(df[FEATURES]), columns=FEATURES)
    le = LabelEncoder()
    y = le.fit_transform(df["recommended_path"])
    return X, y, le, imputer

def distance_based_match(row, class_profiles):
    scores = {}
    for label, profile in class_profiles.items():
        profile = np.array(profile)
        deficit = np.maximum(profile - row.values, 0)
        scores[label] = np.linalg.norm(deficit)
    return min(scores, key=scores.get)

def main():
    print("=" * 60)
    print("STEP 1: Generating synthetic dataset")
    print("=" * 60)
    df = generate_dataset()
    df.to_csv("stage3_dataset.csv", index=False)
    print(f"Dataset shape: {df.shape}")
    print(f"Missing values injected: {df[FEATURES].isna().sum().sum()}")
    print(f"Class distribution:\n{df['recommended_path'].value_counts()}\n")

    print("=" * 60)
    print("STEP 2: Preprocessing (imputation + label encoding)")
    print("=" * 60)
    X, y, le, imputer = preprocess(df)
    print(f"Classes: {list(le.classes_)}")
    print("Missing values after imputation:", X.isna().sum().sum(), "\n")

    print("=" * 60)
    print("STEP 3: Train/test split (80/20, stratified)")
    print("=" * 60)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"Train size: {len(X_train)} | Test size: {len(X_test)}\n")

    print("=" * 60)
    print("STEP 4: Training Gradient Boosting Classifier")
    print("=" * 60)
    model = GradientBoostingClassifier(n_estimators=150, max_depth=3, learning_rate=0.1, random_state=42)
    model.fit(X_train, y_train)
    print("Model trained.\n")

    print("=" * 60)
    print("STEP 5: Evaluation")
    print("=" * 60)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="weighted")
    print(f"Accuracy: {acc:.4f}")
    print(f"Weighted F1-score: {f1:.4f}\n")
    print("Classification report:")
    print(classification_report(y_test, y_pred, target_names=le.classes_))

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(7, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Oranges", xticklabels=le.classes_, yticklabels=le.classes_)
    plt.xlabel("Predicted"); plt.ylabel("Actual")
    plt.title("Stage 3 - Confusion Matrix (Gradient Boosting)")
    plt.xticks(rotation=30, ha="right")
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig("stage3_confusion_matrix.png", dpi=120)
    plt.close()

    importances = pd.Series(model.feature_importances_, index=FEATURES).sort_values()
    plt.figure(figsize=(7, 5))
    importances.plot(kind="barh", color="#DD8452")
    plt.title("Stage 3 - Feature Importance")
    plt.xlabel("Importance")
    plt.tight_layout()
    plt.savefig("stage3_feature_importance.png", dpi=120)
    plt.close()

    print("=" * 60)
    print("STEP 6: No-training distance-based baseline (for comparison)")
    print("=" * 60)
    X_test_reset = X_test.reset_index(drop=True)
    y_test_labels = le.inverse_transform(y_test)
    dist_preds = X_test_reset.apply(lambda row: distance_based_match(row, CLASS_PROFILES), axis=1)
    dist_acc = accuracy_score(y_test_labels, dist_preds)
    print(f"Distance-based method accuracy: {dist_acc:.4f}")
    print(f"Gradient Boosting accuracy:     {acc:.4f}\n")

    print("=" * 60)
    print("STEP 7: Saving model artifacts")
    print("=" * 60)
    joblib.dump(model, "stage3_model.pkl")
    joblib.dump(imputer, "stage3_imputer.pkl")
    joblib.dump(le, "stage3_label_encoder.pkl")
    with open("stage3_metrics.json", "w") as f:
        json.dump({
            "accuracy": acc, "f1_weighted": f1, "distance_baseline_accuracy": dist_acc,
            "n_train": len(X_train), "n_test": len(X_test), "classes": list(le.classes_),
        }, f, indent=2)
    print("Saved: stage3_model.pkl, stage3_imputer.pkl, stage3_label_encoder.pkl, stage3_metrics.json")
    print("Saved: stage3_confusion_matrix.png, stage3_feature_importance.png")

if __name__ == "__main__":
    main()
