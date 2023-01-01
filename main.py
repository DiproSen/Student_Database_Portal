'''
User Input Functions
'''
import traceback
from batches.batches import batch, create_batch
from courses.courses import course, create_course
from departments.departments import department, create_dept
from students.students import student, create_student
from examinations.examinations import examination

def validate_input(ch):
    while(True):
        if ch not in ('1','2','3','4','5','6'):
            print('Please enter valid values 1/2/3/4/5/6 \n')
            ch=str(input('Please enter 1/2/3/4/5/6\n'))
        else:
            break

    return True


def main():
    '''
    Main Function
    '''
    create_batch()
    create_course()
    create_dept()
    create_student()
    
    choice_str = '''
    ===============
    ## Main Menu ##
    ===============
    1. Do you want to work with students?
    2. Do you want to work with batches?
    3. Do you want to work with courses?
    4. Do you want to work with departments?
    5. Do you want to work with examination?
    6. Exit
    '''

    while(True):

        print(choice_str)
        choice=str(input('Please enter 1/2/3/4/5/6 \n'))

        if validate_input(choice):
            if choice == '1':
                student()
            elif choice == '2':
                batch()
            elif choice == '3':
                course()
            elif choice == '4':
                department()
            elif choice == '5':
                examination()
            else:
                break

        print('Do you want to continue with Main Menu? \n')
        cont=str(input('Please enter Y / N \n'))

        if cont not in ('Y', 'y'):  
            break

    return True


if __name__=="__main__":
    try:
        main()
    except Exception:
        print(traceback.format_exc())
        main()
