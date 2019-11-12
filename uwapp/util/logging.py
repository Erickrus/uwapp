# -*- coding: utf-8 -*-#

import sys
import uwapp.util.toolbox as toolbox

DEBUG = 4
INFO = 3
WARNING = 2
ERROR = 1
CRITICAL = 0

_level = DEBUG

#f = open("./logs/uwapp.log", "w")
f = open("./uwapp.log", "w")

class Logger:
    def __init__(self, name):
        if name == "__main__":
            name = sys.modules['__main__'].__file__
            p = name.find("uwapp")
            if p >= 0:
                name = name[name.find("uwapp"):].replace("/",".")[:-3]
            else:
                name = name[name.rfind("/")+1:][:-3]
        self.name = name
        _level = INFO
        self.fmt = "%Y-%m-%d %H:%M:%S.%f"
        
    def info(self, text):
        if _level >= INFO:
            ts = toolbox.get_timestamp(self.fmt)
            f.write("%s %s %-24s : %s \n"%(ts, 'INFO    ', self.name, str(text)))
            
    def debug(self, text):
        if _level >= DEBUG:
            ts = toolbox.get_timestamp(self.fmt)
            f.write("%s %s %-24s : %s \n"%(ts, 'DEBUG   ', self.name, str(text)))
        
    def warning(self, text):
        if _level >= WARNING:
            ts = toolbox.get_timestamp(self.fmt)
            f.write("%s %s %-24s : %s \n"%(ts, 'WARNING ', self.name, str(text)))
        
    def error(self, text):
        if _level >= ERROR:
            ts = toolbox.get_timestamp(self.fmt)
            f.write("%s %s %-24s : %s \n"%(ts, 'ERROR   ', self.name, str(text)))
    
    def critical(self, text):
        if _level >= CRITICAL:
            ts = toolbox.get_timestamp(self.fmt)
            f.write("%s %s %-24s : %s \n"%(ts, 'CRITICAL', self.name, str(text)))
            
    def setLevel(self, level):
        _level = level
        
    def flush(self):
        f.flush()

loggers = {}

def getLogger(name):
    if name in loggers:
        return loggers[name]
    else:
        return Logger(name)

    

