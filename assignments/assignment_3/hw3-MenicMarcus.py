#################################################################################
# Homework Assignment 3: for loop, string processing
#
# Description:
# Reads an excel file full of id codes and formats them using specific guidelines
#
# Author: Marcus Menic, marcusbmenic@gmail.com
# Date: October 4, 2024
#
# Input: <none>
# Output: <list of formatted ids are printed to the console>
#
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: Marcus Menic
###################################################################################

import pandas as pd
import os

d = pd.read_excel("specimen_ids.xlsx")

new_ids = []


def main():

    # goes through all the rows of the excel file, modifies, and stores ids in new list
    for index, row in d.iterrows():
        
        id = row["Specimen ID"]


        # Makes sure the first three characters are uppercase VOA
        if id[0:3] != "VOA": 

            id = "VOA" + id[3:len(id)]


        # If the last character is uppercase inserts the # symbol before it
        if id[len(id) - 1].islower(): 

            last_character = id[-1]
            id = id[0:(len(id) - 1)]
            id = id + "@" + last_character.upper()
        
        # If the last character is lowercase it makes that character uppercase and then puts the @ symbol before it
        elif id[len(id) - 1].isupper():
            
            last_character = id[len(id) - 1]
            id = id[0:(len(id) - 1)]
            id = id + "#" + last_character

        new_ids.append(id)  # add final version of id to new_ids list 
    
    #prints the entire new_ids list in order
    for i in range(len(new_ids)):
        print(new_ids[i])

main()

        




    
    
    


    

       
       
       








