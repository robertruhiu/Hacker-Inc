class User :
    def __init__(self) :
        self.__id = None # set by the db engine if data's gon be saved in a db
                         # else we'll have to make it a static field and increment
                         #  it anytime an object is created out of this class
        self.__firs_tname = None
        self.__last_name = None
        self.__email = None
        self.__gender = None
        self.__password = None
        self.__date_registered = None
        self.__dob = None
        self.__educational_background = None #will contain an object of the ed_bg class

        self.__headline = None
        self.__country = None
        self.__zipcode = None
        self.__profile_Img = None
        self.__summary = None
        self.__links = [] # a list of urls
        self.__skills = None
        self.__of = None
        self.__string = None
        self.__interest = [] # a list of interests<String>

        self.__followers = [] # a list of user ids
        self.__following = [] # a list of user ids
        self.__connections = [] # a list of user ids

        self.__posts = [] # a list of post ids

    def get_id(self):
        """
        :return:
        """
        return self.__id


class UserManager:

    def __init__(self):
        self.__users = []


    def delete_user(self, user_id):
        """

        :param user_id:
        :return:
        """
        self.remove_user(user_id)

        # def

    def person_exists(self, user_id) :
        """

        :param user_id:
        :return:
        """
        people = self.__users
        for person in people :

            if (person.get_id() == user_id) :
                return person
        return False

    def is_empty(self) :
        """
        :param self:
        :param type: string
        :return:
        """
        return (len(self.__users) == 0)

    def add_user(self, person) :
        """

        :param person:
        :return:
        """
        people = self.__users 
        if self.is_empty() :
            people.append(person)

        else :
            if not self.person_exists(person.get_id()) :
                people.append(person)
            else :
                return "user already exists"

    def remove_user(self, user_id) :
        """

        :param user_id:
        :return:
        """
        people = self.__users 
        if self.is_empty() :
            return "cannot remove from an empty list"
        else :
            person = self.person_exists(user_id)

            if person :
                people.remove(person)
                return person
            else :
                return "user not found"

    def find_user(self, user_id):
        """

        :param user_id:
        :return:
        """
        person = self.person_exists(user_id)

        return "user not found" if person == False else person