# Quarter enumerations
FALL = 1
WINTER = 2
SPRING = 3
SUMMER = 4

class Catalog:
    def __init__(self):
        self.courses = {}
        self.min_year = None
        self.max_year = None

    # Add courses for a year from url
    def add(self, year, url):
        # Scrape url page for course information
        # Course(title, units, prereqs, offerings)

        if self.min_year is None or self.min_year > year:
            self.min_year = year
        if self.max_year is None or self.min_year < year:
            self.max_year = year

    # Get course nbrs available
    def get_courses(self):
        return self.courses.keys()

    # Get course title
    def get_title(self, nbr):
        return self.courses[nbr][0]

    # Get course units
    def get_units(self, nbr):
        return self.courses[nbr][1]

    # Get course prereqs (a list of course nbrs)
    def get_prereqs(self, nbr):
        return self.courses[nbr][2]

    # Is course offered at certain year, quarter
    def is_offered(self, nbr, year, quarter):
        return (year, quarter) in self.courses[nbr]['offerings']

    # Get earliest year recorded
    def min_year(self):
        return self.min_year

    # Get most recent year recorded
    def max_year(self):
        return self.max_year
