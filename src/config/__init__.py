import os
import importlib

from enum import Enum


class Environment(Enum):

    development = "development"
    test = "test"
    production = "production"

    def is_production(self):
        return self.value == "production"

    def is_not_dev(self):
        return self.value != "development"


# Determine the environment we want to load, default is development.py
env_str = os.environ.get("PROJECT_ENV", "development")

# load config files at run time
module = importlib.import_module(f".environments.{env_str}", package=f"src.config")

# update globals of this module (i.e. settings) with imported.
globals().update(vars(module))
