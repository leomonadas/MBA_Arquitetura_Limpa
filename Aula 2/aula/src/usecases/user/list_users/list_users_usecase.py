from domain.__seedwork.user_case_interface import UseCaseInterface
from domain.user.user_repository import UserRepositoryInterface
from usecases.user.list_users.list_users_dto import ListUsersInputDto, ListUsersOutputDto


class ListUserUseCase(UseCaseInterface):
    user_repository: UserRepositoryInterface

    def _init_(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, input: ListUsersInputDto) -> ListUsersOutputDto:
        users = self.user_repository.list_users()

        output = []

        for user in users:
            user_dto = UserDto(id=user.id, name=user.name) 
            output.append(UserDto())

        return ListUsersOutputDto(users=output)