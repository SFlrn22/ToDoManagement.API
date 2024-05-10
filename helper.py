import pyorient
from hashlib import sha256
import base64
from models import *

client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect("root", "orientroot")
client.db_open("ManageToDoDB", "root", "orientroot")

def GetTasksByUser(username):
    taskArr = []

    user = client.query(f'SELECT * FROM Users WHERE Username = "{username}"')

    userRID = user[0]._rid

    data = client.query(f'SELECT * FROM Tasks WHERE @rid in (select in from `Has` where out = "{userRID}")')

    if len(data) != 0:
        for task in data:
            mappedTask = Task()
            mappedTask.recordID = task._OrientRecord__rid
            mappedTask.name = task._OrientRecord__o_storage["Name"]
            mappedTask.status = task._OrientRecord__o_storage["Status"]
            taskArr.append(mappedTask)

    return taskArr
        

def Register(username, password):
    hashedPassword = base64.b64encode(sha256(password.encode('utf-8')).digest()).decode('utf-8')

    cmd = f'INSERT INTO Users (Username, Password) VALUES ("{username}", "{hashedPassword}")'

    try:
        result = client.command(cmd)
    except Exception as e:
        return e

    return "Success"

def Login(username, password):
    user = client.query(f'SELECT * FROM Users WHERE Username = "{username}"')

    if len(user) == 0:
        return "User does not exist"

    returnedPassword = user[0]._OrientRecord__o_storage["Password"]
    hashedPassword = base64.b64encode(sha256(password.encode('utf-8')).digest()).decode('utf-8')

    if(hashedPassword == returnedPassword):
        return True

    return False

def CreateTask(username, taskName):
    user = client.query(f'SELECT * FROM Users WHERE Username = "{username}"')

    userRID = user[0]._OrientRecord__rid

    try:
        cmdResult = client.command(f'INSERT INTO Tasks (Name, Status) VALUES ("{taskName}", "To Do")')
        taskRID = cmdResult[0]._rid
        client.command(f'CREATE edge Has from {userRID} to {taskRID};')
    except Exception as e:
        return e
    
    return "Success"

def UpdateTask(username, taskName, status):
    user = client.query(f'SELECT * FROM Users WHERE Username = "{username}"')

    userRID = user[0]._rid

    try:
        tasks = client.command(f'UPDATE Tasks SET Status = "{status}" WHERE @rid in (select in from `Has` where out = "{userRID}") and Name = "{taskName}"')
    except Exception as e:
        return e
    
    return "Success"

def DeleteTask(rid):
    try:
        client.command(f'DELETE FROM Tasks WHERE @rid = "{rid}"')
    except Exception as e:
        return e
    
    return "Success"