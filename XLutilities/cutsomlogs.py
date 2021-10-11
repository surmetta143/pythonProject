import logging

class Test_Base_log:
   @staticmethod
   def log_name():
       logger = logging.getLogger(__name__)
       filehandler = logging.FileHandler(".\\logs\\  + logfiles.log")
       format = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
       filehandler.setFormatter(format)

       logger.addHandler(filehandler)
       logger.setLevel(logging.INFO)

       return logger
