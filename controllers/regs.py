def addCourse():
   form = SQLFORM(db.courses)
   if form.process().accepted:
       response.flash = 'form accepted'
   elif form.errors:
       response.flash = 'form has errors'
   else:
       response.flash = 'please fill out the form'
   return dict(form=form)


def courses():
   grid =SQLFORM.grid(db.courses,csv=False)
   return dict(grid=grid)

def coursesschedules():
   grid=SQLFORM.grid(db.courses.schedule_id==db.courseschedule.schedule_id,
   fields=[db.courses.course_name,db.courses.course_code,db.courses.instructor,db.courses.prerequisites,db.courses.capacity,
   db.courseschedule.days,db.courseschedule.startTime,db.courseschedule.endTime,db.courseschedule.roomNo],
   csv=False,editable=False,deletable=False,details=False,create=False,
   selectable=lambda ids:redirect(URL('regs','Studentschedule',vars=dict(id=ids))))
   return dict(grid=grid)

def StudentSchedule():
   grid=SQLFORM.grid((db.courses.course_code == db.studentsregs.course_code) & (db.students.student_id==db.studentsregs.student_id),
   fields=[db.students.student_id,db.courses.course_code,db.courses.course_name,db.courses.instructor,db.courses.prerequisites,db.courses.capacity,
   db.courseschedule.days,db.courseschedule.startTime,db.courseschedule.endTime,db.courseschedule.roomNo],
   csv=False,editable=False,deletable=False,details=False,create=False)
   return dict(grid=grid)