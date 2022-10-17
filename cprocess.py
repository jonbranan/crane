def build_cont_list(obj):
    cont_list = []
    for i, c in enumerate(obj):
        if c["State"].lower() != "running":
            print(f'index: {i} container: {c["Names"][0].lstrip("/")} State: {c["State"]} ID: {c["Id"]}')
            cont_list.append(c)
    print(len(cont_list))
    return cont_list