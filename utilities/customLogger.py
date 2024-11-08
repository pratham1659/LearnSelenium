import logging
import os
import time

class LogGenerator:
    @staticmethod
    def save_log(message, enable_console_log=True):
        # Use an absolute path for logs, relative to the project root
        log_folder = os.path.join(os.getcwd(), "Logs")

        # Print path for debugging purposes
        print(f"Log folder path: {log_folder}")

        # Create the log folder if it doesn't exist
        if not os.path.exists(log_folder):
            print(f"Creating log folder: {log_folder}")
            os.makedirs(log_folder)

        # Define the log file path, using a fixed log file for all tests
        log_file = os.path.join(log_folder, f"test_log_{time.strftime('%Y-%m-%d')}.log")

        # Print log file path for debugging purposes
        print(f"Log file will be saved at: {log_file}")

        # Set up the logger
        logger = logging.getLogger("TestLogger")
        logger.setLevel(logging.INFO)

        # Create a file handler for logging to a file
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        # Create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        logger.addHandler(file_handler)

        # Conditionally add console output handler for logging in console
        if enable_console_log:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        # Log the provided message
        logger.info(message)

        return logger
