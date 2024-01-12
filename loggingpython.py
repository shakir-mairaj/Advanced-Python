#Differnet Log Levels
import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s- %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S')
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")
# import helper

# Log Handlers- responsible for dispatching the appropriate log messages to the handler's specific destination
logger = logging.getLogger(__name__)

#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler("file.log")

#level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.CRITICAL)

formatter = logging.Formatter('%(name)s - %(levelname)s- %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

#add handler
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is a warning")
logger.critical("This is critical")

# using logging.conf file
import logging.config
logging.config.fileConfig('logging.conf')

logger = logging.getLogger('logger_simpleExample')
logger.debug("This is a debug message")

# Capturing Stack Traces
import traceback

try:
    a=[1, 2, 3]
    val = a[4]
# except IndexError as e:
#     logging.error(e, exc_info=True)

except:
    logging.error("The traceback is %s",traceback.format_exc())

# Rotating file handler
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# This will create a new log file every minute, and 5 backup files with a timestamp before overwriting old logs.
handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backupCount=5)
logger.addHandler(handler)

for i in range(6):
    logger.info('Hello, world!')
    time.sleep(50)

# time rotating file handler
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# This will create a new log file every minute, and 5 backup files with a timestamp before overwriting old logs.
handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backupCount=5)
logger.addHandler(handler)

for i in range(6):
    logger.info('Hello, world!')
    time.sleep(50)

# Logging in json format
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)



