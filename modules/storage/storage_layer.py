"""
Additional layer for databases
"""

from abc import ABCMeta, abstractmethod

class StorageInterface(metaclass=ABCMeta):
    """
    storage interface class
    """

    @abstractmethod
    def save(self, values:list):
        pass
