"""
Utility functions
Author: Mukul Kumar Dhali
"""

import pandas as pd
from logger import setup_logger

logger = setup_logger()

#==========================================================================================
# Save the counterfactual simulation results to a CSV file
#==========================================================================================
def save_results(results):

    # Save the results to a CSV file without including the index column
    results.to_csv("outputs/tables/counterfactual_results.csv", index=False)

#==========================================================================================
# Print a summary of the counterfactual simulation results
#==========================================================================================
    
def print_summary(results):
    # Calculate the average policy impact
    avg_impact = results["Policy_Impact"].mean()
    
    logger.info("\nAverage Estimated Policy Impact:")
    logger.info(f"{avg_impact:.4f}% GDP Growth")


    