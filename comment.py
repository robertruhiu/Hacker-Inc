
class Reply:
    def __init__(self, user, content):
        self.user = user
        self.content = content


class Comment:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.likes = 0
        self.replies = []
    
    def add_like_to_comment(self):
        self.likes += 1

    def add_reply(self, reply):
        self.replies.append(reply)

    def delete_reply(self, reply):
        for rep in self.replies:
            if rep == reply:
                self.replies.pop(rep)