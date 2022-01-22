import logging
import sys
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

logFile = '/var/log/serverio.log'

file_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024, 
                                 backupCount=2, encoding=None, delay=0)
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.INFO)

# stdout_handler = logging.StreamHandler(sys.stdout)

# handlers = [file_handler, stdout_handler]

# logging.basicConfig(
#     level=logging.DEBUG, 
#     format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
#     handlers=handlers
# )

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# if (logger.hasHandlers()):
#     logger.handlers.clear()

logger.addHandler(file_handler)