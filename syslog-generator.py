import logging
import logging.handlers

logging.Formatter(fmt='myscriptname[%(process)d]: %(levelname)s: %(message)s')
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)


# Send to Rsyslog
handler = logging.handlers.SysLogHandler(address = ('10.38.225.78',514))
# Send to loopback
#handler = logging.handlers.SysLogHandler(address = ('127.0.0.1',514))


my_logger.addHandler(handler)


try:
    print("Start Syslog send")
    i = 0
    my_logger.critical('Start lopp message')
    while 1 <= 10:
        my_logger.debug("This is message {0}".format(i))
        i = i + 1
    While i <= 10:
        my_logger.debug("This is message {0}".format(i))
        i = i + 1

    my_logger.critical('this is critical')
    print("Stop Syslog Send")
except:
    print("Failed on Unit Testing")



