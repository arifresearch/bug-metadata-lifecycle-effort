import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_distribution(df, output_dir):
    plt.figure()
    sns.histplot(df["BLE"], bins=30, kde=True)
    plt.title("Distribution of Bug Lifecycle Effort (BLE)")
    plt.xlabel("BLE (seconds)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(output_dir / "ble_distribution.png")
    plt.close()

def plot_time_components(df, output_dir):
    means = [
        df["time_to_detect_sec"].mean(),
        df["time_to_fix_sec"].mean(),
        df["BLE"].mean()
    ]

    labels = ["Detection Time", "Fix Time", "BLE"]

    plt.figure()
    plt.bar(labels, means)
    plt.title("Mean Time Components of Lifecycle Effort")
    plt.ylabel("Seconds")
    plt.tight_layout()
    plt.savefig(output_dir / "mean_time_components.png")
    plt.close()

def plot_regression_coefficients(model, output_dir):
    coef = model.params.drop("Intercept")
    coef = coef.sort_values()

    plt.figure(figsize=(8,6))
    coef.plot(kind="barh")
    plt.title("Regression Coefficients (log BLE Model)")
    plt.tight_layout()
    plt.savefig(output_dir / "regression_coefficients.png")
    plt.close()