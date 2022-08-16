from app.model import College, Course, Manager, Program, Student, Term


def test_model():
    COLLEGE_NAME = 'Lambton College'
    college = College(COLLEGE_NAME)
    assert college.name == COLLEGE_NAME
    assert len(college.programs) == 0
    assert len(college.managers) == 0
    assert len(college.students) == 0

    # adds some programs
    PROGRAM_NAME = 'Artificial Intelligence and Machine Learning'
    aimt = Program(PROGRAM_NAME, 2)
    assert aimt.name == PROGRAM_NAME
    assert aimt.college == None
    assert len(aimt.terms) == 0

    college.add_program(aimt)
    assert len(college.programs) == 1
    assert aimt.college == college

    # adds some terms to a program
    TERM_NAME = 'First Term'
    aimt_1 = Term(TERM_NAME, 1)
    assert aimt_1.name == TERM_NAME
    assert aimt_1.program == None
    assert len(aimt_1.sections) == 0

    aimt.add_term(aimt_1)
    assert len(aimt.terms) == 1
    assert aimt_1.program == aimt

    # adds some courses to a term
    COURSE_NAME = 'AML-1214: Python Programming'
    course = Course(COURSE_NAME)
    assert course.name == COURSE_NAME
    assert course.term == None

    aimt_1.add_course(course)
    assert len(aimt_1.courses) == 1
    assert course.term == aimt_1

    # adds a default manager
    MANAGER_USER = "admin"
    MANAGER_NAME = "System Administrator"
    manager = Manager(MANAGER_USER, MANAGER_NAME)
    assert manager.username == MANAGER_USER
    assert manager.fullname == MANAGER_NAME
    assert manager.college == None

    college.add_manager(manager)
    assert len(college.managers) == 1
    assert manager.college == college

    # adds a default student
    STUDENT_ID = '000'
    STUDENT_NAME = 'Student Zero'
    student_0 = Student(STUDENT_ID, STUDENT_NAME)
    assert student_0.student_id == STUDENT_ID
    assert student_0.full_name == STUDENT_NAME
    assert student_0.college == None

    college.add_student(student_0)
    assert len(college.students) == 1
    assert student_0.college == college
