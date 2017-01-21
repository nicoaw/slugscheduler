class Transcript:
    def __init__(self):
        self.courses = {}
        self.units = 0

    # Take course
    def add(self, catalog, nbr):
        self.courses[nbr] = True
        self.units += catalog.get_units(nbr)

    # Has student taken course
    def has(self, nbr):
        return nbr in self.courses

    # Are the prereqs meet for course
    def is_satisfied(self, catalog, nbr):
        for prereq in catalog.get_prereqs(nbr):
            if not (prereq in self.courses):
                return False
        return True
