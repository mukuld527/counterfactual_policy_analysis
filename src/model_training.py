"""
Module for training and evaluating a fixed effects regression model.
Author: Mukul Kumar Dhali
"""

import statsmodels.formula.api as smf
from logger import setup_logger

logger = setup_logger()

#==========================================================================================
# Train the fixed effects regression model
#==========================================================================================
def train_model(df, target_column):
    # Create a copy of the input dataframe to avoid modifying the original data
    model_df = df.copy()

    # Drop rows with missing values for the relevant columns
    model_df = model_df.dropna(
        subset=[
            "GDP_Growth",
            "Education_Spending",
            "Inflation",
            "Gov_Consumption",
            "Gross_Savings",
            "Industry_Growth",
            "Trade_GDP",
            "Country Code",
            "Year"
        ]
    )

    # Define the formula for the fixed effects regression model
    formula = """
    GDP_Growth ~
    Education_Spending +
    Inflation +
    Gov_Consumption +
    Gross_Savings +
    Industry_Growth +
    Trade_GDP +
    C(Year) +
    C(Q('Country Code'))
    """

    model = smf.ols(
        formula=formula,
        data=model_df
    ).fit()

    return model, model_df


#==========================================================================================
# Evaluate the trained model
#==========================================================================================
def evaluate_model(model):

    logger.info("\nModel Summary")
    logger.info("=" * 80)

    logger.info(model.summary())

    # Return the model performance metrics
    return {
        "R2": model.rsquared,
        "Adj_R2": model.rsquared_adj,
        "AIC": model.aic,
        "BIC": model.bic
    }