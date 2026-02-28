# Replication Package

This repository contains the full replication package for the study:

"Bug Metadata as Low-Fidelity Proxies for Maintenance Effort"

## Dataset

Download the dataset from Kaggle:

Frontend UI/UX Bug Dataset (50,000 records)

Place the file:
frontend_uiux_bug_dataset_50000.csv

inside:
data/raw/

## Environment Setup

Install dependencies:

pip install -r requirements.txt

## Reproducing the Study

Run:

python run_all.py

All tables will be generated in:

results/tables/

## Outputs

- descriptive_statistics.csv
- median_statistics.csv
- skewness_analysis.csv
- correlation_results.csv
- kruskal_results.csv
- regression_summary.txt

All analyses are deterministic and require no random seed.