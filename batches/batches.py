'''
Batch Database Functions
'''
import csv
import os
import pandas as pd
import ast
from departments.departments import update_dept_batch

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'databases', 'Batches.csv')
path_std = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'databases', 'Students.csv')
path_dept = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'databases', 'Departments.csv')
fields=['BatchID','Batch Name','Department_ID','List of Courses','List of Students']


def create_batch():
    '''
    Create Batch Database
    '''
    if not os.path.exists(path):
        with open(path,'w', newline='', encoding='utf-8') as new_file:
            csv_writer=csv.writer(new_file,delimiter=',')
            csv_writer.writerow(fields)

    return True

    
def append_batch():
    '''
    Append Batch Details
    '''
    while (True):
        batch_id=str(input("enter batch id \n")) 
        batch_name=str(input("enter batch name \n"))     
        dept_id=str(input("enter dept id \n"))    
        l_course=[]
        
        while(True):
            ch=str(input("Do you want to add courses? Please enter Y or N\n"))
            if ch=='y' or ch=='Y':
                bch=str(input("Enter course name \n"))
                l_course.append(bch)
            else:
                break

        df = pd.read_csv(path)
        if len(df['List of Students']) != 0:
            l_std = df['List of Students']
        else:
            l_std = []
         
        # while(True):
        #     ch=str(input("Do you want to add students? "))
        #     if ch=='y' or ch=='Y':

        #         bch=str(input("Enter students "))
        #         l_std.append(bch)
        #     else:
        #         break

        dict={'BatchID':batch_id,'Batch Name': batch_name,'Department_ID':dept_id,\
            'List of Courses':l_course,'List of Students':l_std}
                
        with open(path,'a',newline='', encoding='utf-8') as new_file:
            csv_writer=csv.DictWriter(new_file,fieldnames=fields,delimiter=',')
            csv_writer.writerow(dict) 
            update_dept_batch(dept_id, batch_id, 'add')
        break            

    return True


def update_batch_std(batch_id, value, oper):
    '''
    Update Batch Details from Students
    '''

    df = pd.read_csv(path)

    if len(df['BatchID']) == 0:
        print("Database is empty. Please enter record.")
        return True

    for i in range(len(df['BatchID'])):
        if batch_id == df['BatchID'][i]:
            l_std = ast.literal_eval(df.loc[i]['List of Students'])
            batch_name = df['Batch Name'][i]
            dept_id = df['Department_ID'][i]
            l_course = ast.literal_eval(df.loc[i]['List of Courses'])
            if oper != 'del':                
                l_std.append(value)
            else:
                l_std.remove(value)
            df.loc[i]=[batch_id,batch_name,dept_id,l_course,l_std]
            df.to_csv(path, index=False)                
            break

    return True


def view_std():
    '''
    View all Students in specific batch
    '''
    batch_id=str(input("enter batch id choice\n"))
    df_batch=pd.read_csv(path)
    for i in range(len(df_batch['BatchID'])):
        if batch_id == df_batch['BatchID'][i]:
            print(ast.literal_eval(df_batch.loc[i]['List of Students']))

    return True


def view_course():
    '''
    View all courses in specific batch
    '''
    batch_id=str(input("enter batch id choice\n"))
    df_batch=pd.read_csv(path)
    for i in range(len(df_batch['BatchID'])):
        if batch_id == df_batch['BatchID'][i]:
            print(ast.literal_eval(df_batch.loc[i]['List of Courses']))

    return True


def view_perf_std_batch():
    '''
    View complete performance of all students in a batch
    '''
    return True


def pie_chart():
    '''
    View Pie Chart of Percentage of all students?
    '''

    return True


def exit_batch():
    '''
    Exit Batch Details
    '''
    print("You have chosen to exit batch details")

    return True


def validate_input(ch):
    while(True):
        if ch not in ('1','2','3','4','5','6'):
            print('Please enter valid values 1/2/3/4/5/6 \n')
            ch=str(input('Please enter 1/2/3/4/5/6\n'))
        else:
            break

    return True


def batch():
    '''
    Main function
    '''
    df_dept = pd.read_csv(path_dept)
    if len(df_dept['Department_ID']) == 0:
        print("Department Database is empty. Please enter department record.")
        return True

    create_batch()

    choice_str = '''
    ==================
    ## Batches Menu ##
    ==================
    1. Do you want to append specific batch?
    2. Do you want to View all Students in specific batch?
    3. Do you want to View all courses in specific batch?
    4. Do you want to View complete performance of all students in a batch?
    5. Do you want to View Pie Chart of Percentage of all students?
    6. Exit to main menu
    '''

    while(True):

        print(choice_str)
        choice=str(input('Please enter 1/2/3/4/5/6 \n'))

        if validate_input(choice):
            if choice == '1':
                append_batch()
            elif choice == '2':
                view_std()
            elif choice == '3':
                view_course()
            elif choice == '4':
                view_perf_std_batch()
            elif choice == '5':
                pie_chart()
            else:
                exit_batch()
                return True

        print('Do you want to continue with batch details? \n')
        cont=str(input('Please enter Y / N \n'))

        if cont not in ('Y', 'y'):  
            break

    return True
