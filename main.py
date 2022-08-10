from app.use_cases.Main import Main as MainUseCase
from app.model import College, Course, Manager, Program, Student, Term


def create_populated_college():
    college = College("Lambton College")

    # adds some programs
    aimt = Program("Artificial Intelligence and Machine Learning", 2)
    ahcl = Program("Advanced Health Care Leadership", 2)
    college.add_program(aimt)
    college.add_program(ahcl)

    # adds some terms to a program
    aimt_1 = Term("First Term", 1)
    aimt_2 = Term("Second Term", 2)
    aimt_3 = Term("Third Term", 3)
    aimt_4 = Term("Co-op Term", 4)
    aimt.add_term(aimt_2)
    aimt.add_term(aimt_1)
    aimt.add_term(aimt_3)
    aimt.add_term(aimt_4)

    # adds some courses to a term
    aimt_1.add_course(Course("AML-1114: Data Science and Machine Learning"))
    aimt_1.add_course(Course("AML-1214: Python Programming"))
    aimt_1.add_course(Course("CBD-2214: Big Data Fundamentals"))
    aimt_1.add_course(Course("AML-1301: Careers in AI and ML"))
    aimt_1.add_course(Course("COM-3013: Professional Communications"))

    # adds a default manager
    college.add_manager(Manager("admin", "System Administrator"))

    # adds a default student
    student_0 = Student("000", "Student Zero")
    college.add_student(student_0)

    return college


def main():
    use_case = MainUseCase(create_populated_college())
    use_case.execute()


if __name__ == "__main__":
    main()
