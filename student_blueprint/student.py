class Student:
    def __init__(self, major, gpa):
        self.major = major
        self.gpa = gpa
    
    def isFirstClass(self):
        if(self.gpa >= 3.7):
            return True
        else:
            return False