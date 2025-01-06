from uuid import UUID, uuid4

class User:
    id: UUID
    name: str

    def __init__(self, id: UUID, name: str):
        self.id = id
        self.name = name
        self.validate()

    def validate(self):
        if not isinstance(self.id, UUID):
            raise Exception("id must bem an UUID.")

        if not isinstance(self.name, str) or len(self.name)==0:
            raise Exception("Name is required.")


usuario_1 = User(id=uuid4(), name="Leonardo")

# usuario_1.name #Leonardo


