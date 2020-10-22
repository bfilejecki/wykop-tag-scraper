import os
from yaml import safe_load


basedir = os.path.abspath(os.path.dirname(__file__))
secrets_path = os.path.join(basedir, 'secrets.yml')


class Config(object):

    APP_KEY = safe_load(open(secrets_path, 'r'))["app-key"]
    APP_SECRET = safe_load(open(secrets_path, 'r'))["app-secret"]
