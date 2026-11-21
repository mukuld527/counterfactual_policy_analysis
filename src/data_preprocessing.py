"""
Data Preprocessing for World Bank WDI Data

Converts WDI format into a country-year panel dataset.
Author: Mukul Kumar Dhali
"""

import pandas as pd
import logging


# Replace WDI missing values with pandas NA
logger = logging.getLogger(__name__)

# Indicators of type economic to keep in the dataset
KEEP_INDICATORS = {
    "NY.GDP.MKTP.KD.ZG": "GDP_Growth",
    "SE.XPD.TOTL.GD.ZS": "Education_Spending",
    "NY.GDP.DEFL.KD.ZG": "Inflation",
    "NE.CON.GOVT.ZS": "Gov_Consumption",
    "NY.GNS.ICTR.ZS": "Gross_Savings",
    "NV.IND.TOTL.KD.ZG": "Industry_Growth",
    "TG.VAL.TOTL.GD.ZS": "Trade_GDP"
}

# Aggregate entities of type (e.g., "World", "High income") to be removed from the dataset
AGGREGATE_KEYWORDS = [
    "World",
    "High income",
    "Low income",
    "Middle income",
    "OECD",
    "European Union",
    "Euro area",
    "Sub-Saharan",
    "South Asia",
    "North America",
    "Latin America",
    "Caribbean"
]

#==========================================================================================
# Function to load the raw WDI data from a CSV file
#==========================================================================================
def load_data(filepath):

    logger.info(f"Loading data from {filepath}")
    # Read the CSV file into a DataFrame
    return pd.read_csv(filepath)

#==========================================================================================
# Function to remove aggregate entities from the dataset
#==========================================================================================
def remove_aggregates(df):

    logger.info("Removing aggregate entities")

    # Define the set of aggregate codes to be removed
    aggregate_codes = {
        "AFE","AFW","ARB","CEB","CSS",
        "EAR","EAS","ECA","ECS","EMU","EUU",
        "FCS","HIC","HPC","IBD","IBT","IDA","IDX",
        "LAC","LCN","LDC","LIC","LMC","LMY","LTE",
        "MEA","MIC","MNA","NAC","OED","OSS","PSS",
        "SAS","SSA","SSF","SST","TEA","TEC","TLA",
        "TMN","TSA","TSS","UMC","WLD"
    }

    logger.info(f"Entities Before filtering: {df['Country Code'].nunique()}")
    
    # Filter out the aggregate entities from the DataFrame
    filtered_df = df[
        ~df["Country Code"].isin(
            aggregate_codes
        )
    ].copy()

    logger.info(f"Entities After filtering: {filtered_df['Country Code'].nunique()}")

    # Return the filtered DataFrame without aggregate entities
    return filtered_df

#==========================================================================================
# Function to build a country-year panel dataset from the filtered DataFrame
#==========================================================================================
def build_panel_dataset(df):

    logger.info("Creating panel dataset")

    # Filter the DataFrame to keep only the indicators of interest
    df = df[df["Series Code"].isin(KEEP_INDICATORS.keys())].copy()

    # Identify the year columns in the DataFrame
    year_columns = [
        col for col in df.columns
        if "[YR" in col
    ]

    # Melt the DataFrame from wide to long format for easier pivoting
    long_df = pd.melt(
        df,
        id_vars=[
            "Country Name",
            "Country Code",
            "Series Code"
        ],
        value_vars=year_columns,
        var_name="Year",
        value_name="Value"
    )

    # Convert WDI missing values

    long_df["Value"] = (
        long_df["Value"]
        .replace("..", pd.NA)
    )

    # Convert to numeric BEFORE pivoting

    long_df["Value"] = pd.to_numeric(
        long_df["Value"],
        errors="coerce"
    )

    long_df["Year"] = (
        long_df["Year"]
        .str.extract(r'(\d{4})')
        .astype(int)
    )

    long_df["Indicator"] = (
        long_df["Series Code"]
        .map(KEEP_INDICATORS)
    )

    panel_df = (
        long_df
        .pivot(
            index=[
                "Country Name",
                "Country Code",
                "Year"
            ],
            columns="Indicator",
            values="Value"
        )
        .reset_index()
    )

    panel_df.columns.name = None

    return panel_df

#==========================================================================================
# Function to preprocess the data by removing aggregates and building the panel dataset
#==========================================================================================

def preprocess_data(df):
    
    logger.info("Removing aggregate entities")

    # Remove aggregate entities from the DataFrame
    df = remove_aggregates(df)

    # Build the panel dataset from the filtered DataFrame
    panel_df = build_panel_dataset(df)

    # Replace WDI missing values with pandas NA
    panel_df.replace("..", pd.NA, inplace=True)

    # Filter out years greater than 2024
    panel_df = panel_df[panel_df["Year"] <= 2024]

# Ensure numeric conversion for all numeric columns
    numeric_cols = [
            col for col in panel_df.columns
            if col not in ["Country Name", "Country Code"]
        ]

    # Convert all numeric columns to numeric type
    for col in numeric_cols:
        panel_df[col] = pd.to_numeric(panel_df[col], errors="coerce")

    # Drop rows with missing values in key columns
    panel_df = panel_df.dropna(subset=["GDP_Growth", "Education_Spending"])

    logger.info(f"Panel Dataset Shape: " f"{panel_df.shape}")

    # Log the final shape of the panel dataset
    return panel_df