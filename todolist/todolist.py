#module
import os
import time
from pyfiglet import Figlet
from termcolor import colored
from datetime import datetime as dt

#banner
def banner():
    f = Figlet(font ="slant")
    banner = (f.renderText("To Do List"))
    print(colored(banner,"blue"))
#todolist where all the task and timming is store
todolist = {}

#todo list time checker
def timmer():
    a = list(todolist.values())
    for i in a:
        while True:
            hour = str(dt.now().strftime("%H:%M"))
            if hour == i:
                break
            else:
                time.sleep(0.1)
        print(colored("conguratulation your task is completed ","green"))
        for k in list(todolist):
            if todolist[k] == i:
                del todolist[k]

#to add the task in todolist
def add():
    n = int(input(colored("enter a number of task(like 1,2,3,4,5.....):")))
    for a in range(n):
         key = str(input("enter your task:"))
         value = str(input("enter timing(h:m) :"))
         todolist[key]=value
    print(todolist)

#to delete the task form todo list
def delete():
    n = str(input(colored("enter the element name:","yellow")))

    del todolist[n]

#menu
def menu():
    print(colored("1)add task 2)print 3)delete task  4)menu 5)start timmer 6)exit ","yellow"))

#printing the task
def task():
    task = todolist.keys()
    for i in task:
        print(i ,end = "\n")
os.system("clear")
banner()
#main program
loop = 1
while loop == 1:
    task()
    menu()
    print(colored("============================================================================================","red"))
    choice = str(input(colored("enter option(1,2,3,4,5,6):","yellow")))
    if choice == "1":
        add()
    elif choice == "2":
        task()
    elif choice == "3":
        delete()
    elif choice == "4":
        menu()
    elif choice == "5":
        timmer()
    elif choice == "6":
        exit()
    else:
        os.system("clear")
        banner()
        continue

print("thank you ")
