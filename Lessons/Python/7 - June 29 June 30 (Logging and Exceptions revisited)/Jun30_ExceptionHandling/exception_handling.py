import logging

logging.basicConfig(filename="exception.log",level=logging.DEBUG)
#
# ---------
# try:
#     a = 10
#     a/0
# except Exception as e:
#     logging.error(e)
#     print("this line will be executed")
#
#
# ---------
# try:
#     f = open("steve.txt","r")
# except Exception as e:
#     logging.error(e)

# ---------
# try:
#     f = open("Steve.txt","r")
#     f.write("this is a line to write into the file")
# except Exception as e:
#     logging.error(e)
#     print("this statement will be executed")
# finally:
#     print("this FINALLY statement will be executed")

# ---------

# def askint():
#     try:
#         val = int(input("enter an integer: "))
#     except Exception as e:
#         logging.error(e)
#         try:
#             val = int(input("enter an integer: "))
#         except Exception as e:
#             logging.error(e)
#     finally:
#         print("this is finally executed")
#         # print(10/0)
#
# askint()


# ---------

def askint_loop():
    while True:
        try:
            val = int(input("Please enter an integer: "))
            break
        except Exception as e:
            logging.error("Integer not entered")
            continue
        # break # break can be mentioned here also

askint_loop()