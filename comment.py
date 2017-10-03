
class Reply:
    def __init__(self, user, content):
        self.__user = user
        self.__content = content


class Comment:
    def __init__(self, user, content):
        self.__user = user
        self.__content = content
        self.__likes = 0
        self.__replies = []
    
    def add_like_to_comment(self):
        self.__likes += 1

    def add_reply(self, reply):
        self.__replies.append(reply)

    def delete_reply(self, reply):
        for rep in self.replies:
            if rep == reply:
                self.replies.pop(rep)