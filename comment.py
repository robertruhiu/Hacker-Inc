
class Reply:
    def __init__(user, content):
        self.user = user
        self.content = content


class Comment:
    def __init__(user, content):
        self.user = user
        self.content = content
        likes = 0
        replies = []
    
    def add_reply(self, reply):
        self.replies.append(reply)

    def delete_reply(self, reply):
        for rep in self.replies:
            if rep == reply:
                self.replies.pop(rep)