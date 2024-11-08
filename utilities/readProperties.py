import os
import configparser


def read_configuration(category, key):
    # Get the directory of the current script (test_login.py)
    current_script_dir = os.path.dirname(os.path.abspath(__file__))

    # Move up one levels to the root directory (from TestCases/CARTERS to the root)
    root_dir = os.path.abspath(os.path.join(current_script_dir, '..',))

    # Construct the path to the config file
    config_path = os.path.join(root_dir, 'Configuration', 'config.ini')

    print(f"Config Path: {config_path}")

    # Read the config file
    config = configparser.ConfigParser()
    config.read(config_path)

    # Return the desired config value
    return config.get(category, key)
