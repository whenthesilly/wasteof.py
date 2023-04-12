import requests

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


