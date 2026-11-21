"""
Counterfactual Simulation
"""

import pandas as pd

# Function to run counterfactual simulation for a given policy variable
def run_counterfactual(
    model,
    df,
    target_column,
    policy_variable,
    change_percent=10
):

    # Define the feature columns to be used in the simulation
    feature_columns = [
        "GDP_Growth",
        "Education_Spending",
        "Inflation",
        "Gov_Consumption",
        "Gross_Savings",
        "Industry_Growth",
        "Trade_GDP",
        "Country Code",
        "Country Name",
        "Year"
    ]

    # Use the same clean dataset as training
    prediction_df = df[
        feature_columns
    ].dropna().copy()

    # Create counterfactual copy
    counterfactual_df = prediction_df.copy()

    # Apply the counterfactual change to the policy variable
    counterfactual_df[policy_variable] = (
        counterfactual_df[policy_variable]
        * (1 + change_percent / 100)
    )

    # Run predictions on both the original and counterfactual datasets
    actual_predictions = model.predict(
        prediction_df
    )

    # Store the results in a DataFrame for easier comparison
    counterfactual_predictions = model.predict(
        counterfactual_df
    )

    # Initialize the results DataFrame with the identifying columns
    results = prediction_df[
        ["Country Name", "Country Code", "Year"]
    ].copy()

    # Add the actual and counterfactual predictions to the results DataFrame
    results["Actual_GDP_Growth"] = actual_predictions

    # Add the counterfactual predictions to the results DataFrame
    results["Counterfactual_GDP_Growth"] = (
        counterfactual_predictions
    )

    # Calculate the policy impact as the difference between counterfactual and actual predictions
    results["Policy_Impact"] = (
        results["Counterfactual_GDP_Growth"]
        - results["Actual_GDP_Growth"]
    )

    return results