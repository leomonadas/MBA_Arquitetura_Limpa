from domain.user.user_repository_inferface import UserRepositoryInterface
from domanin._seedwork.use_case_interface import UseCaseInterface
from usecases.user.add_user.add_user_dto import AddUserInputDto, AddUSerOutputDto

class AddUserUseCase(UseCaseInterface):

    user_repository: UserRepositoryInterface

    def _init_(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execut(self, input: AddUserInputDto) -> AddUserOutputDto:
        user = user(id=uuid.uuid4(),  name = input.name)
        print(user.name)
        self.user_repository.add_user(user=user)


# user_repository = UserRepository(session = session)
# usecase = AddUserUseCase(user_repository = user_repository)
# output: AddUserOutputDto = usecase.execute(input=AddUserInputDto(name = "leo"))
# output.id
# output.name
