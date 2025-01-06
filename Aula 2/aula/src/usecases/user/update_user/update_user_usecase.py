from domain.__seedwork.user_case_interface import UseCaseInterface
from domain.user.user_repository import UserRepositoryInterface
from usecases.user.update_user.update_user_dto import UpdateUserInputDto, UpdateUserOutputDto

class UpdateUserUseCase(UseCaseInterface):

    user_repository: UserRepositoryInterface

    def _init_(self, user_repository:UserRepositoryInterface):
        user_repository = user_repository

    def execute(self, input:UpdateUserInputDto -> UpdateUSerOutputDto):
        user = User(id=input.id, name=input.name)

        self.user_repository.update_user(user=user)

        return UpdateUSerOutputDto(id=user.id, name=user.name)