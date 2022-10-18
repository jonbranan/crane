# TODO add file for containers that need to be started
def build_cont_list(obj,hypercare_containers):
    cont_list = []
    for i, c in enumerate(obj):
        if c["State"].lower() != "running":
            if c["Names"][0].lstrip("/") in hypercare_containers:
                print(f'index: {i} container: {c["Names"][0].lstrip("/")} State: {c["State"]} ID: {c["Id"]}')
                cont_list.append(c)
    print(len(cont_list))
    return cont_list

def process_cont_list(full_cont_list, cont_fn):
    pass