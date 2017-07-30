import config

def getURL():
  return config.url

def getData(action, dir):
    if action == "scan":
      return getScanData(dir)
    elif action == "clean":
      return getCleanData(dir)


def getScanData(dir):
    if dir == "all":
      return {"jsonrpc": "2.0", "method": "VideoLibrary.Scan", "id": "pyScript"}
    elif dir == "tv":
      return {"jsonrpc": "2.0", "method": "VideoLibrary.Scan", "id": "pyScript", "params": {"directory": config.tvDir}}
    elif dir == "movies":
      return {"jsonrpc": "2.0", "method": "VideoLibrary.Scan", "id": "pyScript", "params": {"directory": config.moviesDir}}


def getCleanData(dir):
    if dir == "all":
      return {"jsonrpc": "2.0", "method": "VideoLibrary.Clean", "id": "pyScript"}
    elif dir == "tv":
      return {"jsonrpc": "2.0", "method": "VideoLibrary.Clean", "id": "pyScript", "params": {"directory": config.tvDir}}
    elif dir == "movies":
      return {"jsonrpc": "2.0", "method": "VideoLibrary.Clean", "id": "pyScript", "params": {"directory": config.moviesDir}}
