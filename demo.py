from us_visa.logger import logging
import sys
from us_visa.exception import USvisaException
logging.info("Hello")

try:
    a=1/0
except Exception as e:
    raise USvisaException(e,sys)
