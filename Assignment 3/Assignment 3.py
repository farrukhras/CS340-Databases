from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
from examples import custom_style_2
from tabulate import tabulate
import pandas as pd

def hash1(key, temp):
    res = (key + temp) % 11
    return res

def hash2(key, temp):
    res = ((key + temp) / 11) % 11
    return int(res)

def search(key, arr1, arr2): # 1. Search a given key in the tables and return the table and inde at which it is stored
    indext1 = 0
    indext2 = 0

    for x in arr1: # if the to_be_found key is in table 1 then return the table number and the index of the key
        if x == key:
            return 1, indext1

        indext1 = indext1 + 1

    for x in arr2: # if the to_be_found key is in table 1 then return the table number and the index of the key
        if x == key:
            return 2, indext2

        indext2 = indext2 + 1

    return 0, 0 # if key is not in either then return 0 for table number and index

def insert(key, fac, arr1, arr2): # 2. Insert keys in the hashtables
    for i in range(len(arr1)):
        if arr1[i] == 'empty':
            arr1[i] = -100

    for i in range(len(arr2)):
        if arr2[i] == 'empty':
            arr2[i] = -100

    hash_index1 = hash1(key, fac)
    hash_index2 = hash2(key, fac)

    if arr1[hash_index1] == key or arr2[hash_index2] == key: # check for duplicates (like key is already in the hashtable)
        print("Key is already inserted!!")
        return True

    current_key = key
    count = 0

    while count < 11: # this loop runs 11 times to check is there is a cyle or not (can run any number of time but 11 as table size is 11)
        
        prev_key = arr1[hash1(current_key, fac)] # if there is already a key in slot hashed to current key, then store that key in prev_key vairable
        arr1[hash1(current_key, fac)] = current_key #insert the new key in the slot 

        if prev_key == -100: # if the slot was empty then simply insert there and return True and exit function else insert prev to other hash table
            return True

        current_key = prev_key
        prev_key = arr2[hash2(current_key, fac)] # if there is already a key in slot hashed to current key, then store that key in prev_key vairable
        arr2[hash2(current_key, fac)] = current_key #insert the new key in the slot 

        if prev_key == -100: # if the slot was empty then simply insert there and return True and exit function else insert prev to other hash table
            return True

        current_key = prev_key

        count = count + 1
    
    print("cycle found") # loop ended thus there is cycle and now rehash the tables
    #print("Fazul key: ", key)
    return False

def print_tables(arr1, arr2): # 4. Print Tables
    for i in range(len(arr1)):
        if arr1[i] == -100:
            arr1[i] = 'empty'

    for i in range(len(arr2)):
        if arr2[i] == -100:
            arr2[i] = 'empty'

    data = data = {'Table 1': arr1, 'Table 2': arr2}
    df = pd.DataFrame(data)
    print("")
    print(df)
    
def main():

    admin_operations = [
            {
                'type' : 'list',
                'message' : 'What would you like to do?',
                'name' : 'operations',
                'choices' : ['Search a key', 'Insert a key', 'Delete a key', 'Print all tables', 'Exit'] 
            }
        ]

    answer = prompt(admin_operations, style=custom_style_2)
    arr1 = [-100] * 11 #initialise all the values in the hash table initially to -100
    arr2 = [-100] * 11 #initialise all the values in the hash table initially to -100
    temp = [0] * 22 #initialise a temparory list to store each value being added so that it can be used in rehashing when cycle detected
    bo = True
    num = 0
    z = 0

    while answer['operations'] != 'Exit':
        
        if answer['operations'] == 'Search a key':
            sear = int(input("Enter key you want to search: "))
            t_num, index = search(sear, arr1, arr2)
            
            if t_num == 0:
                print("")
                print("KEY NOT FOUND!!")
                print("")

            else:
                ans = str(sear) + " is present in " + "table" + str(t_num) + "[" + str(index) + "]"
                print("")
                print(ans)
                print("")

        elif answer['operations'] == 'Insert a key':
            #while num != 999: # enter 999 to exit insertion window
            num = int(input ("Enter word to be added: "))
            bo = insert(num, 0, arr1, arr2)
            temp[z] = num
            z = z + 1

            if bo == False: # if there is a cylce then make new hashfunctions and then rehash the inputted keys and give the result
                x = 3 # this variable is used to change the hash functions whenever there is cycle
                while bo == False:
                    for i in range(len(arr1)): # reinitialise the arrays to a default values
                        arr1[i] = -100
                        arr2[i] = -100
                    
                    for i in temp: # run this loop and fill the hashtable initially and return False if there is a cycle in the inputed keys 
                        bo = insert(i, x, arr1, arr2)

                    x = x + 3
            
            print(num," added successfully")
            print("")

        elif answer['operations'] == 'Print all tables':
            print_tables(arr1, arr2)
            print("")

        elif answer['operations'] == 'Delete a key':
            del_key = int(input("Enter key you want to delete: "))
            t_num, index = search(del_key, arr1, arr2)

            if t_num == 1:
                arr1[index] = -100
                print("")
                print("Element " + str(del_key) + " deleted successfully")
                print("")

            elif t_num == 2:
                arr2[index] = -100
                print("")
                print("Element " + str(del_key) + " deleted successfully")
                print("")

            else:
                print("")
                print("KEY NOT FOUND!!")
                print("")

        admin_operations = [
                {
                    'type' : 'list',
                    'message' : 'What would you like to do?',
                    'name' : 'operations',
                    'choices' : ['Search a key', 'Insert a key', 'Delete a key', 'Print all tables', 'Exit'] 
                }
            ]

        answer = prompt(admin_operations, style=custom_style_2)

main()