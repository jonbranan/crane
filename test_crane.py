import unittest
import requests
from json import load
from cclient import c_auth, c_get_containers, c_start_container, c_stop_container
from cprocess import build_cont_list

class TestCrane(unittest.TestCase):
    def setUp(self):
        with open('./config.json') as c:
            self.config = load(c)
        self.host = self.config["host"]
        self.port = self.config["port"]
        self.username = self.config["username"]
        self.password = self.config["password"]
        self.endpoint = self.config["endpoint"]
        self.cid = '06ffaed8153495db19b35f5982e0f9d4cfea0da7b803f825a6686a4017af8d6e'
        self.req_obj = requests
        self.hypercare_containers = ['hello-world']
    def test_c_auth(self):
        self.jwt = c_auth(self.req_obj, self.host, self.port, self.username, self.password)
        self.assertTrue(self.jwt, "No JWT returned by cauth.")

    def test_c_get_containers(self):
        self.jwt = c_auth(self.req_obj, self.host, self.port, self.username, self.password)
        self.cont_obj = c_get_containers(self.req_obj, self.host, self.port, self.jwt, self.endpoint)
        self.assertTrue(self.cont_obj, "No cont object returned by c_get_containers.")
    
    def test_build_cont_list(self):
        self.jwt = c_auth(self.req_obj, self.host, self.port, self.username, self.password)
        self.cont_obj = c_get_containers(self.req_obj, self.host, self.port, self.jwt, self.endpoint)
        self.cont_list = build_cont_list(self.cont_obj, self.hypercare_containers)
        self.assertTrue(self.cont_list, "No cont_list returned by build_cont_list.")
    
    def test_c_start_container(self):
        self.jwt = c_auth(self.req_obj, self.host, self.port, self.username, self.password)
        self.c_start_container_response = c_start_container(self.req_obj, self.host, self.port, self.jwt, self.endpoint, self.cid)
        print(self.c_start_container_response)
        self.assertTrue(self.c_start_container_response, "No c_start_container_resonse returned by c_start_container.")
        # 204 success 304 already on
    
    def test_c_stop_container(self):
        self.jwt = c_auth(self.req_obj, self.host, self.port, self.username, self.password)
        self.c_stop_container_response = c_stop_container(self.req_obj, self.host, self.port, self.jwt, self.endpoint, self.cid)
        print(self.c_stop_container_response)
        self.assertTrue(self.c_stop_container_response, "No c_start_container_resonse returned by c_start_container.")
if __name__ == '__main__':
    unittest.main()