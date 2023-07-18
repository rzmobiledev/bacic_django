import logging


class Log:

    format = "%(asctime)s %(levelname)s %(message)s"
    logger = logging.getLogger(__name__)

    # handler
    stream_h = logging.StreamHandler()
    file_h = logging.FileHandler('logger.log')

    stream_h.setLevel(logging.WARNING)
    file_h.setLevel(logging.ERROR)

    # formater
    formater = logging.Formatter(format)
    stream_h.setFormatter(formater)
    file_h.setFormatter(formater)

    logger.addHandler(stream_h)
    logger.addHandler(file_h)
