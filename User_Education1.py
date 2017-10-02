class School:
    def __init__(self, name, year_completed=None, course_studied="", year_started=None, school_url=" "):
        """
        :param name:
        :param year_completed:
        :param course_studied:
        :param year_started:
        :param school_url:
        :return:
        """
        self.__name = name
        self.__year_completed = year_completed
        self.__year_started = year_started
        self.__course_studied = course_studied

    def get_name(self):
        return self.__name


class User_Education:
    def __init__(self):
        self.__schools = []

    def school_exists(self, school_name):
        """
        :param school_name:
        :return:
        """
        schools = self.__schools
        for school in schools:

            if school.get_name() == school:
                return school
        return False

    def add_school(self, school):
        # FIXME implement this well
        self.__schools.append(school)

    def is_schools_list_empty(self):
        """
        :param self:
        :param type: string
        :return:
        """
        return (len(self.__schools) == 0)

    def remove_school(self, school_name):
        """
        :param user_id:
        :return:
        """
        schools = self.__schools
        if self.is_schools_list_empty():
            return "cannot remove from an empty list"
        else:
            school = self.school_exists(school_name)

            if school:
                school.remove(school)
                return school
            else:
                return "school not found"

    def find_school(self, school):
        """
        :param user_id:
        :return:
        """
        school = self.school_exists(school)

        return "user not found" if school == False else school


user_education = User_Education()

print(user_education.add_school(School("ana")))
# print (user_education.add_school(input("Enter School name: ")))
