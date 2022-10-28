from tomllib import load

with open('./config.toml', mode="rb") as c:
    config = load(c)

print(config["containers"].values())