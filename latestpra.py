import pandas as pd
import csv
import re
from csv import writer


#To watch the file data
def watch_data():
    try:
        file_name = input('Enter name of csv file: ')
        file_name = file_name +'.csv'
        df = pd.read_csv(file_name)
        print(df)
    except:
        print('file not present')

#to check the file format and list out the incorrect data
def watch_format():
    col_names = ['candidate_name', 'roll_number', 'contact_number', 'branch', 'email']    
    try:
        file_name = input('Enter name of csv file: ')
        file_name = file_name +'.csv'
#         print(file_name)
        df = pd.read_csv(file_name)
        if (df.columns[0] == 'candidate_name' and df.columns[1] == 'roll_number' and df.columns[2] == 'contact_number' and df.columns[3]== 'branch'  and df.columns[4]== 'email'):
#             print('ok')
            name_list = []
            for index, row in df.iterrows():
                contains_digit = False
                contains_digit1 = False
                wrong_email = False
                wrong_roll = False

                try:
                    if int(row['roll_number']) >0 and int(row['roll_number']) < 100:
                        pass
                    else:
                        name_list.append(
                        {'candidate_name': row['candidate_name'], 'email': row['email'], 'roll_number': row['roll_number'],
                         'contact_number': row['contact_number'], 'branch': row['branch'], 'Error': 'wrong roll no.'})
                        contains_digit1 = True
                except:
                    name_list.append(
                        {'candidate_name': row['candidate_name'], 'email': row['email'], 'roll_number': row['roll_number'],
                         'contact_number': row['contact_number'], 'branch': row['branch'], 'Error': 'wrong roll no.'})
                    contains_digit1 = False

                #     print(row['CANDIDATE NAME'])
                #For Candidate Name
                for character in row['candidate_name']:
                    if character.isdigit():
                        contains_digit = True
                        # print(row[['CANDIDATE NAME','EMAIL','ROLL NUMBER','CONTACT NUMBER','BRANCH']])
                        name_list.append(
                    {'candidate_name': row['candidate_name'], 'email': row['email'], 'roll_number': row['roll_number'],
                     'contact_number': row['contact_number'], 'branch': row['branch'], 'Error': 'wrong name'})
                        break


                # For Candidate Email
                if contains_digit == False:
                    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                    if (re.search(regex, str(row['email']))):
                        pass
                    else:
                        wrong_email = True
                        name_list.append(
                    {'candidate_name': row['candidate_name'], 'email': row['email'], 'roll_number': row['roll_number'],
                     'contact_number': row['contact_number'], 'branch': row['branch'], 'Error': 'wrong email'})


                # For Candidate Contact Number
                if wrong_email == False or contains_digit == False:
                    for character in str(row['contact_number']):
                        if character.isalpha():
                            contains_digit1 = True
                            # print(row[['CANDIDATE NAME','EMAIL','ROLL NUMBER','CONTACT NUMBER','BRANCH']])
                            name_list.append(
                        {'candidate_name': row['candidate_name'], 'email': row['email'], 'roll_number': row['roll_number'],
                         'contact_number': row['contact_number'], 'branch': row['branch'], 'Error': 'wrong contact no.'})
                            break





            new_df = pd.DataFrame(name_list)
            print('Change the values of faulted data')
            print(new_df)
        else:
            print('file not in order')
    except:
        print('file not present')    


#to add a new data
def add_row():
    try:
        file_name = input('Enter name of csv file: ')
        file_name = file_name +'.csv'
        df = pd.read_csv(file_name)
#         print(df)
        data_list = []
        col = df.columns
#         print(df.index)
        for c in col:
            col_name = input('Enter '+c+': ')
            data_list.append(col_name)
            


        with open(file_name, 'a', newline='') as f_object:

            writer_object = writer(f_object)

            writer_object.writerow(data_list)

            f_object.close()
            df = pd.read_csv(file_name)
#             print(df)
            print('Data added successfully')
            print('\n')
            
        
    except:
        print('file not present')



# to delete given data
def del_row():
    try:
        flag = 0
        ctn = -1
        file_name = input('Enter name of csv file: ')
        file_name = file_name +'.csv'
        df = pd.read_csv(file_name)
        col = df.columns
        data_list=[]
        for c in col:
            col_name = input('Enter '+c+': ')
            data_list.append(col_name)
        
        for index, row in df.iterrows():
            ctn+=1
            if row['candidate_name'] == data_list[0] and row['roll_number'] == data_list[1] and row['contact_number']== data_list[2] and  row['branch'] == data_list[3] and  row['email'] == data_list[4] :
                flag = 1
                break
        
        if flag == 1:
            print(ctn)
            df = df.drop(labels=ctn, axis=0)
            df.to_csv(file_name, index=False)

                
        else:
            print('Given data not present')
            
#         print(df)
        print('Data deleted successfully')
        print('\n')        
            
    except:
        print('file not present')


# __main__

flag = 'y'
while flag != 'q':
    
    choice = input('''Enter your choice
                    1. watch file data
                    2. check file format
                    3. enter new data
                    4. delete data
                    5. quit
                    ''')

    if choice == '1':
        watch_data()
    elif choice == '2':
        watch_format()
    elif choice == '3':
        add_row()
    elif choice == '4':
        del_row()
    elif choice == '5':
        flag = 'q'
    else:
        print('Enter correct option')

