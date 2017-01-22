import Catalog
import Queue
import re

class Scoreboard:
    def __init__(self):
        self.ratings = Queue.PriorityQueue()

    def empty(self):
        return self.ratings.empty()

    # Rate courses in catalog
    def rate(self):
        # Clear ratings
        while not self.empty():
            self.pop()

        # Rate courses from catalog
        courses = Catalog.get_courses()

        # First pass: count times course is a prereq
        requisites = {}
        for nbr in courses:
            course = Catalog.get_course(nbr)
            m = re.search('"([^"]+)"', course.prereqs)
            if m:
                for prereq in m.groups():
                    if prereq in requisites:
                        requisites[prereq] += 1
                    else:
                        requisites[prereq] = 1

        # Second pass: score course
        for nbr in courses:
            course = Catalog.get_course(nbr)
            score = 0
            for quarter in [Catalog.FALL, Catalog.WINTER, Catalog.SPRING, Catalog.SUMMER]:
                if Catalog.is_offered(course, quarter):
                    score += 1
            score -= 4 * (requisites[nbr] if nbr in requisites else 0)
            self.ratings.put((score, course))

    # Pop best course to schedule
    def pop(self):
        item = self.ratings.get()
        return item[1]
