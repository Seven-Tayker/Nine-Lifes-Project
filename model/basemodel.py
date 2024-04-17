from abc import ABC, abstractmethod


class AbstractBaseModel(ABC, dict):
    def __init__(self) -> None:
        self.id = None
        super().__init__()

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def read(self, id=None):
        pass

    @abstractmethod
    def delete(self):
        pass

    def __str__(self):
        return f"BaseModel {self.id}"
