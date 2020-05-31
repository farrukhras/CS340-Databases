from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
from examples import custom_style_2
from prettytable import PrettyTable
from tabulate import tabulate

import mysql.connector
from mysql.connector import Error

def connect_db_admin():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='airline_system',
                                            user='root',
                                            password='1234')

        sql_select_Query = "SELECT * FROM admins"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        return records

    except Error as e:
        print("Error reading data from MySQL table", e)
    
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def connect_db_receptionist():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='airline_system',
                                            user='root',
                                            password='1234')

        sql_select_Query = "SELECT * FROM receptionist"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        return records

    except Error as e:
        print("Error reading data from MySQL table", e)

    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def connect_db_flight():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='airline_system',
                                            user='root',
                                            password='1234')

        sql_select_Query = "SELECT * FROM flight"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        return records

    except Error as e:
        print("Error reading data from MySQL table", e)
    
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def connect_db_flight1(flightID): #TO GENERATE TICKET
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='airline_system',
                                            user='root',
                                            password='1234')

        sql_select_Query = 'SELECT * FROM flight WHERE flight_id = "%s"'
        val = (flightID)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query%val)
        records = cursor.fetchall()
        return records

    except Error as e:
        print("Error reading data from MySQL table", e)
    
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def connect_db_passenger():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='airline_system',
                                            user='root',
                                            password='1234')

        sql_select_Query = "SELECT * FROM passenger"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall() 
        return records

    except Error as e:
        print("Error reading data from MySQL table", e)
    
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def connect_db_passenger1(pass_num): #TO GENERATE TICKET
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='airline_system',
                                            user='root',
                                            password='1234')

        sql_select_Query = "SELECT * FROM passenger WHERE Passport_num = %s"
        val = (pass_num)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query%val)
        records = cursor.fetchall() 
        return records

    except Error as e:
        print("Error reading data from MySQL table", e)
    
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def connect_db_ticket():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='airline_system',
                                            user='root',
                                            password='1234')

        sql_select_Query = "SELECT * FROM ticket"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall() 
        return records

    except Error as e:
        print("Error reading data from MySQL table", e)
    
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def connect_db_ticket1(pass_num, fli_ID): # FOR CANCELLING A TICKET
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='airline_system',
                                            user='root',
                                            password='1234')

        sql_select_Query = 'DELETE from ticket WHERE Passport_num = "%s" AND flight_id = "%s"'
        val = (pass_num, fli_ID)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query%val)
        connection.commit()

    except Error as e:
        print("Error reading data from MySQL table", e)
    
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def connect_db_flight_new(query, val): # FOR ADDING NEW FLIGHT RECORD
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='airline_system',
                                            user='root',
                                            password='1234')

        cursor = connection.cursor()
        cursor.execute(query, val)
        connection.commit()

    except Error as e:
        print("Error reading data from MySQL table", e)
    
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def connect_db_flight_new1(query): # IN FINDING THE CHEAPEST FLIGHT
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='airline_system',
                                            user='root',
                                            password='1234')

        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        return records


    except Error as e:
        print("Error reading data from MySQL table", e)
    
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def connect_db_flight_update(query, vlu): # FOR UPDATING NEW FLIGHT RECORD
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='airline_system',
                                            user='root',
                                            password='1234')

        cursor = connection.cursor()
        cursor.execute(query%vlu)
        connection.commit()

    except Error as e:
        print("Error reading data from MySQL table", e)
    
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def connect_db_flight_table(query):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='airline_system',
                                            user='root',
                                            password='1234')

        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        records = cursor.fetchall()
        return records 

    except Error as e:
        print("Error reading data from MySQL table", e)
    
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def connect_db_flight_cancel(query, val): # FOR CANCELLING NEW FLIGHT RECORD
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='airline_system',
                                            user='root',
                                            password='1234')

        cursor = connection.cursor()
        cursor.execute(query%val)
        connection.commit()

    except Error as e:
        print("Error reading data from MySQL table", e)
    
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def connect_db_passenger_new(query, val): # FOR ADDING NEW PASSENGER RECORD
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='airline_system',
                                            user='root',
                                            password='1234')

        cursor = connection.cursor()
        cursor.execute(query, val)
        connection.commit()

    except Error as e:
        print("Error reading data from MySQL table", e)
    
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def connect_db_passenger_update(query, vlu): # FOR UPDATING NEW FLIGHT RECORD
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='airline_system',
                                            user='root',
                                            password='1234')

        cursor = connection.cursor()
        cursor.execute(query%vlu)
        connection.commit()

    except Error as e:
        print("Error reading data from MySQL table", e)
    
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def create_new_flight():
    questions_new_flight = [
        {
            'type' : 'input',
            'name' : 'flight_id',
            'message' : 'Flight ID:',
        },
        {
            'type' : 'input',
            'name' : 'dept_time',
            'message' : 'Departure Time:',
        },
        {
            'type' : 'input',
            'name' : 'arrival_time',
            'message' : 'Arrival Time:',
        },
        {
            'type' : 'input',
            'name' : 'dept_airport',
            'message' : 'Departure Airport:',
        },
        {
            'type' : 'input',
            'name' : 'arrival_airport',
            'message' : 'Arrival Airport:',
        },
        {
            'type' : 'input',
            'name' : 'fare',
            'message' : 'Fare:',
        },
        {
            'type' : 'input',
            'name' : 'plane',
            'message' : 'Airplane:',
        }
    ]

    new_flight_record = prompt(questions_new_flight, style = custom_style_2)
    return new_flight_record

