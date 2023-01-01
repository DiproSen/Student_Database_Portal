'''
Student Database Functions
'''
import csv
import os
import pandas as pd
from batches.batches import update_batch_std

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'databases', 'Students.csv')
path_batch = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'databases', 'Batches.csv')
fields=['StudentID','Name','Class Roll No.','BatchID']


def create_student():
    '''
    Create Student Database
    '''
    if not os.path.exists(path):
        with open(path,'w', newline='', encoding='utf-8') as new_file:
            csv_writer=csv.writer(new_file,delimiter=',')
            csv_writer.writerow(fields)

    return True

    
def append_student():
    '''
    Append Student Details
    '''
    while True:

        std_id=str(input("enter student id "))      
        std_name=str(input("enter name "))
        std_roll_num=str(input("enter roll "))
        std_batch=str(input("enter batch id "))            

        dict={'StudentID':std_id,'Name':std_name,'Class Roll No.':std_roll_num,'BatchID':std_batch}
                
        with open(path,'a',newline='', encoding='utf-8') as new_file:
            csv_writer=csv.DictWriter(new_file,fieldnames=fields,delimiter=',')
            csv_writer.writerow(dict)
            update_batch_std(std_batch, std_id, 'add')    
        break         

    return True


def update_student():
    '''
    Update Student Details
    '''
    up = str(input("Enter StudentID of whom details are to be updated \n"))
    df = pd.read_csv(path)

    if len(df['StudentID']) == 0:
        print("Student Database is empty. Please enter student record.")
        return True

    std_name=str(input("enter name "))
    std_roll_num=int(input("enter roll "))
    std_batch=str(input("enter batch id "))

    
    for i in range(len(df['StudentID'])):
        if up == df['StudentID'][i]:
            df.loc[i]=[up,std_name,std_roll_num,std_batch]
            df.to_csv(path, index=False)
            update_batch_std(std_batch, up, 'add')
            break

    return True


def remove_student():
    '''
    Remove Student Details
    '''
    re=str(input("Enter StudentID of whom details are to be removed \n"))
    
    df = pd.read_csv(path)
    if len(df['StudentID']) == 0:
        print("Student Database is empty. Please enter student record.")
        return True

    df_s = df[:]

    df_s.set_index('StudentID', inplace=True)

    df_s = df_s.drop(re)
    df_s.to_csv(path)

    std_batch = df[re]['BatchID']
    update_batch_std(std_batch, re, 'del')

    return True


def exit_student():
    '''
    Exit Student
    '''
    print("You have chosen to exit student details")

    return True


def validate_input(ch):
    while(True):
        if ch not in ('1','2','3','4'):
            print('Please enter valid values 1/2/3/4 \n')
            ch=str(input('Please enter 1/2/3/4\n'))
        else:
            break

    return True


def student():
    '''
    Student Main function
    '''
    df_batch = pd.read_csv(path_batch)
    if len(df_batch['BatchID']) == 0:
        print("Batch Database is empty. Please enter batch record.")
        return True

    create_student()

    choice_str = '''
    ===================
    ## Students Menu ##
    ===================
    1. Do you want to append student details?
    2. Do you want to update student details?
    3. Do you want to remove student details?
    4. Exit to main menu
    '''

    while(True):

        print(choice_str)
        choice=str(input('Please enter 1/2/3/4 \n'))

        if validate_input(choice):
            if choice == '1':
                append_student()
            elif choice == '2':
                update_student()
            elif choice == '3':
                remove_student()
            else:
                exit_student()
                return True

        print('Do you want to continue with student details? \n')
        cont=str(input('Please enter Y / N \n'))

        if cont not in ('Y', 'y'):  
            break

    return True
