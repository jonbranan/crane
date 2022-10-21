# TODO add file for containers that need to be started
def build_cont_list(obj, hypercare_containers):
    cont_list = []
    for i, c in enumerate(obj):
        if c["State"].lower() != "running":
            if c["Names"][0].lstrip("/") in hypercare_containers:
                #print(f'index: {i} container: {c["Names"][0].lstrip("/")} State: {c["State"]} ID: {c["Id"]}')
                cont_list.append(c)
    return cont_list

def build_full_cont_list(obj, hypercare_containers):
    cont_full_list = []
    for i, c in enumerate(obj):
        if c["Names"][0].lstrip("/") in hypercare_containers:
            #print(f'index: {i} container: {c["Names"][0].lstrip("/")} State: {c["State"]} ID: {c["Id"]}')
            cont_full_list.append(c)
    return cont_full_list

def process_cont_list(full_cont_list, start_cont_fn, req_obj, host, port, jwt, endpoint):
    if full_cont_list:
        for container in full_cont_list:
            start_cont_fn(req_obj, host, port, jwt, endpoint, container["Id"])
        return True

def process_cont_status(obj):
    if not obj:
        return -1 # Can't find the containter
    for c in enumerate(obj):
        # print(c[1]['Names'][0].lstrip("/"))
        if 'running' in c[1]["State"].lower():
            return 0
        if c[1]["State"] != 'running':
            return 1