def update_flight_data():
    questions = [
        {
            'type' : 'input',
            'name' : 'f_id', 
            'message' : 'Enter Flight ID of record you want to update:'
        },
        {
            'type' : 'list',
            'name' : 'options',
            'message' : 'What would you like to update for the current flight?',
            'choices' : ['flight_id', 'dept_time', 'arrival_time', 'dept_airport', 'arrival_airport', 'fare', 'Airplane']
        }
    ]

    answer = prompt(questions, style = custom_style_2)
    return answer

def create_new_pass():
    questions_new_recep = [
        {
            'type' : 'input',
            'name' : 'passportnum',
            'message' : 'Passport Num:',
        },
        {
            'type' : 'input',
            'name' : 'fname',
            'message' : 'First Name:',
        },
        {
            'type' : 'input',
            'name' : 'lname',
            'message' : 'Last Name:',
        },
        {
            'type' : 'input',
            'name' : 'addr',
            'message' : 'Passenger Address:',
        },
        {
            'type' : 'input',
            'name' : 'phonenum',
            'message' : 'Enter Phone Number:',
        },
        {
            'type' : 'input',
            'name' : 'nation',
            'message' : 'Nationality:',
        }
    ]

    new_recep_record = prompt(questions_new_recep, style = custom_style_2)
    return new_recep_record

def update_passenger_data():
    questions = [
        {
            'type' : 'input',
            'name' : 'passnum', 
            'message' : 'Enter Passport Number of passenger, whose data you want to update:'
        },
        {
            'type' : 'list',
            'name' : 'options',
            'message' : 'What would you like to update for the current flight?',
            'choices' : ['f_name', 'l_name', 'address', 'phone_num', 'Nationality']
        }
    ]

    answer = prompt(questions, style = custom_style_2)
    return answer


question1 = [ # PROMPT 1 : ASKS THE PERSON TO IDENTIFY ITSELF
    {
        'type' : 'list',
        'message' : 'Who are you?',
        'name' : 'post', 
        'choices' : ['Admin', 'Receptionist'],
        'validate' : lambda answer: 'You must choose at least one news option.'
    }
]

answer = prompt(question1, style=custom_style_2)
response1 = answer['post']

