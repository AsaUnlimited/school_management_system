class School:
    id = 0
    schools_list = {}
    def __init__(self,school_name,school_description,school_type):
        School.id += 1
        self.school_name = school_name
        self.school_description = school_description
        self.school_type = school_type
    def add_school(self):
        School.schools_list[School.id] = [self.school_name, self.school_type, self.school_description]
        return f"{self.school_name} has already been added to the Schools"

class EditSchool(School):
    def __init__(self, id):
        self.id = id
        # super().schools_list
    def name(self, name):
        if self.id in School.schools_list.keys():
            print(School.schools_list[self.id])
            School.schools_list[self.id][0] = name
            print(School.schools_list[self.id])
        return School.schools_list[self.id]
    def description(self, description):
        if self.id in School.schools_list.keys():
            print(School.schools_list[self.id])
            School.schools_list[self.id][1] = description
            print(School.schools_list[self.id])
    def type(self, type):
        if self.id in School.schools_list.keys():
            print(School.schools_list[self.id])
            School.schools_list[self.id][3] = type
            print(School.schools_list[self.id])
first_school = School("alakara", "In God we trust", "secondary School")
first_school.add_school()
second_school = School("alabal", "God we trust", "secondary School")
second_school.add_school()
