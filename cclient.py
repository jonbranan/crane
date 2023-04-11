def c_get_containers(req_obj, host, port, access_token, endpoint):
    url = f'https://{host}:{port}/api/endpoints/{endpoint}/docker/containers/json?all=true'
    c_get_containers_response = req_obj.get(url, headers={"X-API-Key": access_token},verify=False)
    return c_get_containers_response.json()

def c_get_filtered_containers(req_obj, j_obj, host, port, access_token, endpoint, containers, statuses):
    filter_string = j_obj.dumps({"name":containers,"status":statuses})
    # url = 'https://192.168.4.11:9443/api/endpoints/1/docker/containers/json?filters={"name": ["restic","qbittorrent"],"status": ["paused","dead","created","exited","removing","restarting","created"]}'
    url = f'https://{host}:{port}/api/endpoints/{endpoint}/docker/containers/json?filters={filter_string}'
    c_get_containers_response = req_obj.get(url, headers={"X-API-Key": access_token}, verify=False)
    return c_get_containers_response.json()

def c_start_container(req_obj, host, port, access_token, endpoint, cid):
    url = f'https://{host}:{port}/api/endpoints/{endpoint}/docker/containers/{cid}/start'
    c_start_container_response = req_obj.post(url, headers={"X-API-Key": access_token},verify=False)
    return c_start_container_response.status_code

def c_stop_container(req_obj, host, port, access_token, endpoint, cid):
    url = f'https://{host}:{port}/api/endpoints/{endpoint}/docker/containers/{cid}/stop'
    c_start_container_response = req_obj.post(url, headers={"X-API-Key": access_token},verify=False)
    return c_start_container_response.status_code