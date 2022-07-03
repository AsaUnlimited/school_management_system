from ntpath import join


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

    def edit_school_name(self, id, name):
        if id in School.schools_list.keys():
            print(School.schools_list[id])
            School.schools_list[id][0] = name
            print(School.schools_list[id])
            return School.schools_list[id]

    def edit_school_description(self, id, description):
        if id in School.schools_list.keys():
            print(School.schools_list[id])
            School.schools_list[id][1] = description
            print(School.schools_list[id])

    def edit_school_type(self, id, type):
        if id in School.schools_list.keys():
            print(School.schools_list[id])
            School.schools_list[id][2] = type
            print(School.schools_list[id])

    def delete(self, id):
        if id in School.schools_list.keys():
            School.schools_list.pop(id)
        return School.schools_list

    def search_school(self, school):
        for i,y in School.schools_list.items():
                if school in "".join(map(str, y)):
                    print(y)


school = School("alakara", "In God we trust", "secondary School")
school.add_school()
school = School("alabal", "God we trust", "secondary School")
school.edit_school_name(1, "boy")
school.edit_school_type(1, "primary")
school.edit_school_description(1, "God is my strength")
school.search_school("God we trust")

