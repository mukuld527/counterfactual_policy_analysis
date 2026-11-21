"""
Centralized Logging Configuration

Author: Mukul Kumar Dhali
"""

import logging
from pathlib import Path

#==========================================================================================
# Function to set up the centralized logger
#========================================================================================== 
def setup_logger():
    # Define the log file path
    log_file = Path("project.log")

    # Ensure the log file's parent directory exists
    logger = logging.getLogger("PolicyAnalysis")

    # Set the logging level for the logger
    logger.setLevel(logging.INFO)

    # Add handlers to the logger if they don't already exist
    if not logger.handlers:
        # Define the log file path
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

        # File Handler
        file_handler = logging.FileHandler(log_file,mode="a")

        file_handler.setFormatter(formatter)

        # Console Handler
        console_handler = logging.StreamHandler()

        # Ensure the log file's parent directory exists
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        logger.addHandler(file_handler)

        # Add the console handler to the logger
        logger.addHandler(console_handler)

    return logger