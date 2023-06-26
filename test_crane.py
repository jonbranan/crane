import unittest
import requests
import json
from tomllib import load
from cclient import c_get_filtered_containers, c_start_container, c_stop_container, c_get_container_id
from cprocess import process_cont_list
unittest.TestLoader.sortTestMethodsUsing = None
requests.packages.urllib3.disable_warnings()

class TestCrane(unittest.TestCase):
    def setUp(self):
        with open('./config.toml', 'rb') as c:
            self.config = load(c)
        self.host = self.config["portainer"]["host"]
        self.port = self.config["portainer"]["port"]
        self.access_token = "ptr_ufS1nADXmrU3QSN3bvITLMQ7oOH9yo3ECb/QNwtIYJ4="
        self.endpoint = self.config["portainer"]["endpoint"]
        self.req_obj = requests
        self.j_obj = json
        self.hypercare_containers = ['hottub']
        self.status_filters = ["paused","dead","created","exited","removing","restarting","created"]

    def test_c_get_filtered_containers(self):
        self.cont_obj = c_get_filtered_containers(self.req_obj,self.j_obj, self.host, self.port, self.access_token, self.endpoint,self.hypercare_containers,self.status_filters)
        self.assertTrue(self.cont_obj, "No cont object returned by c_get_filtered_containers.")

    def test_c_start_container(self):
        self.cid = c_get_container_id(self.req_obj,self.j_obj, self.host, self.port, self.access_token, self.endpoint, self.hypercare_containers,self.status_filters)
        c_stop_container(self.req_obj, self.host, self.port, self.access_token, self.endpoint, self.cid)
        self.c_start_container_response = c_start_container(self.req_obj, self.host, self.port, self.access_token, self.endpoint, self.cid)
        self.assertTrue(self.c_start_container_response, "No c_start_container_resonse returned by c_start_container.")
        # 204 success 304 already on
    
    def test_c_process_cont_list(self):
        self.cont_obj = c_get_filtered_containers(self.req_obj,self.j_obj, self.host, self.port, self.access_token, self.endpoint,self.hypercare_containers,self.status_filters)
        self.assertTrue(process_cont_list(self.cont_obj, c_start_container, self.req_obj, self.host, self.port, self.access_token, self.endpoint))
    
    def test_c_stop_container(self):
        self.cid = c_get_container_id(self.req_obj,self.j_obj, self.host, self.port, self.access_token, self.endpoint, self.hypercare_containers,self.status_filters)
        self.c_stop_container_response = c_stop_container(self.req_obj, self.host, self.port, self.access_token, self.endpoint, self.cid)
        self.assertTrue(self.c_stop_container_response, "No c_start_container_resonse returned by c_start_container.")
        

if __name__ == '__main__':
    unittest.main()