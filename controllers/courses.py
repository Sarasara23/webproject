def search():
    query = request.vars.query
    if not query:
        courses =[]
    else:
        courses = db(db.courses.course_name.contains(query) or db.courses.course_code.contains(query) or db.courses.instructor_name.contains(query)).select
    return dict(courses=courses ,query=query)

def student():
    query=request.vars.query
    if not query:
        students=[]
    else:
        students=db(db.students.first_name.contains(query) or db.students.student_id.contains(query))
    return dict(student=student,query=query)

def details():
    course_code=request.args(0)
    courses=(db.courses.ALL)
    return dict(courses=courses)


def courses():
    grid =db(db.courses)
    return dict(grid=grid)