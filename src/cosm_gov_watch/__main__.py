from cosm_gov_watch.api_requests import request_governance
from config_loader.load_config import load_chains
from prettytable import PrettyTable

proposals_table = PrettyTable()
proposals_table.title = f"Chain Proposals"
proposals_table.field_names = ["Chain", "ID", "Type", "Title", "Status"]
proposals_table.align = "l"
proposals_table.border = True


def main():
    chains = load_chains()
    for chain in chains["chains"]:
        proposals_table.add_row([chain["name"],
                                 "--",
                                 "--",
                                 "--",
                                 "--"])
        governance = request_governance(chain["api"])
        try:
            for proposal in governance['proposals']:
                if proposal['status'] == "PROPOSAL_STATUS_VOTING_PERIOD":
                    proposals_table.add_row([chain["name"],
                                             proposal['proposal_id'],
                                             proposal['content']['@type'].rsplit('.', 1)[-1],
                                             proposal['content']['title'][:60],
                                             proposal['status']])
        except KeyError as e:
            proposals_table.add_row([chain["name"],
                                     "API error",
                                     "API error",
                                     "API error",
                                     "API error"])

    print(proposals_table)


if __name__ == '__main__':
    main()