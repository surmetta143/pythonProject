import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\cinfi.ini")

class Readconfig:
    @staticmethod
    def getApplicationurl():
        url = config.get("common info","baseurl")
        return url
    @staticmethod
    def getApplicationUsername():
        username = config.get("common info","username")
        return username
    @staticmethod
    def getApplicationPassword():
        password = config.get("common info","password")
        return password