if response1 == 'Admin': # IF THE USER IS ADMIN THEN CARRY OUT COMMANDS ACCORDINGLY
    question2 = [
    {  
        'type' : 'input',
        'name' : 'user_name',
        'message' : 'Admin username: '
    },
    {
        'type' : 'input',
        'name' : 'password',
        'message' : 'Admin password: '
    }
    ]

    answer2 = prompt(question2, style = custom_style_2)
    input_username = answer2['user_name']
    input_password = answer2['password']

    db_admin = connect_db_admin()
    true_admin_un = db_admin[0][0]
    true_admin_pass = db_admin[0][1]

    if (input_username == true_admin_un) and (input_password == true_admin_pass): # IF ADMIN ENTERS CORRECT CREDENTIALS
        print('Correct credentials, WELCOME ADMIN')
        print('')
        admin_operations = [
            {
                'type' : 'list',
                'message' : 'What would you like to do?',
                'name' : 'operations',
                'choices' : ['Add a new Flight record', 'Update flight details', 'Cancel a flight', 'View Flights landing/taking off', 'View all tables', 'Logout'] 
            }
        ]

        ans_admin_operations = prompt(admin_operations, style = custom_style_2)
        print(ans_admin_operations['operations'])

        if (ans_admin_operations['operations'] == 'Add a new Flight record'):
            print('\nADMIN ADDING NEW RECORD\n')
            new_f_record = create_new_flight()
            # print(new_f_record)

            new_flight_query = "INSERT INTO flight (flight_id, dept_time, arrival_time, dept_airport, arrival_airport, fare, Airplane) VALUES (%s, %s, %s, %s, %s, %s, %s)" 
            val = (new_f_record['flight_id'], new_f_record['dept_time'], new_f_record['arrival_time'], new_f_record['dept_airport'], new_f_record['arrival_airport'], new_f_record['fare'], new_f_record['plane'])
            connect_db_flight_new(new_flight_query, val)

        elif (ans_admin_operations['operations'] == 'Update flight details'):
            print('\nADMIN UPDATING RECORD\n')
            query = 'SELECT * FROM flight'

            user_data = update_flight_data()
            tobe_updated_f_id = user_data['f_id']
            attribute_to_update = user_data['options']
            
            print(tobe_updated_f_id)
            print(attribute_to_update)

            ask_for_value = [
                {
                    'type' : 'input',
                    'name' : 'value',
                    'message' : 'Enter the new value:'
                }
            ]

            new_value = prompt(ask_for_value, style = custom_style_2)
            new_value1 = new_value['value']

            query1 = 'UPDATE flight SET %s = %s WHERE flight_id = "%s"'
            vlu = (attribute_to_update, new_value1, tobe_updated_f_id)

            connect_db_flight_update(query1, vlu)

        elif (ans_admin_operations['operations'] == 'Cancel a flight'):
            question = [
                {
                    'type' : 'input',
                    'name' : 'cancel_id',
                    'message': 'Enter the flight_id of the flight you want to delete.'
                }
            ]
            answer = prompt(question, style = custom_style_2)
            cancel_wala_id = answer['cancel_id']

            query = 'DELETE from flight WHERE flight_id = "%s"'
            val = (cancel_wala_id)

            connect_db_flight_cancel(query, val)

        elif (ans_admin_operations['operations'] == 'View all tables'):
            columns_flight = ["flight_id", "dept_time", "arrival_time", "dept_airport", "arrival_airport", "fare", "Airplane"]
            columns_passenger = ["Passport_num", "f_name", "l_name", "address", "phone_num", "Nationality"]
            columns_admin = ["user_name", "passward"]
            columns_recep = ["user_name", "passward"]
            columns_ticket = ["Passport_num", "flight_id"]

            admin_data = connect_db_admin()
            recep_data = connect_db_receptionist()
            flight_data = connect_db_flight() 
            passenger_data = connect_db_passenger()
            ticket_data = connect_db_ticket()

            x = PrettyTable(columns_admin)
            y = PrettyTable(columns_recep)
            z = PrettyTable(columns_flight) 
            a = PrettyTable(columns_passenger)
            b = PrettyTable(columns_ticket)

            for d in admin_data:
                x.add_row([d[0], d[1]])
            
            for d in recep_data:
                y.add_row([d[0], d[1]])

            for d in flight_data:
                z.add_row([d[0], d[1], d[2], d[3], d[4], d[5], d[6]])

            for d in passenger_data:
                a.add_row([d[0], d[1], d[2], d[3], d[4], d[5]])

            for d in ticket_data:
                b.add_row([d[0], d[1]])
            
            print("\nADMIN DATA\n")
            print(x)
            print('\n')

            print("\nRECEPTIONIST DATA\n")
            print(y)
            print('\n')

            print("\nFLIGHT DATA\n")
            print(z)
            print('\n')

            print("\nPASSENGER DATA\n")
            print(a)
            print('\n')

            print("\nTICKET DATA\n")
            print(b)
            print('\n')

    else:
        print('\nWRONG CREDENTIALS')

