from pathlib import Path
from configparser import ConfigParser
import sys
#import Inventory.inventory_baseConfig as bc
cfgFile = 'env.ini'
cfgFileDir = 'Config'

config = ConfigParser()

BASE_DIR= Path(__file__).resolve().parent.parent

#print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFile)
config.read(CONFIG_FILE) #config is reading the env.ini


# Now, you can use Env, Client_name, and Product_name as needed in your script
Env = globals()["Env"]
Client_name = globals()["Client_name"]
Product_name = globals()["Product_name"]

class ConfigParser:
 def __init__(self, config_file='env.ini', config_dir='Config'):
     self.Config = ConfigParser()
     self.base_dir = Path(__file__).resolve().parent.parent
     self.config_file_path = self.base_dir.joinpath(config_dir).joinpath(config_file)
     self.Config.read(self.config_file_path)


urls_config = {
    'RL_Test': {'url': config['RL_Test']['url']},
    'SIGNET_Test': {'url': config['SIGNET_Test']['url']},
    'VB_Test': {'url': config['VB_Test']['url']},
    'RL_Replica': {'url': config['RL_Replica']['url']},
    'SIGNET_Replica': {'url': config['SIGNET_Replica']['url']},
    'RL_EU_Test': {'url': config['RL_EU_Test']['url']},
    'VB_Replica': {'url': config['VB_Replica']['url']},
    'DG_Test': {'url': config['DG_Test']['url']},
    'CARTERS_Test': {'url': config['CARTERS_Test']['url']},
    'RL_UAT': {'url': config['RL_UAT']['url']},
    'EU_UAT': {'url': config['EU_UAT']['url']},
    'VS_Test':{'url': config['VS_Test']['url']},
    'SIGNET_Uat': {'url': config['SIGNET_Uat']['url']}

}

def get_URL(Env ,Client_name):
    #global url
    if Env == "Test" and Client_name == "RL":
        baseURL = 'https://' + urls_config['RL_Test']['url']
    elif Env == "Test" and Client_name == "SIGNET":
        baseURL = 'https://' + urls_config['SIGNET_Test']['url']
    elif Env == "Test" and Client_name == "Mlops":
        baseURL = 'https://' + urls_config['VB_Test']['url']
    elif Env == "Replica" and Client_name == "RL":
        baseURL = 'https://' + urls_config['RL_Replica']['url']
    elif Env == "Replica" and Client_name == "SIGNET":
        baseURL = 'https://' + urls_config['SIGNET_Replica']['url']
    elif Env == "Replica" and Client_name == "VB":
        baseURL = 'https://' + urls_config['VB_Replica']['url']
    elif Env == "EU" and Client_name == "RL":
        baseURL = 'https://' + urls_config['RL_EU_Test']['url']
    elif Env == "Test" and Client_name == "DG":
        baseURL = 'https://' + urls_config['DG_Test']['url']
    elif Env == "Test" and Client_name == "CARTERS":
        baseURL = 'https://' + urls_config['CARTERS_Test']['url']
    elif Env == "UAT" and Client_name == "RL":
        baseURL = 'https://' + urls_config['RL_UAT']['url']
    elif Env == "UAT" and Client_name == "EU":
        baseURL = 'https://' + urls_config['EU_UAT']['url']
    elif Env == "Test" and Client_name == "VS":
        baseURL = 'https://' + urls_config['VS_Test']['url']
    elif Env == "UAT" and Client_name == "SIGNET":
        baseURL = 'https://' + urls_config['SIGNET_Uat']['url']

    else:
        baseURL = ''  # Default value for unsupported cases
    return baseURL


url = get_URL(Env, Client_name)
if url:
    print("Base URL IS:", url)
else:
    print("No matching URL found for the given client and environment.")

def get_client_name():
    # Replace this with your logic to get the correct client name
    return Client_name



