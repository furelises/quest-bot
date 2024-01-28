import layer
import json
import os
from pathlib import Path

db_path = "./db"


class User:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.vars = {}
        for file in os.listdir(db_path):
            if str(user_id) == Path(file).stem:
                with open(f"{db_path}/{file}") as f:
                    self.vars = json.load(f)
                    break

    def dump(self):
        with open(f"./db/{self.user_id}.json", "w") as f:
            json.dump(self.vars, f)

    def restart(self):
        self.vars = {}
        self.dump()

    def get_path(self):
        return self.vars.get("path", [])

    def handler(self, layer_id):
        path = self.get_path()
        path.append(layer_id)
        self.vars["path"] = path
        self.dump()
