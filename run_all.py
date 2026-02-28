from pathlib import Path
from scripts.preprocessing import load_and_prepare_data
from scripts.descriptive import run_descriptive
from scripts.correlation import run_correlation
from scripts.group_tests import run_group_tests
from scripts.regression import run_regression
from scripts.visualization import (
    plot_distribution,
    plot_time_components,
    plot_regression_coefficients
)

def main():
    base_dir = Path(__file__).parent
    data_path = base_dir / "data/raw/frontend_uiux_bug_dataset_50000.csv"
    output_dir = base_dir / "results/tables"
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_and_prepare_data(data_path)

    run_descriptive(df, output_dir)
    run_correlation(df, output_dir)
    run_group_tests(df, output_dir)
    run_regression(df, output_dir)

    print("Replication complete. All outputs saved in results/tables/")
    figure_dir = base_dir / "results/figures"
figure_dir.mkdir(parents=True, exist_ok=True)

plot_distribution(df, figure_dir)
plot_time_components(df, figure_dir)

model = run_regression(df, output_dir)
plot_regression_coefficients(model, figure_dir)

if __name__ == "__main__":

    main()
