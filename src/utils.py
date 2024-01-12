import logging

def configure_logging(log_level='INFO'):
    # Clear existing loggers and handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Configure logging if not already configured
    if not logging.getLogger().hasHandlers():
        logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s', filename='../main.log', filemode='w')
    else:
        logging.debug("Logging is already configured. Skipping.")

# Call configure_logging once at the beginning of your script
configure_logging()

if __name__ == "__main__":
    # Rest of your script...
    logging.info("This is an info message.")
    logging.error("This is an error message.")
