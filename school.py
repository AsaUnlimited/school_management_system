class School:
    school_id = 0
    school_list = {}

    def __init__(self, school_name, school_description, school_type):
        School.school_id += 1
        self.school_description = school_description
        self.school_name = school_name
        self.school_type = school_type

    def addSchool(self):
        School.school_list[School.school_id] = [self.school_name, self.school_type, self.school_description]
        return f"School of {self.school_name}, type {self.school_type} with motto: {self.school_description} have " \
               f"successfully been added "

    @staticmethod
    def delete_school_by_id(new_id):
        if new_id in School.school_list.keys():
            School.school_list.pop(new_id)
            return School.school_list

    @staticmethod
    def edit_school_name(new_id, new_name):
        if new_id in School.school_list.keys():
            School.school_list[new_id][0] = new_name
            return School.school_list

    @staticmethod
    def edit_school_description(new_id, new_description):
        if new_id in School.school_list.keys():
            School.school_list[new_id][1] = new_description
            return School.school_list

    @staticmethod
    def search_school_by_id(search_id):
        list(filter(lambda s: search_id in School.school_list.keys(), School.school_list))


sch1 = School("Semicolon", "Go placidly", "Ed-Tech")
# print(sch1.addSchool())
sch2 = School("Iyanfoworogi", "We discpline any nonsense out of children", "we keep home disturbers busy")
# print(sch2.addSchool())
# print(School.school_list)

print(School.search_school_by_id(1))
# print(sch1.edit_school_name(1, "unilag"))
# print(sch1.edit_school_description(1, "For always there will be greater and lesser person than yourself"))
