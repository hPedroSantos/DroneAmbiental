import logging

def get_logger(name):

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
             '{"time": "%(asctime)s", "level": "%(levelname)s", "name": "%(name)s", "message": "%(message)s", datefmt="%Y-%m-%d %H:%M:%S"}'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger