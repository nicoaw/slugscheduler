class Schedule:
    def __init__(self, catalog, transcript):
        self.quarters = {}
        self.catalog = catalog
        self.transcript = transcript

    # Build schedule for specific year and quarter
    def build(self, year, quarter, scoreboard):
        # Add courses to correct year quarter
        # [(year, quarter)] = <courses>
        # CODE HERE

        return

    # Get list of courses for specific year and quarter
    def get_quarter(self, year, quarter):
        return self.quarters[(year, quarter)]

    # Get earliest year for schedule
    def min_year(self):
        return self.min_year

    # Get most recent year for schedule
    def max_year(self):
        return self.max_year
