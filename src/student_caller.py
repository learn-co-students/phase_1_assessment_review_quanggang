import numpy as np

def one_random_student(student_list, question = None):
    """
    :param student_list: a list of students in any given class
    :return: a student to be called on
    """

    student =  np.random.choice(student_list, 1)[0]
    print(student)
   
    if question is not None:
        print(question)


def three_random_students(student_list, question = None):
    """
    :param student_list: a list of students in any given class
    :return: a student to be called on
    """

    students = np.random.choice(student_list, 3, replace=False)
    print(students)
    return students
   
    if question != None:
        print(question)
