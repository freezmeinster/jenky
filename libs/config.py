import os
import sys
import ConfigParser

BASE_DIR = os.path.dirname(sys.modules['__main__'].__file__)

def get_config(section, item, type="str"):
    config_file = os.path.join(BASE_DIR, "default.conf")
    config = ConfigParser.SafeConfigParser()
    config.read([config_file, os.path.expanduser('~/.jenky.conf')])
    if type == "int":
        return config.getint(section, item)
    elif type == "float":
        return config.getfloat(section, item)
    elif type == "bool":
        return config.getboolean(section, item)
    else:
        return config.get(section, item)