import json
import requests
import argparse
import helpers

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--action", type=str,
                    choices=["scan", "clean"], default="scan", help="Sets library method")
parser.add_argument("-d", "--dir", type=str,
                    choices=["all", "tv", "movies"], default="all", help="Sets directory")
args = parser.parse_args()


def __main__():
    print(args.action, "->", args.dir)
    r = requests.post(helpers.getURL(), json=helpers.getData(args.action, args.dir))


__main__()
