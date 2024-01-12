import logging


def configure_logging(log_level):
    logging.basicConfig(filename='../main.log', level=log_level)
