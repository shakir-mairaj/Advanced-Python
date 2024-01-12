#logging in modules and hierarchy
import logging
logger = logging.getLogger(__name__)
logger.propagate = False  # It will not pass log events to higher loggers, by default it is true
logger.info("This is helper")