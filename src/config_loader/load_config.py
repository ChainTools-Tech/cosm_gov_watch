import os
import sys
import tomli


def load_chains():
    chains_config_path = os.path.abspath(os.path.dirname(__file__)) + '\chains.toml'
    try:
        with open(chains_config_path, mode="rb") as chains_file:
            loaded_chains = tomli.load(chains_file)
    except IOError:
        sys.exit("Can't load chains.toml.")

    return loaded_chains
