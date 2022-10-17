import pushover
from json import load
from cclient import c_auth, c_get_containers
from clogging import *
import time
import datetime
import logging
import requests

class Crn:
    def __init__(self):
        """Main object, should be calling functions from qlist.py, qlogging.py and qprocess.py"""
        # Open the config. Needs a json file with the data in config.json.example
        self.st = datetime.datetime.now()
        with open('./config.json') as c:
            self.config = load(c)
        # Create the api object
        self.cc = requests
        # Create the logging and pushover objects
        self.tl = logging
        self.po = pushover
        
        # Init config.json
        self.use_pushover = self.config["use_pushover"]
        self.use_log = self.config["use_log"]
        self.po_key = self.config["po_key"]
        self.po_token = self.config["po_token"]
        self.log_path = self.config["log_path"]
        self.log_level = self.config["log_level"]
        self.host = self.config["host"]
        self.port = self.config["port"]
        self.username = self.config["username"]
        self.password = self.config["password"]
        self.endpoint = self.config["endpoint"]
        cont_log(self)
        cont_notify(self)
        self.t = time

        #logging in
        try:
            self.tl.info('Authenticating.')
            self.jwt = c_auth(self.cc, self.host, self.port, self.username, self.password)
            self.tl.info('Authenticated successfully.')
            self.cont_obj = c_get_containers(self.cc, self.host, self.port, self.jwt)
            self.tl.info('Collected container list.')
        except requests.exceptions.RequestException as e:
            self.tl.exception(e)
            self.po.send_message(e, title="crane API ERROR")

        #Main process block
        self.et = datetime.datetime.now()
        get_script_runtime(self)
        if self.use_pushover:
            cont_notify_summary(self)
# Run
if  __name__== "__main__":
    Crn()