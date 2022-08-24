import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs.log",'w+'),
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
