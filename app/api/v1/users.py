import asyncio, time
import json

from sqlalchemy.orm import Session
from fastapi import APIRouter, Body, Depends, HTTPException, UploadFile, Request, Response

from app.services.userService import UserService
from app.schemas.userDto import UserInput, UserOutput
from app.db.database import MysqlDB
# from schemas.userDto import user

router = APIRouter(prefix='/users')

async def say_after(delay, what):
  await asyncio.sleep(delay)
  print(what)
  
@router.get("")
def read_users(address: str):
  session = MysqlDB.sessionmaker()
  _service = UserService(session)
  return _service.read_user(address)

@router.post("")
def create_users(address: str):
  # session = Depends(MysqlDB.sessionmaker)
  session = MysqlDB.sessionmaker()
  _service = UserService(session)
  return _service.create_user(address)

@router.put("", response_model=UserOutput)
async def update_users(data: UserInput, session: Session = Depends(MysqlDB.sessionmaker)):
  try:
    _service = UserService(session)
    return _service.update_user(data)
  except Exception as e:
    return json.dumps(status_code=400, content={"success": False, "error": ""})

@router.post("/test")
async def get_test():
    
  # task = asyncio.create_task(say_after(1, 'hello'))
  # print(json.loads(status_code=400, content={"success": True, "data": "hello world"}))

  return Response(status_code=400, content={"success": True, "data": "hello world"})
