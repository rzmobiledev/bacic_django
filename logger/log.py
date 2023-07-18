import logging

"""
Logging info level:
1. debug
2. info
3. warning
4. error
5. critical
"""


class Log:

    format = "%(asctime)s - %(levelname)s - %(message)s"
    logger = logging.getLogger(__name__)

    # create handler
    stream_h = logging.StreamHandler()
    file_h = logging.FileHandler('log.log')

    # level and format
    stream_h.setLevel(logging.WARNING)
    file_h.setLevel(logging.ERROR)

    formatter = logging.Formatter(format)
    stream_h.setFormatter(formatter)
    file_h.setFormatter(formatter)

    logger.addHandler(stream_h)
    logger.addHandler(file_h)

    @classmethod
    def warning(cls, message):
        cls.logger.warning(message)

    @classmethod
    def error(cls, message):
        cls.logger.error(message)

    @classmethod
    def info(cls, message):
        cls.logger.info(message)
