import requests

class AuthenticationError(Exception):
    pass

def TopUsers():
    r = requests.get('https://api.wasteof.money/explore/users/top')
    return(r.json())

def trending(timeframe = "week"):
    print(timeframe)
    r = requests.get('https://api.wasteof.money/explore/posts/trending?timeframe=' + timeframe)
    return(r.json())

def userToId(id):
    r = requests.get("https://api.wasteof.money/username-from-id/" + id)
    j = r.json()
    return(j["username"])

def getSession(username, password):
    r = requests.post("https://api.wasteof.money/session", json = {"username": username, "password": password})
    j = r.json()
    try:
        return(j["token"])
    except:
        if "error" in j:
            raise AuthenticationError(j["error"])


