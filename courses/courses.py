'''
Course Database Functions
'''
import csv
import os
import pandas as pd
import ast

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
       
        course_id = str(input("enter course id "))
        course_name = str(input("enter course name "))
    
        marks = {} 
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
            marks_obtained = ast.literal_eval(df.loc[i]['Marks Obtained'])
            course_name = df['Course Name'][i]

            if oper != 'del':                
                marks_obtained[std_id] = marks
            else:
                marks_obtained.pop[std_id]
            df.loc[i]=[course_id,course_name,marks_obtained]
            df.to_csv(path, index=False)                
            break

    return True


def view_perf():
    '''
    View performance in specific course
    '''
    course_id=str(input("Enter the course id choice"))
    df_std=pd.read_csv(path_std)
    df_course=pd.read_csv(path)

    print('Class Roll No.','Name','Marks Obtained')
    for i in range(len(df_course['Course ID'])):
        if course_id == df_course['Course ID'][i]:
            print(df_std['Class Roll No.'],df_std['Name'],df_course['Marks Obtained'])
    return True


def course_stat():
    '''
    Histogram showing  no. of students  Vs grades
    '''             
    



    return True


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
                view_perf()
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
