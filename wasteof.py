import requests

class AuthenticationError(Exception):
    pass

class users():
    def topUsers():
        r = requests.get('https://api.wasteof.money/explore/users/top')
        return(r.json())
    
    def IdToUser(id):
        r = requests.get(f"https://api.wasteof.money/username-from-id/{id}")
        j = r.json()
        return(j["username"])
    
    def isUserAvailable(username):
        r = requests.get(f"https://api.wasteof.money/username-available?username={username}")
        j = r.json()
        return(j["available"])
class session():
    def auth(username, password):
        r = requests.post("https://api.wasteof.money/session", json = {"username": username, "password": password})
        j = r.json()
        try:
            return(j["token"])
        except:
            if "error" in j:
                raise AuthenticationError(j["error"])
    def get(token):
        r = requests.get("https://api.wasteof.money/session", headers={"Authorization":token})
        return(r.json())
    
    def remove(token):
        r = requests.delete("https://api.wasteof.money/session", headers={"Authorization":token})
        j = r.json()
        return(j["ok"])


class posts():
    
    def trending(timeframe = "week"):
        r = requests.get(f'https://api.wasteof.money/explore/posts/trending?timeframe={timeframe}')
        return(r.json())
    
    def random():
        r = requests.get("https://api.wasteof.money/random-post")
        return(r.json())

class messages():
    def getRead(token):
        r = requests.get("https://api.wasteof.money/messages/read", headers={"Authorization":token})
        return(r.json())
    
    def getUnread(token):
        r = requests.get("https://api.wasteof.money/messages/unread", headers={"Authorization":token})
        return(r.json())
    
    def count(token):
        r = requests.get("https://api.wasteof.money/messages/count", headers={"Authorization":token})
        j = r.json()
        return(int(j["count"]))
    
    def markRead(token,id):
        r = requests.post("https://api.wasteof.money/messages/mark/read", json = {"messages":id} , headers = {"Authorization":token})
        j = r.json()
        return(j["ok"])
    
    def markUnread(token,id):
        r = requests.post("https://api.wasteof.money/messages/mark/unread", json = {"messages":id} , headers = {"Authorization":token})
        j = r.json()
        return(j["ok"])