class User:
    def __init__(self):
        self.__followers = []

    def add_follower(self, follower):
        """
        Adds a follower(user object) to a list

        :rtype: object
        :param follower: a user object
        """
        self.__followers.append(follower)

    def remove_follower(self, id_of_follower):
        """
        Removes a follower(user object) from list by id

        :rtype: object
        :param id_of_follower: the name of the follower to remove
        :return: an object of the user if removed else None object
        """
        for a_follower in self.__followers:
            if id_of_follower == a_follower.id:
                self.__followers.remove(a_follower)
                return a_follower
        return None
