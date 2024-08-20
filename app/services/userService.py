from app.models import models
from app.schemas.userDto import UserInput
from app.db.database import MysqlDB
from app.repos.userRepo import UserRepo


class UserService:
  def __init__(self, session):
    self.repository = UserRepo(session)
    
  def create_user(self, address: str):
    return self.repository.create_user(address)

  def update_user(self, data: UserInput):
    return self.repository.update_users(data)

  def read_user(self, address: str):
    return self.repository.get_user_by_address(address)
  
  def read_users(self):
    return self.repository.get_all_users()

  def read_user_by_email(self, user_email: str):
    return self.repository.get_user_by_email(user_email)

  def update_user(self, user_id, user_data: models.Users):
    return self.repository.update_user(user_id, user_data)

  async def delete_user(self, user_id: int):
    return await self.repository.delete_user(user_id)