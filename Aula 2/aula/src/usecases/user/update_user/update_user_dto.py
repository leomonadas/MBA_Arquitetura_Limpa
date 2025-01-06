from pydantic import BaseModel

#INPUT
class UpdateUserInputDto(BaseModel):
    id: UUID
    name: str

#OUTPUT
class UpdateUserOutputDto(BaseModel):
    id: UpdateUserInputDto
    name: str