import requests


class GeneralError(Exception):
    pass


class users:
    def topUsers():
        r = requests.get("https://api.wasteof.money/explore/users/top")
        return r.json()

    def IdToUser(id):
        r = requests.get(f"https://api.wasteof.money/username-from-id/{id}")
        j = r.json()
        return j["username"]

    def isUserAvailable(username):
        r = requests.get(
            f"https://api.wasteof.money/username-available?username={username}"
        )
        j = r.json()
        return j["available"]

    def getWall(username, page=1):
        r = requests.get(f"https://api.wasteof.money/users/{username}/wall?page={page}")
        return r.json()

    def postToWall(username, token, content):
        r = requests.post(
            f"https://api.wasteof.money/users/{username}/wall",
            headers={"Authorization": token},
            json={"content": content},
        )
        j = r.json()
        return j["id"]

    def replyOnWall(username, token, content, parent):
        r = requests.post(
            f"https://api.wasteof.money/users/{username}/wall",
            headers={"Authorization": token},
            json={"content": content, "parent": parent},
        )
        j = r.json()
        return j["id"]


class session:
    def auth(username, password):
        r = requests.post(
            "https://api.wasteof.money/session",
            json={"username": username, "password": password},
        )
        j = r.json()
        try:
            return j["token"]
        except:
            if "error" in j:
                raise GeneralError(j["error"])

    def get(token):
        r = requests.get(
            "https://api.wasteof.money/session", headers={"Authorization": token}
        )
        return r.json()

    def remove(token):
        r = requests.delete(
            "https://api.wasteof.money/session", headers={"Authorization": token}
        )
        j = r.json()
        return j["ok"]


class posts:
    def trending(timeframe="week"):
        r = requests.get(
            f"https://api.wasteof.money/explore/posts/trending?timeframe={timeframe}"
        )
        return r.json()

    def random():
        r = requests.get("https://api.wasteof.money/random-post")
        return r.json()

    def get(id):
        r = requests.get(f"https://api.wasteof.money/posts/{id}")
        return r.json()

    def getComments(id, page=1):
        r = requests.get(f"https://api.wasteof.money/posts/{id}/comments?page={page}")
        return r.json()

    def GetCommentReplies(id, page=1):
        r = requests.get(f"https://api.wasteof.money/comments/{id}/replies?page={page}")
        return r.json()

    def create(token, content):
        r = requests.post(
            "https://api.wasteof.money/posts",
            headers={"Authorization": token},
            json={"post": content},
        )
        j = r.json()
        return j["id"]

    def repost(token, content, id):
        r = requests.post(
            "https://api.wasteof.money/posts",
            headers={"Authorization": token},
            json={"post": content, "repost": id},
        )
        j = r.json()
        return j["id"]

    def edit(token, content, id):
        r = requests.put(
            f"https://api.wasteof.money/posts/{id}",
            headers={"Authorization": token},
            json={"post": content},
        )
        return r.json()

    def delete(token, id):
        r = requests.delete(
            f"https://api.wasteof.money/posts/{id}", headers={"Authorization": token}
        )
        j = r.json()
        return j["ok"]

    def comment(token, id, content):
        r = requests.post(
            f"https://api.wasteof.money/posts/{id}/comments",
            headers={"Authorization": token},
            json={"content": content},
        )
        j = r.json()
        return j["id"]

    def replyToComment(token, id, content, parent):
        r = requests.post(
            f"https://api.wasteof.money/posts/{id}/comments",
            headers={"Authorization": token},
            json={"content": content, "parent": parent},
        )
        j = r.json()
        return j["id"]

    def deleteComment(token, id):
        r = requests.delete(
            f"https://api.wasteof.money/comments/{id}", headers={"Authorization": token}
        )
        j = r.json()
        try:
            return j["ok"]
        except:
            if "error" in j:
                raise GeneralError(j["error"])

    def pin(token, id):
        r = requests.post(
            f"https://api.wasteof.money/posts/{id}/pin",
            headers={"Authorization": token},
        )
        j = r.json()
        return j["ok"]

    def unpin(token, id):
        r = requests.post(
            f"https://api.wasteof.money/posts/{id}/unpin",
            headers={"Authorization": token},
        )
        j = r.json()
        return j["ok"]

    def report(token, id, type, reason):
        r = requests.post(
            f"https://api.wasteof.money/posts/{id}/report",
            headers={"Authorization": token},
            json={"type": type, "reason": reason},
        )
        j = r.json()
        return j["ok"]

    def toggleLove(token, id):
        r = requests.post(
            f"https://api.wasteof.money/posts/{id}/loves",
            headers={"Authorization": token},
        )
        j = r.json()
        return j["ok"]

    def didUserLove(id, user):
        r = requests.get(f"https://api.wasteof.money/posts/{id}/loves/{user}")
        return r.json()


class messages:
    def getRead(token):
        r = requests.get(
            "https://api.wasteof.money/messages/read", headers={"Authorization": token}
        )
        return r.json()

    def getUnread(token):
        r = requests.get(
            "https://api.wasteof.money/messages/unread",
            headers={"Authorization": token},
        )
        return r.json()

    def count(token):
        r = requests.get(
            "https://api.wasteof.money/messages/count", headers={"Authorization": token}
        )
        j = r.json()
        return int(j["count"])

    # below ids need to be in an array
    def markRead(token, id):
        r = requests.post(
            "https://api.wasteof.money/messages/mark/read",
            json={"messages": id},
            headers={"Authorization": token},
        )
        j = r.json()
        return j["ok"]

    def markUnread(token, id):
        r = requests.post(
            "https://api.wasteof.money/messages/mark/unread",
            json={"messages": id},
            headers={"Authorization": token},
        )
        j = r.json()
        return j["ok"]


class oauth:
    def github():
        r = requests.get("https://api.wasteof.money/sessions/oauth/github/url")
        j = r.json()
        return j["url"]

    def google():
        r = requests.get("https://api.wasteof.money/sessions/oauth/google/url")
        j = r.json()
        return j["url"]


class search:
    def users(query):
        r = requests.get(f"https://api.wasteof.money/search/users/?q={query}")
        return r.json()

    def posts(query):
        r = requests.get(f"https://api.wasteof.money/search/posts/?q={query}")
        return r.json()


# class settings:
#   def get(token):
#    r = requests.get("https://api.wasteof.money/settings", headers={"Authorization": token})
#    return r.json()
