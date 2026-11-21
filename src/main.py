"""
Counterfactual Analysis Project

Policy:
10% Increase in Education Spending

Outcome:
GDP Growth

#Author: Mukul Kumar Dhali
"""

import os


from data_preprocessing import (
    load_data,
    preprocess_data
)

from model_training import (
    train_model,
    evaluate_model
)

from counterfactual_simulation import (
    run_counterfactual
)

from visualization import (
    create_visualizations,
    correlation_heatmap
)

from utils import (
    save_results,
    print_summary
)


from logger import setup_logger

logger = setup_logger()

#==========================================================================================
# Main Function for the Counterfactual Analysis Project
#==========================================================================================

def main():
    logger.info("Application Started")
    os.makedirs(
        "outputs/figures",
        exist_ok=True
    )

    os.makedirs(
        "outputs/tables",
        exist_ok=True
    )

    logger.info("Loading Data...")

    # 
    df = load_data("data/policy_analysis_data.csv")

    logger.info("Preprocessing Data...")

    # Preprocess the loaded data to create a panel dataset
    panel_df = preprocess_data(df)

    logger.info(sorted(panel_df["Country Code"].unique())[:50])

    logger.info(f"Countries remaining: "f"{panel_df['Country Code'].nunique()}")

    logger.info(sorted(panel_df["Country Code"].unique())[:20])

    # Replace the original dataframe with the preprocessed panel dataframe
    df = panel_df
    
    # Generate a report of missing data in the dataset
    missing_report = (
        df.isnull()
        .sum()
        .to_frame(name="Missing_Count")
    )

    # Calculate the percentage of missing data for each column
    missing_report["Missing_Percent"] = (missing_report["Missing_Count"]/ len(df)* 100)

    # Save the missing data report to a CSV file
    missing_report.to_csv("outputs/tables/missing_data_report.csv")

    logger.info("Missing data report saved.")

    logger.info("\nMissing Value Summary")
    logger.info(f"\n{missing_report}")

    # Save the cleaned panel dataset and final model dataset
    df.to_csv("outputs/tables/clean_panel_data.csv", index=False)

    # Save the final model dataset
    df.to_csv("outputs/tables/final_model_dataset.csv", index=False)

    # Save the regression summary to a text file
    with open(
                "outputs/tables/regression_summary.txt", "w", encoding="utf-8"
            ) as f:
                f.write(model.summary().as_text())

    # Define the target column and policy variable for the counterfactual analysis
    target_column = "GDP_Growth"

    # Define the policy variable for the counterfactual analysis
    policy_variable = "Education_Spending"

    logger.info("Training Model...")

    # Train the model using the preprocessed panel dataset
    model, model_df = train_model(df,target_column)

    # Evaluate the trained model
    metrics = evaluate_model(model)

    logger.info(f"R² = {metrics['R2']:.4f}")
    
    logger.info("\nModel Performance")

    # Log the model performance metrics
    for metric, value in metrics.items():
        logger.info(f"{metric}: {value:.4f}")

    logger.info("\nRunning Counterfactual Simulation...")

    # Run the counterfactual simulation using the trained model
    results = run_counterfactual(
                    model,
                    model_df,
                    target_column,
                    policy_variable,
                    change_percent=10
                )

    # Save the counterfactual simulation results
    save_results(results)

    # Calculate the average policy impact for each country
    country_impacts = (results.
                       groupby("Country Name")["Policy_Impact"].
                       mean().
                       sort_values(ascending=False)
                    )

    # Save the country policy impacts to a CSV file
    country_impacts.to_csv("outputs/tables/country_policy_impacts.csv")

    # Create visualizations for the counterfactual simulation results
    create_visualizations(results)

    # Print a summary of the counterfactual simulation results
    print_summary(results)

    # Generate a correlation heatmap for the dataset
    correlation_heatmap(df)
    
    logger.info("\nProject Completed Successfully.")

    # Generate summary statistics for the dataset
    summary_stats = (df.select_dtypes(include=["number"]).describe())

    # Save the summary statistics to a CSV file
    summary_stats.to_csv("outputs/tables/summary_statistics.csv")

    logger.info("\nSummary Statistics")
    logger.info(summary_stats)


# Main execution block for the script
if __name__ == "__main__":
    main()



