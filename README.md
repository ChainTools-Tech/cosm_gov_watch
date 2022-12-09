# Cosmos Governance Watcher
Script pulls list of active proposals from chains enumerated in configuration file.
Governance proposals information is pulled via API endpoint.
Once information is collected script produces table with collected data.
Even if particular chain has no active proposals it will be listed in table.

[Installation Video](https://odysee.com/@ChainToolsScripts:5/ct_Scripts_cosm_gov_watch:4)

## Requirements
 - Python 3.8 or newer
 - Python Virtual Environment

## Installation

1. Clone repository and create a Python virtual environment
```bash
$ git clone https://github.com/ChainTools-Tech/cosm_gov_watch
$ cd cosm_gov_watch
$ python -m venv ./venv
$ source venv/bin/activate
(venv) $
```

2. Install the requirements
```bash
(venv) $ python -m pip install -r requirements.txt
```

3. Install script
```bash
(venv) $ pip install -e .
```

## Configuration
List of chains to check along with endpoints is located in ```config_loader/chains.toml``` file. 
Each chain is described as example below:
```toml
[[chains]]
name = "cosmoshub"
displayname = "Cosmos Hub"
chain-id = "cosmoshub-4"
rpc = "https://rpc.cosmos.chaintools.tech:443"
api = "https://api.cosmos.chaintools.tech:443"
```

In order to add another chain create new section and populate with appropriate information.
If some chains are not needed just remove chain section from configuration file.



## Usage
```
(venv) $ cosm_gov_watch              
+---------------------------------------------------------------------------------------------------------------------------------+
|                                                         Chain Proposals                                                         |
+---------------+-----+------------------------------+--------------------------------------------+-------------------------------+
| Chain         | ID  | Type                         | Title                                      | Status                        |
+---------------+-----+------------------------------+--------------------------------------------+-------------------------------+
| beezee        | --  | --                           | --                                         | --                            |
| bitsong       | --  | --                           | --                                         | --                            |
| carbon        | --  | --                           | --                                         | --                            |
| chihuahua     | --  | --                           | --                                         | --                            |
| comdex        | --  | --                           | --                                         | --                            |
| cosmoshub     | --  | --                           | --                                         | --                            |
| cosmoshub     | 81  | TextProposal                 | Atom Zero Constitution                     | PROPOSAL_STATUS_VOTING_PERIOD |
| cosmoshub     | 82  | TextProposal                 | ATOM 2.0: A new vision for Cosmos Hub      | PROPOSAL_STATUS_VOTING_PERIOD |
| cosmoshub     | 83  | TextProposal                 | Atom One Constitution (sentiment proposal) | PROPOSAL_STATUS_VOTING_PERIOD |
| decentr       | --  | --                           | --                                         | --                            |
| desmos        | --  | --                           | --                                         | --                            |
| evmos         | --  | --                           | --                                         | --                            |
| evmos         | 78  | RegisterCoinProposal         | Register ERC20 for Injective (INJ)         | PROPOSAL_STATUS_VOTING_PERIOD |

...
```
In case of any questions contact support@chaintools.tech


## ToDo
- [X] api_requests : error handling
- [ ] load_config : error handling
