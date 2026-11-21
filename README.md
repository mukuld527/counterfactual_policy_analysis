# Counterfactual Analysis of Education Spending Policy

## Project Overview

This project evaluates the potential impact of a hypothetical policy change on economic outcomes using counterfactual analysis.

### Policy Scenario

Increase national education spending by 10%.

### Research Question

How would a 10% increase in public education spending influence GDP growth?

---

## Methodology

A regression-based counterfactual framework is used.

### Steps:

1. Data collection
2. Data preprocessing
3. Feature scaling
4. Model training
5. Counterfactual simulation
6. Economic impact analysis
7. Visualization

---

## Dataset Variables

| Variable | Description |
|-----------|------------|
| GDP_Growth | Annual GDP growth rate (%) |
| Education_Spending | Education expenditure (% GDP) |
| Inflation | Inflation rate (%) |
| Unemployment | Unemployment rate (%) |
| Government_Expenditure | Government expenditure (% GDP) |

---

## Counterfactual Design

### Baseline Scenario

Observed education spending.

### Treatment Scenario

Education spending increased by 10%.

Example:

Current Education Spending = 5%

Counterfactual Spending =

5 × 1.10 = 5.5%

The fitted model predicts GDP growth under both scenarios.

The difference represents the estimated policy impact.

---

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Step 1: Generate Dataset

```bash
python data/generate_dataset.py
```

### Step 2: Run Analysis

```bash
python main.py
```

---

## Outputs

### Figures

- policy_impact_distribution.png
- actual_vs_counterfactual.png

### Tables

- counterfactual_results.csv

---

## Evaluation Metrics

The model is evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R-Squared

---

## Expected Findings

The counterfactual simulation generally indicates that increased education spending:

- Improves GDP growth
- Enhances long-term productivity
- Supports human capital development

Results may vary depending on model assumptions.

---

## Assumptions

1. Linear relationship between predictors and GDP growth.
2. No major structural economic shocks.
3. Policy implementation is immediate.
4. Other macroeconomic variables remain unchanged.

---

## Limitations

- Simulated policy intervention
- Synthetic dataset
- Correlation is not necessarily causation
- External economic shocks not modeled

---

## Author

Mukul Kumar Dhali
PhDAI 730: Statistics for AI

Project name: Project 2 - Evaluating the Impact of Policy Changes on Economic Outcomes



```
Project folder structure

📦 counterfactual_policy_analysis
├── 📁 data
│   └──  policy_analysis_data.csv
├── 📁 outputs
│   ├── 📁 figures
│   │   ├── actual_vs_counterfactual.png
│   │   ├── policy_impact_distribution.png
│   │   └── correlation_heatmap.png
│   └── 📁 tables
│       ├── clean_panel_data.csv
│       ├── final_model_dataset.csv
│       ├── counterfactual_results.csv
│       ├── summary_statistics.csv
│       ├── missing_data_report.csv
│       ├── country_policy_impacts.csv
│       └── regression_summary.txt
├── 📁 src
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── counterfactual_simulation.py
│   ├── visualization.py
│   ├── logger.py
│   ├── main.py
│   └── utils.py
├── project.log
├── requirements.txt
└── README.md


```
