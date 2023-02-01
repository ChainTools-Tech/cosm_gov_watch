import threading

from cosm_gov_watch.api_requests import request_governance
from config_loader.load_config import load_chains
from prettytable import PrettyTable

proposals_table = PrettyTable()
proposals_table.title = f"Chain Proposals"
proposals_table.field_names = ["Chain", "ID", "Type", "Title", "Status"]
proposals_table.align = "l"
proposals_table.border = True

threads = []

def process_data(chain_name, chain_api):
    governance = request_governance(chain_api)
    proposals_table.add_row([chain_name,
                             "",
                             "",
                             "",
                             ""])
    try:
        for proposal in governance['proposals']:
            if proposal['status'] == "PROPOSAL_STATUS_VOTING_PERIOD":
                proposals_table.add_row([f'  {chain_name}',
                                         proposal['proposal_id'],
                                         proposal['content']['@type'].rsplit('.', 1)[-1],
                                         proposal['content']['title'][:60],
                                         proposal['status']])
    except KeyError as e:
        proposals_table.add_row([f'  {chain_name}',
                                 "API error",
                                 "API error",
                                 e,
                                 "API error"])

    proposals_table.add_row(["--------",
                             "--------",
                             "--------",
                             "--------",
                             "--------"])

def main():
    chains = load_chains()
    for chain in chains["chains"]:
        print(f'Processing: {chain["name"]} -> calling API: {chain["api"]}')
        t = threading.Thread(target=process_data, args=(chain["name"], chain["api"]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print (f'\rProcessing done. Displaying results.')
    print(proposals_table)


if __name__ == '__main__':
    main()