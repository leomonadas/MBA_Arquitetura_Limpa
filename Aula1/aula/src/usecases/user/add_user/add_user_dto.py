from pydantic import Basemodel
from uuid import UUID

#INPUT
class AddUserInputDto(BaseModel):
    name:str

#OUTPUT
class AddUserOutputDto(BaseModel):
    id: UUID
    name: str

# usecase = AddUserUseCase(repository = repository)
# output = usecase.execute(input=AddUserInputDto(name="Alexandre"))