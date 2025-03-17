from abc import ABC, abstractmethod

class APIBase(ABC):
    @abstractmethod
    def get_100_biggest_stocks_history(self):
        """Method to fetch data from the API"""
        pass