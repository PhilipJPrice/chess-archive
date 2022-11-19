"""App configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Set app configuration from environment variables."""
    USERNAME = environ.get('USERNAME')
    OUTPUT_PATH = environ.get('OUTPUT_PATH')