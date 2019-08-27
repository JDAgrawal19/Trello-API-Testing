import inspect
import logging


def custom_logger(loglevel=logging.DEBUG):
    # gets the name of caller_function
    caller_log = inspect.stack()[1][3]

    logger = logging.getLogger(caller_log)

    # log all messages
    logger.setLevel(logging.ERROR)

    file_handler = logging.FileHandler("test_logger.log", mode='a')
    file_handler.setLevel(loglevel)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

