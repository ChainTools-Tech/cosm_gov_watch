import pkg_resources
import sys
import tomli

from importlib import resources


def load_chains():
    try:
        with resources.open_binary("config", "chains.toml") as config_chains:
            loaded_chains = tomli.load(config_chains)
    except IOError:
        sys.exit("Can't load chains.toml.")

    return loaded_chains
