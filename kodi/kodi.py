from time import gmtime, strftime
import json
import requests
import argparse
import helpers

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--action", type=str,
                    choices=["scan", "clean"], default="scan", help="Sets library method")
parser.add_argument("-d", "--dir", type=str,
                    choices=["all", "series", "movies"], default="all", help="Sets directory")
args = parser.parse_args()


def __main__():
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), args.action, "->", args.dir)
    requests.post(helpers.getURL(), json=helpers.getData(args.action, args.dir))

if __name__ == '__main__':
  __main__()
