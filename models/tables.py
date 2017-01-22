# prereqs format: python boolean expression with course nbrs
#   Example: ('CMPS 101' or 'MATH 100') and 'CMPS 102'
# offerings format: json dumps of list of pairs

db.define_table('course',
        Field('nbr', 'string'),
        Field('title', 'string'),
        Field('units', 'integer'),
        Field('prereqs', 'text'),
        Field('offerings', 'json')
        )
