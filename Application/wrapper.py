import logging
import sys
from datetime import datetime
import wrapper

now = datetime.now()
current_time = now.strftime("%m-%d-%Y-%H:%M:%S")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("/MonitoringApp/Logging/logs"+ current_time + ".log",'w+'),
        logging.StreamHandler(sys.stdout)
    ]
)
def wrap(pre, post):
	""" Wrapper """
	def decorate(func):
		""" Decorator """
		def call(*args, **kwargs):
			""" Actual wrapping """
			pre(func)
			result = func(*args, **kwargs)
			post(func)
			return result
		return call
	return decorate

def entering(func):
	""" Pre function logging """
	logging.info("Entered %s", func.__name__)

def exiting(func):
	""" Post function logging """
	logging.info("Exited  %s", func.__name__)
