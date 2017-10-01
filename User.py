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


    def create(self):
        pass

    def delete_user(self, user_id):
        pass
