# Quarter enumerations
FALL = 1
WINTER = 2
SPRING = 3
SUMMER = 4

class Catalog:
    def __init__(self):
        self.courses = {}

    # Add a new course
    def add_course(self, nbr, title, units, prereqs):
        self.courses[nbr] = {
                'title': title,
                'units': units,
                'prereqs': prereqs,
                'offerings': []
                }

    # Add  offering
    def add_offering(self, nbr, year, quarter):
        self.courses[nbr]['offerings'] += [(year, quarter)]

    # Get course
    def get_course(self, nbr):
        return self.courses[nbr]

    # Is course offered at certain year, quarter
    def is_offered(self, nbr, year, quarter):
        return (year, quarter) in self.courses[nbr]['offerings']
