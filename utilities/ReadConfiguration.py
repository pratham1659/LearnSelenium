from configparser import ConfigParser

def read_configuration(category,key):
    config = ConfigParser()
    config.read("env.ini")
    return config[category][key]