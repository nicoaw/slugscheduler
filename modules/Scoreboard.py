import Queue

class Scoreboard:
    def __init__(self, transcript):
        self.ratings = Queue.PriorityQueue()
        self.transcript = transcript

    def empty(self):
        return self.ratings.empty()

    # Rate courses in catalog
    def rate(self):
        # Rate courses from catalog
        # CODE HERE

    # Pop best course to schedule
    def pop(self):
        self.ratings.get()[1]
