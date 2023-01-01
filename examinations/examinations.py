'''
Examination Functions
'''
import pandas as pd
from courses.courses import update_course

# def view_perf():
#     '''
#     View performance of all students in each course
#     '''

#     ch=str(input("Enter the course of your choice "))

    
def append_exam_marks():
    '''
    Append Exam Details
    '''             
    course_id=str(input("enter course id "))
    std_id=str(input("enter student id "))
    marks=int(input("enter marks "))

    update_course(course_id, std_id, str(marks), 'add')      

    return True


def validate_input(ch):
    while(True):
        if ch not in ('1','2','3','4'):
            print('Please enter valid values 1/2/3/4 \n')
            ch=str(input('Please enter 1/2/3/4\n'))
        else:
            break

    return True


def examination():
    '''
    Main function
    '''

    ##create_exam_marks()

    choice_str = '''
    ======================
    ## Examination Menu ##
    ======================
    1. Do you want to append examination details?
    2. Exit to main menu
    '''

    while(True):

        print(choice_str)
        choice=str(input('Please enter 1/2 \n'))

        if validate_input(choice):
            if choice in ('1'):
                append_exam_marks()
            else:
                break

        print('Do you want to continue with examination details? \n')
        cont=str(input('Please enter Y / N \n'))

        if cont not in ('Y', 'y'):  
            break

    return True
