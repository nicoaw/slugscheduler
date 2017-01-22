import Catalog

class Schedule:
    def __init__(self, transcript, requirements):
        self.quarters = []
        self.transcript = transcript
        self.requirements = requirements

    # Build schedule for specific year and quarter
    def build(self, scoreboard):
        self.quarters += []
        units = 0
        while True:
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

            if self.is_done()
                break
            
            self.quarters[:-1] += [course]
            units += course.units

    def is_done(self):
        return Catalog.is_satisfied(self.transcript, self.requirements)

