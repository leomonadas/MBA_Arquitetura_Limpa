from pydantic import BaseModel
from uuid import UUID

#INPUT
class FindUserInputDto(BaseModel):
    id:UUID

#OUTPUT
class FindUserOutputDto(BaseModel):
    id:UUID
    name: str