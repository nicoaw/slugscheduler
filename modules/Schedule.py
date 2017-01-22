import Catalog

class Schedule:
    def __init__(self, transcript, requirements):
        self.quarters = []
        self.transcript = transcript
        self.requirements = requirements

    # Build schedule for specific year and quarter
    def build(self, scoreboard):
        quarters = [Catalog.FALL, Catalog.WINTER, Catalog.SPRING, Catalog.SUMMER]
        qname = quarters[len(self.quarters) % 4]
        quarter = []
        units = 0
        print len(self.quarters), qname
        while True:
            #print 'loop'
            # No more courses to take
            if scoreboard.empty():
                #print 'empty'
                break

            course = scoreboard.pop()

            # Don't repeat a course
            if self.transcript.has(course.nbr) or course in quarter:
                #print 'has', course.nbr
                continue

            # Course prereqs not met
            if not Catalog.is_satisfied(self.transcript, course.prereqs):
                #print 'is_satisfied', course.nbr
                continue

            # Not offered this quarter
            if not (qname in course.offerings):
                #print 'offerings', course.nbr
                continue

            # Only allowed 19 units
            if units + course.units > 19:
                #print 'units', course.nbr
                break

            # Meet requirements
            if self.is_done():
                #print 'done'
                break
            
            quarter += [course]
            units += course.units
            #print 'units =', units
            print course.nbr, course.title, course.units

        for course in quarter:
            self.transcript.add(course.nbr)
        self.quarters += [quarter]
        print ''

    # Done with requirements
    def is_done(self):
        return Catalog.is_satisfied(self.transcript, self.requirements)

