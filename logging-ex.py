from  logging import *
print(dir())
#l.basicConfig(format='%(levelname)s')
#l.basicConfig(format='%(levelname)s:%(message)s',level=10,filemode='w')
basicConfig(datefmt='%d/%B/%Y:%A-%(time:%I:%M:%S:%p:)',format='%(asctime)s-%(levelname)s-%(name)s-%(message)s-%(process)d',level=10,filemode='w')
#refer python's official documentation of logging for more formats

#filemode a-for append w-for overwrite
#print(logging-ex.__file__)
info('info level with process id and time stamp')
debug('debuge level with process id and time stamp')
error('error level with process id and time stamp')
warning('warning level with process id and time stamp')
critical('critical level with process id and time stamp')
print()

basicConfig(filename='a_log.txt',format='%(levelname)s:%(message)s',level=10,filemode='w')
info('info level')
debug('debuge level')
error('error level')
warning('warning level')
critical('critical level')