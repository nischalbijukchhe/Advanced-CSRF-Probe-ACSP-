import json

config = {
    "target_url": "",
    "payload_file": "",
    "threads": 10,
    "proxy": False,
    "user_agent": "Mozilla/5.0",
    "output_file": "results.txt",
    "burp_suite_integration": False,
    "zap_integration": False
}

def save_config():
    with open("config.json", "w") as f:
        json.dump(config, f)

def load_config():
    global config
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        pass

load_config()
