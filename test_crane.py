import unittest
import requests
from json import load
from cclient import c_auth, c_get_containers, c_start_container, c_stop_container
from cprocess import build_cont_list, process_cont_list, build_full_cont_list, process_cont_status
unittest.TestLoader.sortTestMethodsUsing = None

class TestCrane(unittest.TestCase):
    def setUp(self):
        with open('./config.json') as c:
            self.config = load(c)
        self.host = self.config["host"]
        self.port = self.config["port"]
        self.username = self.config["username"]
        self.password = self.config["password"]
        self.endpoint = self.config["endpoint"]
        self.cid = 'aa5b217ca6217fd9d268396039da69ea9e4a5aff381b3dceb71edb5a1f4d429d'
        self.req_obj = requests
        self.hypercare_containers = ['hello-world']
        self.jwt = c_auth(self.req_obj, self.host, self.port, self.username, self.password)
        self.cont_obj = c_get_containers(self.req_obj, self.host, self.port, self.jwt, self.endpoint)

    def test_c_auth(self):
        self.assertTrue(self.jwt, "No JWT returned by cauth.")

    def test_c_get_containers(self):
        self.assertTrue(self.cont_obj, "No cont object returned by c_get_containers.")

    def test_a_is_hypercare_container_status(self):
        self.cont_full_list = build_full_cont_list(self.cont_obj, self.hypercare_containers)
        self.process_cont_status_response = process_cont_status(self.cont_full_list)
        if self.process_cont_status_response == 0:
            c_stop_container(self.req_obj, self.host, self.port, self.jwt, self.endpoint, self.cid)
        
    def test_build_cont_list(self):
        self.cont_list = build_cont_list(self.cont_obj, self.hypercare_containers)
        self.assertTrue(self.cont_list, "No cont_list returned by build_cont_list. Does the test container exist?")

    def test_c_start_container(self):
        self.c_start_container_response = c_start_container(self.req_obj, self.host, self.port, self.jwt, self.endpoint, self.cid)
        # print(self.c_start_container_response)
        self.assertTrue(self.c_start_container_response, "No c_start_container_resonse returned by c_start_container.")
        # 204 success 304 already on
    
    def test_c_stop_container(self):
        self.c_stop_container_response = c_stop_container(self.req_obj, self.host, self.port, self.jwt, self.endpoint, self.cid)
        # print(self.c_stop_container_response)
        self.assertTrue(self.c_stop_container_response, "No c_start_container_resonse returned by c_start_container.")
    
    def test_process_cont_list(self):
        self.cont_list = build_cont_list(self.cont_obj, self.hypercare_containers)
        self.process_cont_list_response = process_cont_list(self.cont_list, c_start_container, self.req_obj, self.host, self.port, self.jwt, self.endpoint)
        self.assertTrue(self.process_cont_list_response, "No c_start_container_resonse returned by c_start_container.")
    
    def test_z_tear_down(self):
        c_stop_container(self.req_obj, self.host, self.port, self.jwt, self.endpoint, self.cid)
        

if __name__ == '__main__':
    unittest.main()