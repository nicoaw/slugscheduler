from catalog import *
from slugscheduler import *
from gluon import current

def main():
    db = current.db
    db.course.truncate()
    db.program.truncate()

    update_course(
            name='CMPS101',
            title='Abstract Data Types',
            units=5,
            prerequisites=[],
            offerings=[]
            )
    
    update_course(
            name='CMPS102',
            title='Analysis of Algorithms',
            units=5,
            prerequisites=[Choice(['CMPS101'])],
            offerings=[]
            )

    update_course(
            name='CMPS104A',
            title='Compiler Design',
            units=5,
            prerequisites=[Choice(['CMPS101'])],
            offerings=[]
            )
    
    update_course(
            name='CMPS111',
            title='Operating Systems',
            units=5,
            prerequisites=[Choice(['CMPS101'])],
            offerings=[]
            )
    
    update_course(
            name='CMPS112',
            title='Comparative Languages',
            units=5,
            prerequisites=[Choice(['CMPS101'])],
            offerings=[]
            )

    update_course(
            name='CMPS130',
            title='Computational Models',
            units=5,
            prerequisites=[Choice(['CMPS101'])],
            offerings=[]
            )

    update_course(
            name='CMPS115',
            title='Introduction to Software Engineering',
            units=5,
            prerequisites=[Choice(['CMPS101'])],
            offerings=[]
            )

    update_course(
            name='CMPS132',
            title='Computability and Computational Complexity',
            units=5,
            prerequisites=[Choice(['CMPS130'])],
            offerings=[]
            )

    update_course(
            name='CMPS160',
            title='Introduction to Computer Graphics',
            units=5,
            prerequisites=[Choice(['CMPS101'])],
            offerings=[]
            )

    update_course(
            name='CMPS161',
            title='Introduction to Data Visualization',
            units=5,
            prerequisites=[Choice(['CMPS160'])],
            offerings=[]
            )

    update_course(
            name='CMPS183',
            title='Web Applications',
            units=5,
            prerequisites=[],
            offerings=[]
            )

    update_program(
            name='CMPS',
            requirements=[
                Choice(['CMPS101']),
                Choice(['CMPS102']),
                Choice(['CMPS104A']),
                Choice(['CMPS111']),
                Choice(['CMPS112']),
                Choice(['CMPS130']),
                Choice(['CMPS115', 'CMPS132']), # DC
                Choice(['CMPS161', 'CMPS183']), # Capstone
                Choice(['CMPS115', 'CMPS160', 'CMPS183'], 2), # Electives
                ]
            )

main()
