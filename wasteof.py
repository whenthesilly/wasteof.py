import requests


class GeneralError(Exception):
    pass


class UnknownUserError(Exception):
    pass


class WallError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class users:
    def get(username: str) -> dict:
        """a function to get the info of a user
        Args:
            username (str): a wasteof.money username

        Returns:
            dict: the info of the user you requested
        """
        r = requests.get(f"https://api.wasteof.money/users/{username}")
        j = r.json()
        if not "error" in j:
            return j
        else:
            raise UnknownUserError(j["error"])

    def topUsers() -> dict:
        """a function to get top users

        Returns:
            dict: a dict containing top users
        """
        r = requests.get("https://api.wasteof.money/explore/users/top")
        return r.json()

    def IdToUser(id: str) -> str:
        """a function to get the username of a user via the ID

        Args:
            id (str): a wasteof.money user ID

        Raises:
            UnknownUserError: an error containing the error from the server

        Returns:
            str: a wasteof.money username
        """
        r = requests.get(f"https://api.wasteof.money/username-from-id/{id}")
        j = r.json()
        if "username" in j:
            return j["username"]
        else:
            raise UnknownUserError(j["error"])

    def isUserAvailable(username: str) -> bool:  # I think it is bool
        """a function to see if a username is available

        Args:
            username (str): a wasteof.money username

        Raises:
            UnknownUserError: an error containing the error from the server

        Returns:
            bool: a boolean stating if the username if available
        """
        r = requests.get(
            f"https://api.wasteof.money/username-available?username={username}"
        )
        j = r.json()
        if "available" in j:
            return j["available"]
        else:
            raise UnknownUserError(j["error"])  # I think

    def getWall(username: str, page: int = 1) -> dict:
        """a function to get a username's wall

        Args:
            username (str): the username to get the wall of
            page (int, optional): the page number of the wall. Defaults to 1.

        Raises:
            WallError: an error containg the error from the server
            WallError: an error stating the end of wall has been found

        Returns:
            dict: a dictionary containing that page of the wall
        """
        r = requests.get(f"https://api.wasteof.money/users/{username}/wall?page={page}")
        j = r.json()
        if not "error" in j:
            if j["comments"] == [] and j["last"]:
                raise WallError("end of wall")
            else:
                return j
        else:
            raise WallError(j["error"])
        return r.json()

    def postToWall(username: str, token: str, content: str) -> str:
        """a function to post a comment to a wall

        Args:
            username (str): the username of the wall you want to post on
            token (str): your wasteof.money session token
            content (str): the content of your wall comment

        Raises:
            WallError: an error containing the error from the server

        Returns:
            str: the comment ID
        """
        r = requests.post(
            f"https://api.wasteof.money/users/{username}/wall",
            headers={"Authorization": token},
            json={"content": content},
        )
        j = r.json()
        if not "error" in j:
            return j["id"]
        else:
            raise WallError(j["error"])

    def replyOnWall(username: str, token: str, content: str, parent: str) -> str:
        """a function to reply to a wall comment

        Args:
            username (str): the username of the wall you want to post on
            token (str): your wasteof.money session token
            content (str): the content of your wall comment
            parent (str): the ID of the parent comment

        Raises:
            WallError: an error containing the error from the server

        Returns:
            str: the comment ID
        """
        r = requests.post(
            f"https://api.wasteof.money/users/{username}/wall",
            headers={"Authorization": token},
            json={"content": content, "parent": parent},
        )
        j = r.json()
        if not "error" in j:
            return j["id"]
        else:
            raise WallError(j["error"])


class session:
    def auth(username: str, password: str) -> str:
        """a function to get your wasteof.money session token

        Args:
            username (str): your wasteof.money username
            password (str): your wasteof.money password

        Raises:
            AuthenticationError: an error containing the error from the server

        Returns:
            str: your wasteof.money session token
        """
        r = requests.post(
            "https://api.wasteof.money/session",
            json={"username": username, "password": password},
        )
        j = r.json()
        try:
            return j["token"]
        except:
            if "error" in j:
                raise AuthenticationError(j["error"])

    def get(token: str) -> dict:
        """a function to get session information

        Args:
            token (str): your wasteof.money session token

        Raises:
            AuthenticationError: an error containing the error from the server

        Returns:
            dict: session information
        """
        r = requests.get(
            "https://api.wasteof.money/session", headers={"Authorization": token}
        )
        j = r.json()
        if not "error" in j:
            return j
        else:
            raise AuthenticationError(j["error"])

    def remove(token: str) -> str:
        """a function to remove a wasteof.money session

        Args:
            token (str): your wasteof.money session token

        Raises:
            AuthenticationError: an error containing the error from the server

        Returns:
            str: success
        """
        r = requests.delete(
            "https://api.wasteof.money/session", headers={"Authorization": token}
        )
        j = r.json()
        if not "error" in j:
            return j["ok"]
        else:
            raise AuthenticationError(j["error"])


class posts:
    def trending(timeframe: str = "week") -> dict:
        """function to get trending posts

        Args:
            timeframe (str, optional): timeframe of posts. Defaults to "week".

        Returns:
            dict: _description_
        """
        r = requests.get(
            f"https://api.wasteof.money/explore/posts/trending?timeframe={timeframe}"
        )
        return r.json()

    def random() -> dict:
        """a functon to get a random post

        Returns:
            dict: the random post
        """
        r = requests.get("https://api.wasteof.money/random-post")
        return r.json()

    def get(id: str) -> dict:
        """a function to get a post by ID

        Args:
            id (str): the post ID

        Returns:
            dict: the post
        """
        r = requests.get(f"https://api.wasteof.money/posts/{id}")
        return r.json()

    def getComments(id: str, page: int = 1) -> dict:
        """a function to get comments of a post

        Args:
            id (str): the post ID to get comments of
            page (int, optional): the page of comments to get. Defaults to 1.

        Returns:
            dict: the comments of a post and a key called 'last' indicating if it is the last page of comments
        """
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