elif response1 == "Receptionist": # IF THE USER IS RECEPTIONIST THEN CARRY OUT COMMANDS ACCORDINGLY
    question2 = [
    {
        'type': 'input',
        'name': 'user_name',
        'message': 'Receptionist username',
    },
    {
        'type': 'input',
        'name': 'password',
        'message': 'Receptionist password'
    }
    ]

    answer2 = prompt(question2, style = custom_style_2)
    input_username = answer2['user_name']
    input_password = answer2['password']

    db_recep = connect_db_receptionist()
    true_recep_un = db_recep[0][0]
    true_recep_pass = db_recep[0][1]
    
    if (input_username == true_recep_un) and (input_password == true_recep_pass):
        print('Correct credentials, WELCOME RECEPTIONIST')
        print('')
        recep_operations = [
            {
                'type' : 'list',
                'message' : 'What would you like to do?',
                'name' : 'operation',
                'choices' : ['Add a new passenger record', 'Update existing passenger details', 'Generate ticket for passenger', 'Find cheapest flight', 'Cancel a ticket'] 
            }
        ]

        ans_recep_operations = prompt(recep_operations, style = custom_style_2)
        recep_op = ans_recep_operations['operation']

        if (ans_recep_operations['operation'] == 'Add a new passenger record'):
            print('\nRECEPTIONIST ADDING NEW PASSENGER RECORD\n')
            new_p_record = create_new_pass()
            # print(new_f_record)

            new_password_query = "INSERT INTO passenger (Passport_num, f_name, l_name, address, phone_num, Nationality) VALUES (%s, %s, %s, %s, %s, %s)" 
            val = (new_p_record['passportnum'], new_p_record['fname'], new_p_record['lname'], new_p_record['addr'], new_p_record['phonenum'], new_p_record['nation'])
            connect_db_passenger_new(new_password_query, val)

        elif (ans_recep_operations['operation'] == 'Update existing passenger details'):
            print('\nRECEPTIONIST UPDATING RECORD\n')

            user_data = update_passenger_data()
            tobe_updated_pass_num = user_data['passnum']
            attribute_to_update = user_data['options']
            
            print(tobe_updated_pass_num)
            print(attribute_to_update)

            ask_for_value = [
                {
                    'type' : 'input',
                    'name' : 'new_data',
                    'message' : 'Enter the new Data:'
                }
            ]

            new_value = prompt(ask_for_value, style = custom_style_2)
            new_value1 = new_value['new_data']

            query1 = 'UPDATE passenger SET %s = "%s" WHERE Passport_num = "%s"'
            vlu = (attribute_to_update, new_value1, tobe_updated_pass_num)

            connect_db_passenger_update(query1, vlu)

        elif (ans_recep_operations['operation'] == 'Generate ticket for passenger'):
            question = [
                {
                    'type' : 'input',
                    'name' : 'pass_num',
                    'message' : 'What is the passport number?'
                },
                {
                    'type' : 'input',
                    'name' : 'flightID',
                    'message' : 'What is the Flight ID?'
                }
            ]

            ans = prompt(question, style = custom_style_2)
            pass_num = ans['pass_num']
            flightID = ans['flightID']

            passen = connect_db_passenger1(pass_num)
            flight = connect_db_flight1(flightID)
            print(passen)
            print(flight)

            print("\n------------------------------------------------------------------\n")
            print("|    Name of Passenger   |-|    Flight ID   |-|   Passport Number   |-|    Dept Airport    |-|    Arrival Airport   |-|        Dept Date/Time       |-|    Arrival Date/Time    |")
            print("      ", passen[0][1],  passen[0][2], "              " , flightID, "                 " , passen[0][0], "                  " , flight[0][3], "               " , flight[0][4], "             " , flight[0][1], "             " , flight[0][2])
            print("\n------------------------------------------------------------------\n")

        elif (ans_recep_operations['operation'] == 'Find cheapest flight'):
            question = [
                {
                    'type' : 'input',
                    'name' : 'dept_airport',
                    'message' : 'Enter departure Airport Code'
                },
                {
                    'type' : 'input',
                    'name' : 'arrival_airport',
                    'message' : 'Enter arrival airport Code'
                }
            ]

            answers = prompt(question, style = custom_style_2)
            dept_code = answers['dept_airport']
            arri_code = answers['arrival_airport']

            query = 'SELECT * from flight WHERE (dept_airport = "%s" and arrival_airport = "%s") ORDER BY fare DESC'
            
            res = connect_db_flight_new1(query)
            #print(res)
            
            print(tabulate(res, headers=['flight_id','dept_time','arrival_time','dept_airport','arrival_airport','fare','Airplane'], tablefmt='psql'))

        elif (ans_recep_operations['operation'] == 'Cancel a ticket'):
            question = [
                {
                    'type' : 'input',
                    'name' : 'tick',
                    'message' : 'Enter the Passport Num'
                },
                {
                    'type' : 'input',
                    'name' : 'tick1',
                    'message' : 'Enter the Flight ID'
                }
            ]

            ans1 = prompt(question, style = custom_style_2)
            pass_num1 = ans1['tick']
            f_ID = ans1['tick1']

            connect_db_ticket1(pass_num1, f_ID)

    else:
        print('\nWRONG CREDENTIALS')
