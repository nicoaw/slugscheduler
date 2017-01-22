import Catalog

class Schedule:
    def __init__(self, transcript, requirements):
        self.quarters = {}
        self.transcript = transcript
        self.requirements = requirements

    # Build schedule for specific year and quarter
    def build(self, year, quarter, scoreboard):
        units = 0
        while not Catalog.is_satisfied(self.transcript, self.requirements):
            course = scoreboard.pop()

            # Only allowed 19 units
            if units + course.units > 19:
                break

            # Don't repeat a course
            if self.transcript.has(course.nbr):
                break

            # Course prereqs not met
            if not Catalog.is_satisfied(self.transcript, course.prereqs):
                break
            
            self.quarters[(year, quarter)] = course
            units += course.units

    # Get list of courses for specific year and quarter
    def get_quarter(self, year, quarter):
        return self.quarters[(year, quarter)]

    # Get earliest year for schedule
    def min_year(self):
        return self.min_year

    # Get most recent year for schedule
    def max_year(self):
        return self.max_year
