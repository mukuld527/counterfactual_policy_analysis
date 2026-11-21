"""
Visualization Module
Author: Mukul Kumar Dhali
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns

from logger import setup_logger
logger = setup_logger()

#==========================================================================================
# Create a correlation heatmap of economic indicators
#==========================================================================================
def correlation_heatmap(df):

   # Keep only numeric columns
    numeric_df = df.select_dtypes(include=["number"])

    # Create a correlation matrix of the numeric columns
    plt.figure(figsize=(12, 8))

    # Plot the correlation heatmap
    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    # Add a title to the heatmap
    plt.title("Economic Indicators Correlation Matrix")
    logger.info("Correlation heatmap saved to outputs/figures/correlation_heatmap.png")
    plt.tight_layout()

    # Save the heatmap to a file
    plt.savefig("outputs/figures/correlation_heatmap.png")
    logger.info("Correlation heatmap saved to outputs/figures/correlation_heatmap.png")

    logger.info("Correlation heatmap creation completed.")

    # Close the current figure to free up memory
    plt.close()

#==========================================================================================
# Create visualizations of counterfactual policy effects
#==========================================================================================
def create_visualizations(results):

    # Ensure the output directory exists before saving figures
    os.makedirs("outputs/figures", exist_ok=True)

    # Create a histogram of the policy impact distribution
    plt.figure(figsize=(10, 6))
    
    # Plot the histogram of policy impact distribution
    sns.histplot(results["Policy_Impact"], kde=True, color="green")

    # Add a title to the histogram
    plt.title("Distribution of Counterfactual Policy Effects")

    # Add labels to the x and y axes
    plt.xlabel("GDP Growth Change (%)")

    # Add a label to the y-axis
    plt.ylabel("Frequency")

    # Save the histogram to a file
    plt.savefig("outputs/figures/policy_impact_distribution.png")

    logger.info("Policy impact distribution histogram saved to outputs/figures/policy_impact_distribution.png")

    logger.info("Policy impact distribution histogram creation completed.")
    # Close the current figure to free up memory
    plt.close()
    # Create a line plot of actual vs counterfactual GDP growth
    plt.figure(figsize=(12, 6))

    # Plot the actual vs counterfactual GDP growth line chart
    plt.plot(
        results["Actual_GDP_Growth"],
        label="Actual"
    )

    # Plot the counterfactual GDP growth line chart
    plt.plot(
        results["Counterfactual_GDP_Growth"],
        label="Counterfactual"
    )

    # Add a title to the line chart
    plt.title("Actual vs Counterfactual GDP Growth")

    # Add a legend to the line chart
    plt.legend()

    # Save the line chart to a file
    plt.savefig("outputs/figures/actual_vs_counterfactual.png")

    logger.info("Actual vs counterfactual GDP growth line chart saved to outputs/figures/actual_vs_counterfactual.png")

    logger.info("Actual vs counterfactual GDP growth line chart creation completed.")

    # Close the current figure to free up memory
    plt.close()

