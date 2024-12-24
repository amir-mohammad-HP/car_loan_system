from abc import ABC, abstractmethod
from typing import Dict, List, Any

class ViewInterface(ABC):
    view: str

    @property
    def _query_statement(self):
        return "SELECT * FROM {}".format(self.view)
    
    @abstractmethod
    def query(self, *args, **kwargs) -> List[Dict[str, Any]]:
        """Query all records."""
        pass

    @abstractmethod
    def query_by(self, col: str, *args, **kwargs) -> List[Dict[str, Any]]:
        """Query records based on a condition."""
        pass