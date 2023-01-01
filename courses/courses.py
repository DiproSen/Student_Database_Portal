'''
Course Database Functions
'''
import csv
import os
import pandas as pd
from matplotlib import pyplot as plt

path_std = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'databases', 'Students.csv')
path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'databases', 'Courses.csv')
fields=['Course ID', 'Course Name', 'Marks Obtained']


def validate_input(ch):
    while(True):
        if ch not in ('1','2','3','4'):
            print('Please enter valid values 1/2/3/4 \n')
            ch=str(input('Please enter 1/2/3/4\n'))
        else:
            break

    return True


def create_course():
    '''
    Create Course Database
    '''
    if not os.path.exists(path):
        with open(path,'w', newline='', encoding='utf-8') as new_file2:
            csv_writer2=csv.writer(new_file2,delimiter=',')
            csv_writer2.writerow(fields)


def append_course():
    '''
    Append Course Details
    '''   
    while (True):
       
        course_id = str(input("enter course id \n"))
        course_name = str(input("enter course name \n"))
    
        marks = '' 
        dict={'Course ID': course_id,'Course Name':course_name,'Marks Obtained':marks}        

        with open(path,'a',newline='', encoding='utf-8') as new_file2:
            csv_writer2=csv.DictWriter(new_file2,fieldnames=fields,delimiter=',')
            csv_writer2.writerow(dict)
        break
    return True


def update_course(course_id, std_id, marks, oper):
    '''
    Update Course Details
    '''
    df = pd.read_csv(path)

    if len(df['Course ID']) == 0:
        print("Course Database is empty. Please enter course record.")
        return True

    for i in range(len(df['Course ID'])):
        if course_id == df['Course ID'][i]:
            marks_obtained = df['Marks Obtained'][i]
            course_name = df['Course Name'][i]

            if (oper != 'del') and not (pd.isna(df['Marks Obtained'][i])):                
                marks_obtained = str(marks_obtained) + '-' + str(std_id) + ':' + str(marks)
            else:
                marks_obtained = str(std_id) + ':' + str(marks)
            df.loc[i]=[course_id,course_name,marks_obtained]
            df.to_csv(path, index=False)                
            break

    return df


def view_perf(course_id):
    '''
    View performance in specific course
    '''
    ##course_id=str(input("Enter the course id choice"))
    df_course=pd.read_csv(path)

    print('StudentID:Marks')
    for i in range(len(df_course['Course ID'])):
        if course_id == df_course['Course ID'][i]:
            print(df_course['Marks Obtained'][i])
    return True


def course_stat():
    '''
    Histogram showing  no. of students  Vs grades
    '''             
    course_id = str(input("enter course id \n"))
    df = pd.read_csv(path)

    marks_obtained = ''

    for i in range(len(df['Course ID'])):
        if course_id == df['Course ID'][i]:
            marks_obtained = df['Marks Obtained'][i]

    grade = ['A','B','C','D','E','F']
    std_a = 0
    std_b = 0
    std_c = 0
    std_d = 0
    std_e = 0
    std_f = 0
    for i in marks_obtained.split('-'):

        if int(i.split(':')[1]) >= 90:
            std_a = std_a + 1 
        elif int(i.split(':')[1]) >= 80:
            std_b = std_b + 1
        elif int(i.split(':')[1]) >= 70:
            std_c = std_c + 1
        elif int(i.split(':')[1]) >= 60:
            std_d = std_d + 1
        elif int(i.split(':')[1]) >= 50:
            std_e = std_e + 1
        elif int(i.split(':')[1]) < 50:
            std_f = std_f + 1

    num_std = [std_a, std_b, std_c, std_d, std_e, std_f]    
    plt.bar(grade, num_std)
    plt.show()

    return True


def count(list1, l, r):
    return len(list(filter(lambda x: l <= x <= r, list1)))


def exit_course():
    '''
    Exit Course
    '''
    print("You have chosen to exit Courses Menu")

    return True


def course():
    '''
    Main function
    '''
    create_course()

    choice_str2 = '''
    ==================
    ## Courses Menu ##
    ==================
    1. Do you want to append course details?
    2. Do you want to view performance?
    3. Do you want to see statistics?
    4. Exit to main menu
    '''

    while(True):

        print(choice_str2)
        choice=str(input('Please enter 1/2/3/4 \n'))

        if validate_input(choice):
            if choice == '1':
                append_course()
            elif choice == '2':
                c_id = str(input("enter course id \n"))
                view_perf(c_id)
            elif choice == '3':
                course_stat()
            else:
                exit_course()
                return True

        print('Do you want to continue with course details? \n')
        cont=str(input('Please enter Y / N \n'))

        if cont not in ('Y', 'y'):  
            break

    return True   
