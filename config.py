import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "bbe00afac676da96bb2ba3b7b3c1fdc9"
    SERVER_NAME = "localhost:7000"
