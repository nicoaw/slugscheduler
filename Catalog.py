class Course:
    def __init__(self, nbr, title, units, prereqs):
        self.nbr = nbr
        self.title = title
        self.units = units
        self.prereqs = prereqs
        self.offerings = []

    def add_offering(self, year, quarter):
        self.offerings += [(year, quarter)]

    def is_offered(self, year, quater):
        return (year, quarter) in self.offerings

class Catalog:
    def __init__(self):
        self.courses = {}

    # Add a new course
    def add_course(self, course):
        self.courses[course.nbr] course

    # Get course
    def get_course(self, nbr):
        return self.courses[course.nbr]
