import pushover
import json
from cclient import *
from clogging import *
from cprocess import *
import time
import datetime
import logging
import requests
from tomllib import load
import os

class Crn:
    def __init__(self):
        """Main object, should be calling functions from qlist.py, qlogging.py and qprocess.py"""
        # Open the config. Needs a json file with the data in config.json.example
        self.st = datetime.datetime.now()

        config_file_path=os.environ["toml_path"]
        with open(config_file_path, 'rb') as c:
            self.config = load(c)
        if os.path.exists('./config.toml'):
            config_file_path = './config.toml'
            with open(config_file_path, 'rb') as c:
                self.config = load(c)

        # Create the api object
        self.cc = requests
        # Create the logging and pushover objects
        self.tl = logging
        self.po = pushover
        self.jn = json
        #Load settings from config.toml
        #portainer
        self.host = self.config["portainer"]["host"]
        self.port = self.config["portainer"]["port"]
        self.access_token = self.config["portainer"]["access_token"]
        self.endpoint = self.config["portainer"]["endpoint"]
        self.start_containers = self.config["portainer"]["start_containers"]
        #logging
        self.use_log = self.config["logging"]["use_log"]
        self.log_path = self.config["logging"]["log_path"]
        self.log_level = self.config["logging"]["log_level"]
        #pushover
        self.use_pushover = self.config["pushover"]["use_pushover"]
        self.po_key = self.config["pushover"]["po_key"]
        self.po_token = self.config["pushover"]["po_token"]
        #containers
        self.observed_containers = list(self.config["containers"].values())
        self.container_statuses = ["paused","dead","created","exited","removing","restarting","created"]

        cont_log(self)
        cont_notify(self)
        self.t = time

        #logging in
        try:
            # c_get_filtered_containers(req_obj, j_obj, host, port, access_token, endpoint, containers, statuses)
            self.cont_obj = c_get_filtered_containers(self.cc, self.jn, self.host, self.port, self.access_token, self.endpoint,self.observed_containers,self.container_statuses)
            # print(self.cont_obj)
            self.tl.debug('Collected container data.')
            self.process_cont_list_response = process_cont_list(self.cont_obj, c_start_container, self.cc, self.host, self.port, self.access_token, self.endpoint)
            if self.process_cont_list_response:
                self.tl.warning(f'Started: {self.process_cont_list_response}')

        except requests.exceptions.RequestException as e:
            self.tl.exception(e)
            self.poc.message(self.po_key, e, title="crane API ERROR")

        #Main process block
        self.et = datetime.datetime.now()
        get_script_runtime(self)
        if self.use_pushover:
            cont_notify_summary(self)
# Run
if  __name__== "__main__":
    Crn()