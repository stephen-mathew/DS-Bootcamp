import logging

logging.basicConfig(filename="test.log",level=logging.INFO)
logging.info("this is my first logging log")
l = [1,2,3,4,5,6]
logging.warning("this is a warning")
logging.error("this is an error message")
for i in l:
    if i == 2:
        logging.info(i)
logging.debug("Debug message")
logging.shutdown()
logging.info("log after shutdown")