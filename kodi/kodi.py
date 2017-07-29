import json, requests, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--action", type=str, choices=["scan", "clean"], default="scan", help="Sets library method")
parser.add_argument("-d", "--dir", type=str, choices=["all", "tv", "movies"], default="all", help="Sets directory")
args = parser.parse_args()

url = 'http://192.168.1.204:80/jsonrpc'

def getData():
	if args.action == "scan":
		return getScanData()
	elif args.action == "clean":
		return getCleanData()

def getScanData():
	if args.dir == "all":
		return {"jsonrpc": "2.0", "method": "VideoLibrary.Scan", "id": "pyScript"}
	elif args.dir == "tv":
		return {"jsonrpc": "2.0", "method": "VideoLibrary.Scan", "id": "pyScript", "params":{"directory":"smb://192.168.1.201/tvAuto/"}}
	elif args.dir == "movies":
		return {"jsonrpc": "2.0", "method": "VideoLibrary.Scan", "id": "pyScript", "params":{"directory":"smb://192.168.1.202/x264/"}}

def getCleanData():
	if args.dir == "all":
		return {"jsonrpc": "2.0", "method": "VideoLibrary.Clean", "id": "pyScript"}
	elif args.dir == "tv":
		return {"jsonrpc": "2.0", "method": "VideoLibrary.Clean", "id": "pyScript", "params":{"directory":"smb://192.168.1.201/tvAuto/"}}
	elif args.dir == "movies":
		return {"jsonrpc": "2.0", "method": "VideoLibrary.Clean", "id": "pyScript", "params":{"directory":"smb://192.168.1.202/x264/"}}

def __main__():
  print(args.action, "->", args.dir)
  r = requests.post(url, json=getData())