import datetime


db.define_table('courses',
	Field('course_code', 'string', required=True, notnull=True),
	Field('course_name', 'string'),
	Field('description', 'string'),
	Field('prerequisites', 'string', 'reference courses',requires=IS_IN_DB(db, 'courses.course_code', '%(course_name)s')),
	Field('instructor_name', 'string'),
	Field('capacity', 'integer'),
	Field('schedule_id', 'integer','reference courseschedule',requires=IS_IN_DB(db, 'courseschedule.schedule_id', '%(days)s- %(startTime)s - %(endTime)s')),
	primarykey=['course_code'])


db.define_table('students',
	Field('student_id', 'integer'),
	Field('first_name', 'string'),
	Field('last_name', 'string'),
	Field('email', 'string'),
	Field('password', 'string'),
	Field('registration_key','string'),
	Field('reset_password_key','string'),
	Field('registration_id','string'),
	primarykey=['student_id'])

db.define_table('studentsreg',
	Field('registration_id', 'integer', required=True, notnull=True),
	Field('student_id','integer'),
	Field('course_code','string'),
	primarykey=['student_id'])



db.define_table('room',
	Field('code', 'string', required=True, notnull=True),
	primarykey=['code'])


db.define_table('courseschedule',
	Field('schedule_id', 'integer',required=True, notnull=True),
	Field('days', 'string'),
	Field('startTime', 'time', default=datetime.time(0,0)),
	Field('endTime', 'time', default=datetime.time(0,0)),
	Field('roomNo', 'string', 'reference room', requires=IS_IN_DB(db, 'room.code', '%(code)s')),
	primarykey=['schedule_id']
	) 