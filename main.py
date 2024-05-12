from fastapi import FastAPI, UploadFile, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from helper import *
from fastapi.middleware.cors import CORSMiddleware
from models import *

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return "API Works"

@app.post("/Register")
def CreateUserEndpoint(request: AuthRequest):
    return Register(request.username, request.password)

@app.post("/Login/")
def LoginEndpoint(request: AuthRequest):
    return Login(request.username, request.password)

@app.get("/GetTasks/")
def GetTasksEndpoint(username):
    if username == '': return
    return GetTasksByUser(username)

@app.post("/AddTask")
def CreateTaskEndpoint(request: AddTaskRequest):
    return CreateTask(request.username, request.taskName)

@app.post("/UpdateTaskStatus")
def UpdateTaskStatusEndpoint(request: EditTaskRequest):
    return UpdateTask(request.rid, request.name, request.status)

@app.post("/DeleteTask")
def DeleteTaskEndpoint(request: DeleteTaskRequest):
    return DeleteTask(request.rid)


