from canvasapi import Canvas
from configparser import ConfigParser

# Read config file
file = "config.ini"
config = ConfigParser()
config.read(file)

# Canvas API URL
API_URL =  "https://example.com/api/v1/"

# API Key
API_KEY = config['canvas']['api_key']

# Init new Canvas obj
# canvas = Canvas(API_URL, API_KEY)