#***********************************************************************/
# CMPT 140 (2024 Fall) HW3 solution
#
# Description:
# Iterates through a list of specimen id's and convert the labelling format
# e.g. "VOA1392a" -> "VOA1392@A"
#      "VOA1392A" -> "VOA1392#A" 
# We can assume the last character is always an alphabet.
# if last character is lower case, replace it with @[upper case of last character]
# if last character is upper case, replace it with #[upper case of last character]
# Make sure “VOA” is always all upper case.
#
# Author: Samuel Leung, samuel.leung@twu.ca
# Date: Sept, 2024
#
# Input: <none>
# Output: <print patient report to console>
#
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: Samuel Leung
#*********************************************************************/

# note: to install Python modules, use pip
# console> pip install pandas openpyxl
import pandas as pd
import os

def main():
    # open an Excel file and read the data into a data frame
    # data frame like a spreadsheet with rows/columns
    # NOTE: please replace with path/name of your file
    d = pd.read_excel("specimen_ids.xlsx")
    
    # initilize a list to store the reformatted ID's.
    new_ids = [] # empty list

    # iterate through all rows in a data frame
    # %%
    for index, row_content in d.iterrows():
        # in this for-loop, there are two loop variables:
        # index = row number
        # row = actual content of the row, in a array-like data structure,
        #       called "Series", which is somewhat like a list.
        #       To access an elemetn in this Series, r, we do the following:
        #       row_content[i]
        #       We can think of this as trying to access column "i" in the row
        #       whose content is stored in row_content
        #
        # the following commented lines print out the index and content of
        # each row.  Try putting them (remember to remove the comment # sign)
        # inside the for loop and observe the content.  You should be able to
        # compare the print out with the content of the Excel file.
        #
        print("row "+str(index)+" "+str(row_content))
        # print(str(index))
        # print(type(row_content))
        
        # NO NEED TO iterate through all "columns" or "cell" of a row
        # we assume ALL specimen ID's are located in first column

        # store the content in a variable for us to manipulate it
        # id = row_content["Specimen ID"] # you can specify via column name

        # please generate the id in new format

        # please remember to add the formatted ID to the list "new_ids"

    # please add a for loop that iterate (go through) all items in the 
    # list "new_ids" and print out the content
    
# if needed, change working directory to the folder where data file is stored
# os.chdir("hw3") # you may not need this, depending on your working folder

# call main function
main()
