from model_loader import load_stage


for stage in ["stage1", "stage2", "stage3", "stage4"]:

    print("=" * 60)
    print(f"Testing {stage}")

    try:
        data = load_stage(stage)

        print("Model loaded successfully")
        print("Stage:", data["name"])
        print("Features:", len(data["features"]))
        print("Classes:", list(data["label_encoder"].classes_))

    except Exception as e:
        print("ERROR:", e)