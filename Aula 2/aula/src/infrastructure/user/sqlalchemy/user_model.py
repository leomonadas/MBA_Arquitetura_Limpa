from infrastructure.api.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

class UserModel(Base):
    _tablename_ = "tb_users"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)

    