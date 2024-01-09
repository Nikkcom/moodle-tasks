import nmap3
import json

results = None

scan_ip = "scanme.nmap.org/24"
json_path = "results.json"


def load_json():
    global json_path
    global results
    with open(json_path, "r") as file:
        results = json.load(file)


load_json()
