import logging

logging.basicConfig(filename="test5.log",level=logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s %(message)s")

try:
    logging.info("------")
    logging.info("Trying to read a file")
    with open('steve.txt',"r"):
        logging.info("successfully it has read the file")
except Exception as e:
    logging.critical("this is a critical situation")
    logging.error(e)
    logging.exception(e)

