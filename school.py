class School():
    school_id = 0
    school_list = {}
    def __init__(self, school_name, school_description, school_type):
        School.school_id += 1
        self.school_description = school_description
        self.school_name = school_name
        self.school_type = school_type

    def addSchool(self):
        School.school_list = {self.school_id:[self.school_name, self.school_type, self.school_description]}
        return f"School of {self.school_name}, type {self.school_type} with motto: {self.school_description} have successfully been added"

    def editSchool(self):


sch1 = School("Semicolon", "Go placidly", "Ed-Tech")
print(sch1.addSchool())
print(sch1.school_list)