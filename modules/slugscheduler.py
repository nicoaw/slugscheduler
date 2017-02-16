import constraint

class Choice(constraint.Constraint):
    def __init__(self, items, count=1):
        self.items = items
        self.count = count

    def __call__(self, variables, domains, assignments, forwardcheck=False, _unassigned=constraint.Unassigned):
        # Items already satisfied
        satisfied = set(assignments.values()).intersection(self.items)
        return len(satisfied) >= self.count or len(assignments) < len(variables)

class SlugScheduler(object):
    def __init__(self, config={}, **changes):
        self.config = config
        self.config.update(changes)

    # Make a schedule
    def schedule(self, courses, program):
        problem = constraint.Problem()

        # Don't repeat courses
        problem.addConstraint(constraint.AllDifferentConstraint())

        # Add program requirement constraints
        for requirement in program.requirements:
            problem.addConstraint(requirement)

        # Add course prerequisite constraints
        for course in courses.values():
            if len(course.prerequisites) > 0:
                problem.addConstraint(self._make_prerequisites(course))

        # Find minimum schedule
        for n in range(len(courses) + 1):
            # Update variable count
            problem._variables.clear()
            problem.addVariables(range(n), courses.keys())

            solution = problem.getSolution()
            if solution:
                return self._make_schedule(courses, solution)

        # No schedule found
        return []

    # Make prerequisites constraint from course
    def _make_prerequisites(self, course):
        class Prerequisites(constraint.Constraint):
            def __init__(self, item, requirements):
                self.item = item
                self.problem = constraint.Problem()

                # Fill prerequisite constraints
                for requirement in requirements:
                    self.problem.addConstraint(requirement)

            def __call__(self, variables, domains, assignments, forwardcheck=False, _unassigned=constraint.Unassigned):
                if self.item in assignments.values():
                    self.problem._variables.clear()

                    # Check previous assignments meet prerequisites
                    for variable, value in assignments.iteritems():
                        if value == self.item:
                            break
                        self.problem.addVariable(variable, [value])
                    return self.problem.getSolution() is not None
                
                # Don't need to check prerequisites since item is not in assignments
                return True

        return Prerequisites(course.name, course.prerequisites)

    # Convert solution format to schedule format
    def _make_schedule(self, courses, solution):
        # Make schedule as a list
        schedule = [None] * (max(solution.keys()) + 1)

        # Fill schedule list
        for n, course in solution.iteritems():
            schedule[n] = [courses[course]]

        return schedule
