from sqlalchemy import ForeignKey, Column, TEXT, INT, BIGINT, DATETIME, BOOLEAN, String
from sqlalchemy.ext.declarative import declarative_base

from app.db.database import engine

Base = declarative_base()
# Base.metadata.create_all(bind=engine)

class Users(Base):
  __tablename__ = "users"

  id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
  address = Column(TEXT, nullable=True)
  email = Column(TEXT, nullable=True)
  # password = Column(TEXT, nullable=True)
  # salt = Column(TEXT, nullable=True)
  nickname = Column(TEXT, nullable=True)
  mobile = Column(TEXT, nullable=True)
  
  bio = Column(TEXT, nullable=True)
  telegram = Column(TEXT, nullable=True)
  twitter = Column(TEXT, nullable=True)
  instagram = Column(TEXT, nullable=True)
  discord = Column(TEXT, nullable=True)
  is_valid = Column(BOOLEAN, nullable=False)
  
  created_at = Column(DATETIME, nullable=True)
  modified_at = Column(DATETIME, nullable=True)

class SharedRewards(Base):
  __tablename__ = "shared_rewards"
  # models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)

  id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
  user_id = Column(BIGINT, ForeignKey(Users.id, ondelete="SET NULL", onupdate="CASCADE"))
  reward = Column(TEXT, nullable=False)
  transaction = Column(TEXT, nullable=False)
  order = Column(TEXT, nullable=False)
  created_at = Column(DATETIME, nullable=True)
  modified_at = Column(DATETIME, nullable=True)
  

class TransactionRewards(Base):
  __tablename__ = "transaction_rewards"
  # models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)

  id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
  user_id = Column(BIGINT, ForeignKey(Users.id, ondelete="SET NULL", onupdate="CASCADE"))
  reward = Column(TEXT, nullable=False)
  transaction = Column(TEXT, nullable=False)
  order = Column(TEXT, nullable=False)
  is_withdrawable = Column(BOOLEAN, nullable=False)
  created_at = Column(DATETIME, nullable=True)
  modified_at = Column(DATETIME, nullable=True)
  
  
class InvitationRewards(Base):
  __tablename__ = "invitation_rewards"
  # models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)

  id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
  user_id = Column(BIGINT, ForeignKey(Users.id, ondelete="SET NULL", onupdate="CASCADE"))
  reward = Column(TEXT, nullable=False)
  transaction = Column(TEXT, nullable=False)
  order = Column(TEXT, nullable=False)
  is_withdrawable = Column(BOOLEAN, nullable=False)
  created_at = Column(DATETIME, nullable=True)
  modified_at = Column(DATETIME, nullable=True)
  
  
  
Base.metadata.create_all(bind=engine)