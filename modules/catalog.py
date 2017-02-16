from gluon import current
from gluon.storage import Storage
from slugscheduler import *
import json
import util

def update_course(course={}, **kwargs):
    db = current.db
    if 'prerequisites' in kwargs:
        kwargs['prerequisites'] = json.dumps(kwargs['prerequisites'], default=util.object_encoder)
    if 'offerings' in kwargs:
        kwargs['offerings'] = json.dumps(kwargs['offerings'], default=util.object_encoder)
    course.update(**kwargs)
    db.course.update_or_insert(**course)

def update_program(program={}, **kwargs):
    db = current.db
    if 'requirements' in kwargs:
        kwargs['requirements'] = json.dumps(kwargs['requirements'], default=util.object_encoder)
    program.update(**kwargs)
    db.program.update_or_insert(**program)

def get_courses():
    db = current.db
    courses = db(db.course).select()
    object_decoder = lambda obj: util.object_decoder(obj, globals())
    courses = {
            course.name:
            Storage(
                name=course.name,
                title=course.title,
                units=course.units,
                prerequisites=json.loads(course.prerequisites, object_hook=object_decoder),
                offerings=json.loads(course.offerings, object_hook=object_decoder)
                )
            for course in courses
            }
    return courses

def get_programs():
    db = current.db
    programs = db(db.program).select()
    programs = {
            program.name:
            Storage(
                name=program.name,
                requirements=json.loads(program.requirements, object_hook=lambda obj: util.object_decoder(obj, globals()))
                )
            for program in programs
            }
    return programs
