from sqlalchemy import and_
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import false
from datetime import datetime

from app.models.models import Users
from app.schemas.userDto import UserInput, UserOutput, UserInDb


class UserRepo:
  
  def __init__(self, session: Session):
    self.session = session

  def create_user(self, address: str) -> UserOutput:
    user = Users(address=address, is_valid=True)
    self.session.add(user)
    self.session.commit()
    self.session.refresh(user)
    return UserOutput(**user.__dict__)
  
  def get_user_by_address(self, address: str) -> UserOutput:
    user = self.session.query(Users).filter_by(address=address).first()
    return UserOutput(**user.__dict__)

  def get_user_by_email(self, user_email):
    ...

  def delete_user(self, user_id):
    ...


          
  async def update_user(self, data: UserInput):
    ...