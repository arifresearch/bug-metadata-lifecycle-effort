from scipy.stats import spearmanr
import pandas as pd

def run_correlation(df, output_dir):
    corr1, p1 = spearmanr(df["time_to_detect_sec"], df["time_to_fix_sec"])
    corr2, p2 = spearmanr(df["user_impact_score"], df["BLE"])

    results = pd.DataFrame({
        "comparison": [
            "detect_vs_fix",
            "impact_vs_BLE"
        ],
        "rho": [corr1, corr2],
        "p_value": [p1, p2]
    })

    results.to_csv(output_dir / "correlation_results.csv", index=False)
    return results