import csv
import os

name    =   input("what's your name? : ")
home    =   input("where are you from? : ")

with open("/Users/shashi/Documents/Project/python3/input_output/data.csv", "a") as file :
    #writer = csv.writer(file)
    writer = csv.DictWriter(file , fieldnames=['name', 'home'])
    writer.writerow({"name" : name, "home" : home})
