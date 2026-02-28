from scipy.stats import kruskal
import pandas as pd

def epsilon_squared(H, n, k):
    return (H - k + 1) / (n - k)

def run_group_tests(df, output_dir):
    categorical_vars = ["severity", "bug_type", "os", "browser"]
    results = []

    for cat in categorical_vars:
        if cat in df.columns:
            groups = [group["BLE"] for _, group in df.groupby(cat) if len(group) > 10]
            k = len(groups)

            if k >= 2:
                H, p = kruskal(*groups)
                n = len(df)
                eps = epsilon_squared(H, n, k)

                results.append({
                    "variable": cat,
                    "H_statistic": H,
                    "p_value": p,
                    "epsilon_squared": eps
                })

    results_df = pd.DataFrame(results)
    results_df.to_csv(output_dir / "kruskal_results.csv", index=False)
    return results_df