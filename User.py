class User:
    def __init__(self):
        self.__followers = []

    def add_follower_id(self, id_of_follower):
        if id_of_follower not in self.__followers:
            self.__followers.append(id_of_follower)
            return True
        else:
            return False

    def remove_follower_id(self, id_of_follower):
            self.__followers.remove(id_of_follower)

    def get_all_followers_ids(self):
        """
        :return:
        """
        return self.__followers


class UserManager:
    def __init__(self):
        self.__users = []

    def person_exists(self, user_id):
        """
        :param user_id:
        :return:
        """
        people = self.__users
        for person in people:

            if (person.get_id() == user_id):
                return person
        return False

    def add_follower(self, user_id, id_of_follower):
        """
        Adds a follower to a user

        :param id_of_follower:
        :param user_id:
        :rtype:
        :param follower: a user object
        """
        if (user_id is None) or (id_of_follower is None):
            return "please supply \"user_id\" and or \"id_of_follower\""

        temp_user = self.find_user_by_id(user_id)

        if temp_user != "user not found":
            user = User(temp_user)
            temp_user = None
            user.add_follower_id(id_of_follower)
        else:
            return "follower not added because user does not exist"

    def remove_follower(self, user_id, id_of_follower):
        """
        Removes a follower(user object) from list by id

        :param user_id:
        :rtype: object
        :param id_of_follower: the name of the follower to remove
        :return: an object of the user if removed else None object
        """
        if (user_id is None) or (id_of_follower is None):
            return "please supply \"user_id\" and or \"id_of_follower\""

        temp_user = self.find_user_by_id(user_id)

        if temp_user != "user not found":
            if id_of_follower in User(temp_user).get_all_followers_ids():
                User(temp_user).remove_follower_id(id_of_follower)
                return True
        else:
            return "follower not added because user does not exist"

    def find_user_by_id(self, user_id):
        """
        :param user_id:
        :return:
        """
        person = self.person_exists(user_id)

        return "user not found" if person == False else person
