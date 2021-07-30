import logging
logging.basicConfig(filename='error_log.txt',datefmt='%d/%B/%Y:%A-%(time:%I:%M:%S:%p:)',format='%(asctime)s-%(levelname)s-%(name)s-%(message)s-%(process)d',level=10,filemode='a')
logging.info('new request is made')
try:
    x=int(input('enter x:'))
    y=int(input('enter y:'))
    print('result:',round(x/y,4))
except ZeroDivisionError as msg:
    print('enter valid value only')
    logging.exception (msg)
except ValueError as msg:
    print('enter valid value only')
    logging.exception (msg)
logging.basicConfig(filename='error_log.txt',datefmt='%d/%B/%Y:%A-%(time:%I:%M:%S:%p:)',format='%(asctime)s-%(levelname)s-%(name)s-%(message)s-%(process)d',level=10,filemode='a')
logging.info('request completed')