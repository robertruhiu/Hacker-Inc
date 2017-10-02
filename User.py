class User :
    def __init__(self) :
        self.__id = None # set by the db engine if data's gon be saved in a db
                         # else we'll have to make it a static field and increament
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




class UserManager:

    def __init__(self):
        self.__users = []

    def add_user(self, user):
        

    def create(self):
        pass

    def delete_user(self, user_id):
        pass

        # def

    def person_exists(self, name) :
        people = self.__users
        for person in people :

            if (person.get_name() == name) :
                return person
        return False

    def is_empty(self) :
        """
        :param self:
        :param type: string
        :return:
        """
        return (len(self.__users) == 0)

    def add_person(self, person) :
        people = self.__users 
        if self.is_empty() :
            people.append(person)

        else :
            if not self.person_exists(person.get_name()) :
                people.append(person)
            else :
                return "contact already exists"

    def remove_person(self, person_name) :
        people = self.__users 
        if self.is_empty() :
            return "cannot remove from an empty list"
        else :
            person = self.person_exists(person_name)

            if person :
                people.remove(person)
                return person
            else :
                return "eit not found"

    def find(self, person_name):
        person = self.person_exists(person_name)

        return "person not found" if person == False else person