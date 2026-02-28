import statsmodels.formula.api as smf

def run_regression(df, output_dir):
    model_df = df[[
        "log_BLE",
        "time_to_detect_sec",
        "user_impact_score",
        "severity",
        "bug_type",
        "os"
    ]].dropna()

    for col in ["severity", "bug_type", "os"]:
        model_df[col] = model_df[col].astype("category")

    formula = """
    log_BLE ~ time_to_detect_sec + user_impact_score
              + C(severity) + C(bug_type) + C(os)
    """

    model = smf.ols(formula=formula, data=model_df).fit()

    with open(output_dir / "regression_summary.txt", "w") as f:
        f.write(model.summary().as_text())

    return model