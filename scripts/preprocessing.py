import pandas as pd
import numpy as np
from pathlib import Path

def load_and_prepare_data(data_path):
    df = pd.read_csv(data_path)

    # Filter resolved bugs
    df = df[df["resolved"] == "Yes"].copy()

    # Convert numeric safely
    numeric_cols = [
        "time_to_detect_sec",
        "time_to_fix_sec",
        "user_impact_score"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=numeric_cols)

    # Feature Engineering
    df["BLE"] = df["time_to_detect_sec"] + df["time_to_fix_sec"]
    df["log_BLE"] = np.log1p(df["BLE"])

    return df