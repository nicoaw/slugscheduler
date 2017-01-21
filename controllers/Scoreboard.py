import Queue

class Scoreboard:
    def __init__(self, transcript, catalog):
        self.ratings = Queue.PriorityQueue()
        self.transcript = transcript
        self.catalog = catalog

    def empty(self):
        return self.ratings.empty()

    # Rate courses in catalog
    def rate(self):
        self.ratings.queue.clear()

        # Rate courses from catalog
        # CODE HERE

    # Pop best course to schedule
    def pop(self):
        self.ratings.get()[1]
