from abc import ABCMeta, abstractmethod

class StorageInterface(metaclass=ABCMeta):
    """
    interface class for all type of storages
    """

    timezone: str

    @abstractmethod
    def save(self, values:list):
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_all_by_depth(self, hours:int) -> list:
        raise NotImplementedError