from abc import ABC, abstractmethod

class CRUDInterface(ABC):

    @abstractmethod
    def insert(self, *args, **kwargs) -> None:
        """Insert a new record."""
        pass

    @abstractmethod
    def update(self, *args, **kwargs) -> None:
        """Update a record identified by the identifier."""
        pass

    @abstractmethod
    def delete(self, *args, **kwargs) -> None:
        """Delete a record identified by the identifier."""
        pass
