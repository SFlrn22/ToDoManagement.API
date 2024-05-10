from fastapi import FastAPI, UploadFile, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from helper import *


app = FastAPI()

@app.get("/")
def root():
    return "API Works"

@app.post("/Register")
def CreateUserEndpoint(username, password):
    return Register(username, password)

@app.post("/Login")
def LoginEndpoint(username, password):
    return Login(username, password)

@app.get("/GetTasks")
def GetTasksEndpoint(username):
    return GetTasksByUser(username)

@app.post("/AddTask")
def CreateTaskEndpoint(username, taskName):
    return CreateTask(username, taskName)

@app.post("/UpdateTaskStatus")
def UpdateTaskStatusEndpoint(username, taskName, status):
    return UpdateTask(username, taskName, status)

@app.post("/DeleteTask")
def UpdateTaskStatusEndpoint(rid):
    return DeleteTask(rid)


