def run_descriptive(df, output_dir):
    desc = df[[
        "time_to_detect_sec",
        "time_to_fix_sec",
        "BLE",
        "user_impact_score"
    ]].describe()

    median = df[[
        "time_to_detect_sec",
        "time_to_fix_sec",
        "BLE",
        "user_impact_score"
    ]].median()

    skewness = df[[
        "time_to_detect_sec",
        "time_to_fix_sec",
        "BLE"
    ]].skew()

    desc.to_csv(output_dir / "descriptive_statistics.csv")
    median.to_csv(output_dir / "median_statistics.csv")
    skewness.to_csv(output_dir / "skewness_analysis.csv")

    return desc, median, skewness