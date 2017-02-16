import constraint

class Choice(constraint.Constraint):
    def __init__(self, items, count=1):
        self.items = items
        self.count = count

    def __call__(self, variables, domains, assignments, forwardcheck=False, _unassigned=constraint.Unassigned):
        return sum([1 for variable in variables if variable in assignments and assignments[variable] in self.items]) >= self.count or len(assignments) < len(variables)

class SlugScheduler(object):
    def __init__(self, config={}, **changes):
        self.config = config
        self.config.update(changes)

    def schedule(self, courses, program):
        class Prerequisites(constraint.Constraint):
            def __init__(self, item, requirements):
                self.item = item
                self.problem = constraint.Problem()
                for requirement in requirements:
                    self.problem.addConstraint(requirement)

            def __call__(self, variables, domains, assignments, forwardcheck=False, _unassigned=constraint.Unassigned):
                if self.item in assignments.values():
                    self.problem._variables.clear()
                    for variable, value in assignments.iteritems():
                        if value == self.item:
                            break
                        self.problem.addVariable(variable, [value])
                    return self.problem.getSolution() is not None
                return True

        problem = constraint.Problem()
        problem.addConstraint(constraint.AllDifferentConstraint())
        for requirement in program.requirements:
            problem.addConstraint(requirement)
        for course in courses.values():
            if len(course.prerequisites) > 0:
                problem.addConstraint(Prerequisites(course.name, course.prerequisites))

        for n in range(len(courses) + 1):
            problem._variables.clear()
            problem.addVariables(range(n), courses.keys())
            solution = problem.getSolution()
            if solution:
                result = [None] * (max(solution.keys()) + 1)
                for n, course in solution.iteritems():
                    result[n] = courses[course]
                return result
        else:
            return []
