# prereqs format: python boolean expression with course nbrs
#   Example: ('CMPS 101' or 'MATH 100') and 'CMPS 102'
# offerings format: json dumps of list of pairs

db.define_table('course',
        Field('name', 'string'),
        Field('title', 'string'),
        Field('units', 'integer'),
        Field('prerequisites', 'json'),
        Field('offerings', 'json')
        )

db.define_table('program',
        Field('name', 'string'),
        Field('requirements', 'json')
        )
