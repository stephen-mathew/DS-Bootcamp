import logging

logging.basicConfig(filename="test2.log",level=logging.DEBUG,format='%(asctime)s %(name)s %(levelname)s %(message)s')

logging.info("Logging with timestamp")
logging.debug("Debug with timestamp")