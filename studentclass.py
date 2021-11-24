# https://docs.python.org/3/tutorial/modules.html#packages

class StudentClass:
    """A class that creates a student object.
    student_fname is the students first name.
    student_lname is the students last name.
    student_age is the students age.
    student_absences is the cummulative number of the students absences."""
    
    def __init__(self, student_fname, student_lname, student_age, student_absences):
        # You can give .__init__() any number of parameters, but the first parameter will always be a variable called self.
        # In Python, you both declare and define attributes inside the class __init__()
        self.student_fname = student_fname
        self.student_lname = student_lname
        self.student_age = student_age
        self.student_absences = student_absences
        
    def student_info(self):
        """Method that returns info on the student object."""
        return '{} {} is {} years old and has a total of {} absences.'.format(self.student_fname, self.student_lname, 
                                                                            self.student_age, self.student_absences)
    def status(self, student_status):
        """Function that returns a student objects status."""
        return '{} {}\'s status is {}.'.format(self.student_fname, self.student_lname, student_status)
    
    # This method will change the default print() output when instantiating the class object
    def __str__(self):
        return 'This returns the __str__ method.'
    
    def term(self, student_term):
        return '{} {} is enrolled in the {} term.'.format(self.student_fname, self.student_lname, student_term)
    
class SecondSemester(StudentClass): # Notice we are passing the StudentClass class as a parameter.
    """A Child Class of the StudentClass.
    It inherits the attributes of the Parent Class, StudentClass."""

    def next_term(self, student_term = 'Jan. 2022'):
        """A default constructor method that returns the start of the next semester."""
        return '{} {} is enrolled in the {} term.'.format(self.student_fname, self.student_lname, student_term)