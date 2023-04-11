def process_cont_list(full_cont_list, start_cont_fn, req_obj, host, port, access_token, endpoint):
    if full_cont_list:
        #print(full_cont_list)
        started = []
        for container in full_cont_list:
            start_cont_fn(req_obj, host, port, access_token, endpoint, container["Id"])
            started.append(container["Names"][0].lstrip("/"))
        return started