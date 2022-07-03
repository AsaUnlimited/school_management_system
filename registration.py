from datetime import date


class Registration:
    registration_id: int = 0
    registration_date = date.today()

    def __init__(self, registration_type: str, registration_description: str, registration_number: str,
                 registration_student_id: int, registration_name: str):
        self.registration_type = registration_type
        self.registration_description = registration_description
        self.registration_number = registration_number
        self.registration_student_id = registration_student_id
        self.registration_name = registration_name
        Registration.registration_id += 1

    def add_registration(self):
        return f"Application of {self.registration_name}, {self.registration_number}, {self.registration_student_id}, {self.registration_type}\
         and {self.registration_description} on {Registration.registration_date} was successful and the new id is {Registration.registration_id}"


Reg1 = Registration("high schhol reg", "welcome to our college", 212, 2341, "funmi florence")
print(Reg1.add_registration())
