import Queue

class Scoreboard:
    def __init__(self):
        self.ratings = Queue.PriorityQueue()

    # Rate courses in catalog
    def rate(self, catalog):
        # Rate courses from catalog
        # Rating(score, nbr)
        pass

    # Pop best course to schedule
    def pop(self):
        self.ratings.get()[1]
