import pushover
from tomllib import load

with open('./config.toml', mode="rb") as c:
    config = load(c)

po_key = config["pushover"]["po_key"]
po_token = config["pushover"]["po_token"]

message = "hello"

pushover.Pushover(po_token).message(po_key, message, title="--- crane summary ---")