from domain.user.user_repository import UserRepositoryInterface
from domain.__seedwork.user_case_interface import UseCaseInterface
from usecases.user.find_user.find_user_dto import FindUserInputDto, FindUserOutputDto

class FindUserCase(UseCaseInterface):
    user_repository: UserRepositoryInterface
    
    def _init_(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, input: FindUserInputDto) -> FindUserOutputDto:
        user = self.user_repository.find_user(user_id = input.id)

        return FindUSerOutputDto(id=user.id, name=user.name)
