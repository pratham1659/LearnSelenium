import os
import configparser

current_script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_script_dir, '..', ))
config = configparser.RawConfigParser()
config_path = os.path.join(root_dir, 'Configuration', 'config.ini')
config.read(config_path)

class ReadConfig:

    @staticmethod
    def get_browser():
        browser = config.get('basic_info', 'browser')
        return browser

    @staticmethod
    def get_url():
        url = config.get('basic_info', 'baseUrl')
        return url

    @staticmethod
    def get_useremail():
        username = config.get('basic_info', 'useremail')
        return username

    @staticmethod
    def get_password():
        passcode = config.get('basic_info', 'password')
        return passcode
