def c_auth(req_obj, host, port, username, password):
    url = f'https://{host}:{port}/api/auth'
    c_auth_response = req_obj.post(url, json={"Username":username,"Password":password}, verify=False)
    return c_auth_response.json()["jwt"]

def c_get_containers(req_obj, host, port, jwt, endpoint):
    url = f'https://{host}:{port}/api/endpoints/{endpoint}/docker/containers/json?all=true'
    c_get_containers_response = req_obj.get(url, headers={"Authorization": f"Bearer {jwt}"},verify=False)
    return c_get_containers_response.json()

#filters={"name": ["restic","qbittorrent"],"status": ["paused","dead","created","exited","removing","restarting","created"]}
def c_get_filtered_containers(req_obj, host, port, jwt, endpoint, containers, statuses):
    url = f'https://{host}:{port}/api/endpoints/{endpoint}/docker/containers/json?filters={"name": {containers},"status": {statuses}}'
    c_get_containers_response = req_obj.get(url, headers={"Authorization": f"Bearer {jwt}"},verify=False)
    return c_get_containers_response.json()

def c_start_container(req_obj, host, port, jwt, endpoint, cid):
    url = f'https://{host}:{port}/api/endpoints/{endpoint}/docker/containers/{cid}/start'
    c_start_container_response = req_obj.post(url, headers={"Authorization": f"Bearer {jwt}"},verify=False)
    return c_start_container_response.status_code

def c_stop_container(req_obj, host, port, jwt, endpoint, cid):
    url = f'https://{host}:{port}/api/endpoints/{endpoint}/docker/containers/{cid}/stop'
    c_start_container_response = req_obj.post(url, headers={"Authorization": f"Bearer {jwt}"},verify=False)
    return c_start_container_response.status_code