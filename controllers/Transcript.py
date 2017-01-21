class Transcript:
    def __init__(self):
        self.courses = {}
        self.units = 0

    # Take course
    def add(self, nbr):
        self.courses[nbr] = True

    # Has student taken course
    def has(self, nbr):
        return nbr in self.courses

    # Get students units taken already
    def get_units(self):
        return self.units
