#import librari json
import json

#This Function is to save everything in a file

def save_file(Tareas):
    with open("Tareas.json","w") as file: #this is for writing everithing inside of the list in the file.
        json.dump(Tareas,file,indent=4)
        print("The Data has been saved Correctly.\n ")

#This function is used to upload a file

def load_file(Tareas):
    try:
        with open("Tareas.json","r") as file: # this is for loaded  the before file.
            Tareas = json.load(file)
            print("Data uploaded Correctly.\n")
            return Tareas

    except:
        print("No data Saved.\n")# in the case don't have a some file befor, the program show this message
        return[]            


#This Function serves for crate a new Task.
def register_newtask(Tareas):
    #In This try is for the user can insed the necessary  data 
    try:
        Id=input("Enter an ID: ") 
        Title=input("Enter a Title: ")
        Description=input("Enter More Details: ")
        Priority=input("High,Medium,Low\n")
        Status=input("pending/completed\n ")

        tarea={#this is the Dictionary tha we used for store the data of Tareas
            "id":Id,
            "title":Title,
            "description":Description,
            "priority":Priority,
            "status":Status
        }
        Tareas.append(tarea)#here we are add the conten of the dictionaty at the List
        print("The task has been added. ")
    except:
        print("Could not add the task. ")

#Ths function serves for show evrything in the list
def consult_task(Tareas):
    if len(Tareas) == 0:
        print("ther is no homework. ")#when Tareas don't have data show this message.
    else:
        for tarea in Tareas:
            print(f"ID:{tarea["id"]} | Title:{tarea["title"]} | Description:{tarea["description"]} | Priority:{tarea["priority"]} | Status:{tarea["status"]}")               

#This Function serves to search for some criteria
def search_task(Tareas):
    x = input("Enter (ID,Title or Status) ")

    for t in Tareas:
        if t["id"] == x or t["title"] == x or t["status"] == x:
            print(t)
            return
    
    print("the task could not be found. ")

#This Function is fir Update the infomation of the tasks
def update_tasks(Tareas):
    id = input("Pleas Enter the ID to Update. ")
    for t in Tareas:
        if t["id"] == id:
            t["title"]=input("Change the Title: ")
            t["description"]=input("Change the Description")
            t["pirority"]=input("Update the Priority. ")
            t["status"]=input("Change the Status. ")
            print("Upgradin\n")
            return

    print("Could't be found.")    

#This Function serves to delete any task do you want.
def delete_task(Tareas):
    id = input("ID  to be Delete. ")
    for t in Tareas:
        if t ["id"] == id:
            Tareas.remove(t)
            print("Deleted\n")
            return
        print("Not Found\n")



def menu():
    Tareas=[]
    op = 0

    while op !=8:
        print("|   ---Menu---  |")
        print("|1.Register Task|")
        print("|2.Consult  Task|")
        print("|3.Search a Task|")
        print("|4.Update a Task|")
        print("|5.Delete a Task|")
        print("|6.Save Data    |")
        print("|7.Load Data    |")
        print("|8.Exit.        |")

        op = input("Choose an Option. ")

        if op =="1":
            register_newtask(Tareas)
        elif op =="2":
            consult_task(Tareas)
        elif op =="3":
            search_task(Tareas)
        elif op =="4":
            update_tasks(Tareas)
        elif op =="5":
            delete_task(Tareas)
        elif op =="6":
            save_file(Tareas)
        elif op =="7":
            Tareas = load_file (Tareas)       
        elif op =="8":
            print("Closing\n")
            break
        else:
            print("Not Valid Option.\n")


menu()                                   