class User :
    users_count = 0
    def __init__(self, first_name, last_name, email, password) :

        #region private props
        User.users_count += 1

        self.__id = User.users_count # set by the db engine if data's gon be saved in a db
                         # else we'll have to make it a static field and increment
                         #  it anytime an object is created out of this class
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__gender = None
        self.__password = password
        self.__date_registered = None
        self.__dob = None
        self.__educational_background = None #will contain an object of the ed_bg class

        self.__headline = None
        self.__country = None
        self.__zipcode = None
        self.__profile_img = None
        self.__summary = None
        self.__links = [] # a list of urls
        self.__skills = None
        self.__interest = [] # a list of interests<String>

        self.__followers = [] # a list of user ids
        self.__following = [] # a list of user ids
        self.__connections = [] # a list of user ids

        self.__posts = [] # a list of post ids
        #endregion

    def get_id(self):
        """
        :return:
        """
        return self.__id

    def set_id(self, id):
        self.__id = id

    # def edit(self, id = 0, ):

    def __repr__(self):
        return "{} {}".format(self.__first_name, self.__last_name )






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
            # User.users_count += 1
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

    def find_user_by_id(self, user_id):
        """
        :param user_id:
        :return:
        """
        person = self.person_exists(user_id)

        return "user not found" if person == False else person

    # TODO

    def edit_user(self, user_id, new_data : dict):
        """
        :param user_id: int
        :param new_data: {"first_name" : string, "last_name" : string}
        :return:
        """

        temp_user = self.find_user_by_id(user_id)
        # print(temp_user)
        valid_keys = temp_user.__dict__.keys()

        for key in new_data.keys():
            new_key = "_User__" + key
            if new_key in valid_keys:
                # print(new_data[key])
                temp_user.__dict__[new_key] = new_data[key]
        return temp_user


mgr = UserManager()

mgr.add_user(User("kwame", "nsiah", "ss@sds.cof", "asadssd"))
mgr.add_user(User("kwabena", "agyekum", "ss@sds.cof", "asadssd"))
# print(mgr.find_user_by_id(1))
# print(mgr.find_user_by_id(2))

print(mgr.edit_user(1, {"first_name" : "new name", "last_name" : "nw-lst-nm"}))
