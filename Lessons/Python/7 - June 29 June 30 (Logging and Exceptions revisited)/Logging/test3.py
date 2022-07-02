import logging
logging.basicConfig(filename="test3.log",level=logging.INFO,format="%(asctime)s %(name)s %(levelname)s %(message)s")


def divide(a,b):
    logging.info("The number entered is %s and %s",a,b)
    try:
        logging.info("we are inside the function")
        div = a/b
        logging.info("we have completed the division")
        return div
    except Exception as e:
        logging.exception(e)

print(divide(3,0))
