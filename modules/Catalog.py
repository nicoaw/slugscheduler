import json
import re
from gluon import *

# Minimum year
BASE_YEAR = 2012

# Quarter enumerations
FALL = 'F'
WINTER = 'W'
SPRING = 'S'
SUMMER = 'U'

# Get course nbrs available
def get_courses():
    db = current.db
    courses = db(db.course).select()
    return [course.nbr for course in courses]

# Get course info
# Example:
# course = get_course('CMPS 101')
# print course.nbr, course.title, course.units, course.prereqs, course.offerings
def get_course(nbr):
    db = current.db
    return db(db.course.nbr == nbr).select().first()

# Is course offered at certain year, quarter
def is_offered(course, quarter):
    return quarter in json.loads(course.offerings)

# Are the prereqs meet for course
def is_satisfied(transcript, requisites):
    def repl(m):
        return 'transcript.has(' + m.group(0) + ')'

    expr = re.sub('("[^"]+")', repl, requisites)
    return eval(expr)
