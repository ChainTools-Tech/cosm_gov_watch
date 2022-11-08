import argparse


def process_command_line():
    """Command line processor

    :return: parameters
    """
    cmdparser = argparse.ArgumentParser(prog='cosm_gov_watch',
                                        usage='%(prog)s [options] path',
                                        description='Command line application.')
    cmdparser.version = "0.1"

    cmdparser.add_argument("-l", "--log",
                           type=str,
                           nargs=1,
                           action="store",
                           dest="log",
                           choices=["debug", "info", "warning", "error", "critical"],
                           required=False,
                           help="defines error logging level")

    cmdparser.add_argument("-v", "--version", action="version")
    args = cmdparser.parse_args()

    return args.log[0]
