import os
import json

# One level (the root of the package)
config_dir = os.path.dirname(os.path.dirname(__file__))
# Append file name of the required credentials file to get full path
config_path = os.path.join(config_dir, 'credentials.json')

# Read the credentials into a dictionary
with open(config_path, 'r') as credential_file:
    credentials = json.load(credential_file)
