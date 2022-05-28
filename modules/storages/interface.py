from abc import ABCMeta, abstractmethod

class StorageInterface(metaclass=ABCMeta):
    """
    interface class for all type of storages
    """

    timezone: str

    @abstractmethod
    def save(self, values:list):
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def get_all_by_depth(self, hours:int) -> list:
        pass