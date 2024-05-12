from pydantic import BaseModel

class Task:
    recordID: str
    name: str
    status: str

class AuthRequest(BaseModel):
    username: str
    password: str

class AddTaskRequest(BaseModel):
    username: str
    taskName: str

class DeleteTaskRequest(BaseModel):
  rid: str

class EditTaskRequest(BaseModel):
  rid: str
  name: str
  status: str
