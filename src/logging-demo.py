import logging
import sys



'''
Basic Config support the following settings

    level: Set root logger to the specified severity level.
    filename: Specifies the file to write log to (when running in Cloud9 the log out goes to the terminal, when running under AWS ECS the log output is automaticall sent to Cloudwatch)
    filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
    format: Defines the format of the log message
    
'''

# For the log level, you can try: DEBUG, INFO, WARNING, ERROR, CRITICAL in that order to restrict the log messages that are created

# basicConfig can only called once in program

logging.basicConfig(level=logging.ERROR)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')