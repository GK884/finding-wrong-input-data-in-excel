import pandas as pd
import re


# pd.set_option('display.max_columns', None)
df = pd.read_csv('pras.csv')
# print(df)

name_list = []
for index, row in df.iterrows():
    contains_digit = False
    wrong_email = False

    #     print(row['CANDIDATE NAME'])
    #For Candidate Name
    for character in row['CANDIDATE NAME']:
        if character.isdigit():
            contains_digit = True
            # print(row[['CANDIDATE NAME','EMAIL','ROLL NUMBER','CONTACT NUMBER','BRANCH']])
            name_list.append(
                {'CANDIDATE NAME': row['CANDIDATE NAME'], 'EMAIL': row['EMAIL'], 'ROLL NUMBER': row['ROLL NUMBER'],
                 'CONTACT NUMBER': row['CONTACT NUMBER'], 'BRANCH': row['BRANCH'], 'Error': 'wrong Name'})
            break


    # For Candidate Email
    if contains_digit == False:
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, str(row['EMAIL']))):
            pass
        else:
            wrong_email = True
            name_list.append(
                {'CANDIDATE NAME': row['CANDIDATE NAME'], 'EMAIL': row['EMAIL'], 'ROLL NUMBER': row['ROLL NUMBER'],
                 'CONTACT NUMBER': row['CONTACT NUMBER'], 'BRANCH': row['BRANCH'], 'Error': 'wrong Email'})


    # For Candidate Contact Number
    if wrong_email == False or contains_digit == False:
        for character in str(row['CONTACT NUMBER']):
            if character.isalpha():
                contains_digit = True
                # print(row[['CANDIDATE NAME','EMAIL','ROLL NUMBER','CONTACT NUMBER','BRANCH']])
                name_list.append(
                    {'CANDIDATE NAME': row['CANDIDATE NAME'], 'EMAIL': row['EMAIL'], 'ROLL NUMBER': row['ROLL NUMBER'],
                     'CONTACT NUMBER': row['CONTACT NUMBER'], 'BRANCH': row['BRANCH'], 'Error': 'wrong Contact NO.'})
                break

#For normal printing 

# print(len(name_list))
# for i in range(len(name_list)):
#     print('CANDIDATE NAME : ', name_list[i]['CANDIDATE NAME'])
#     print('ROLL NUMBER : ', name_list[i]['ROLL NUMBER'])
#     print('CONTACT NUMBER : ', name_list[i]['CONTACT NUMBER'])
#     print('BRANCH : ', name_list[i]['BRANCH'])
#     print('EMAIL : ', name_list[i]['EMAIL'])
#     print('__________________________________')


#Creating a new DataFrame and Printing

new_df = pd.DataFrame(name_list)
print('Change the values of faulted data')
print(new_df)