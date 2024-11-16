#################################################################################
# Homework Assignment 1: Variables, Input/Output
#
# Description:
# This program asks the user a series of questions and displays them in an easy
# to read fashion for the doctor to view and diagnose based on the results
# 
#
# Author: Marcus Menic, marcusbmenic@gmail.com
# Date: September 13, 2024
#
# Input: <none>
# Output: <only a log of what takes place>
#
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: Marcus Menic
###################################################################################

# Greets the user 
print("Greetings user")                  
print("Please answer the following questions")
print(" ")

# Gathers data from the user
name = input("What is your name?: ")
weight = input("What is your weight in kilograms?: ")
height = input("What is your height in centimeters?: ")
poleMutation= input("Do you have a POLE mutation? (yes/no) : ")
mmrDeficiency = input("Do you have a MMR deficiency? (yes/no) : ")
p53Mutation = input("Do you have a p53 mutation? (yes/no) : ")
      
#Calculates BMI
bmi = float(weight) / ((float(height) / 100) * (float(height) / 100)) 

#Outputs data in readable format
print(" ")
print("*** Patient", name, "Test Results ***")
print("BMI:", bmi)
print("POLE mutation:", poleMutation)
print("MMR mutation:", mmrDeficiency)
print("P53 mutation:", p53Mutation)

