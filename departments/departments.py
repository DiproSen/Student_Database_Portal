'''
Department Database Functions
'''
import csv
import os
import pandas as pd
import ast


path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'databases', 'Departments.csv')
fields=['Department_ID','Department_Name','List of Batches']
bch=[]


def validate_input(ch):
    while(True):
        if ch not in ('1','2','3','4'):
            print('Please enter valid values 1/2/3/4 \n')
            ch=str(input('Please enter 1/2/3/4\n'))
        else:
            break

    return True


def create_dept():
    '''
    Create Department Database
    '''
    if not os.path.exists(path):
        with open(path,'w', newline='', encoding='utf-8') as new_file:
            csv_writer=csv.writer(new_file,delimiter=',')
            csv_writer.writerow(fields)

    return True

    
def append_dept():
    '''
    Append Department Details
    '''
    while (True):
        dept_id=str(input("enter department id "))      
        dept_name=str(input("enter department name "))
              
        lst_batches=[]

        dict={'Department_ID':dept_id,'Department_Name':dept_name,'List of Batches':lst_batches}
                
        with open(path,'a',newline='', encoding='utf-8') as new_file:
            csv_writer=csv.DictWriter(new_file,fieldnames=fields,delimiter=',')
            csv_writer.writerow(dict)    
        break            

    return True


def view_batch():
    '''
    View all Batches in specific dept
    '''
    dept_id=str(input("enter dept id choice\n"))
    df_dept=pd.read_csv(path)
    for i in range(len(df_dept['Department_ID'])):
        if dept_id in df_dept['Department_ID'][i]:
            print(ast.literal_eval(df_dept.loc[i]['List of Batches']))

    return True


def avg_batch():
    '''
    Average performance of batch in specific dept
    '''
    return True


def dept_stat():
    '''
    Line plot showing avg percentage Vs batch name
    '''
    return True


def exit_dept():
    '''
    Exit Department
    '''
    print("You have chosen to exit Department")

    return True


def update_dept_batch(dept_id, value, oper):
    '''
    Update Department Details
    '''

    df = pd.read_csv(path)

    if len(df['Department_ID']) == 0:
        print("Database is empty. Please enter record.")
        return True

    for i in range(len(df['Department_ID'])):
        if dept_id == df['Department_ID'][i]:
            lst_batches = ast.literal_eval(df.loc[i]['List of Batches'])
            dept_name = df['Department_Name'][i]
            if oper != 'del':                
                lst_batches.append(value)
            else:
                lst_batches.remove(value)
            df.loc[i]=[dept_id,dept_name,lst_batches]
            df.to_csv(path, index=False)                
            break

    return True


def department():
    '''
    Main function
    '''

    create_dept()

    choice_str = '''
    ======================
    ## Departments Menu ##
    ======================
    1. Do you want to append department details?
    2. Do you want to view all batches in department?
    3. Do you want to view average performance of all batches in department?
    4. Exit to main menu
    '''

    while(True):

        print(choice_str)
        choice=str(input('Please enter 1/2/3/4 \n'))

        if validate_input(choice):
            if choice == '1':
                append_dept()
            elif choice == '2':
               view_batch()
            elif choice == '3':
                dept_stat()
            else:
                exit_dept()
                return True

        print('Do you want to continue with department details? \n')
        cont=str(input('Please enter Y / N \n'))

        if cont not in ('Y', 'y'):  
            break

    return True