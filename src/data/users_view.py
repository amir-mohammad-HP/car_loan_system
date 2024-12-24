import logging
from typing import Any, Dict, List, Optional, Tuple
import uuid
import logging
from lib.crud import CRUDInterface
from lib.db import DatabaseConnector
from lib.view import ViewInterface


class UsersView(ViewInterface):
    view = 'users_v1'

    def __inti__(self):
        self._query = self._query_statement

    def query(self, *args, **kwargs) -> List[Dict[str, Any]]:
        db = DatabaseConnector()
        results = db.execute_query(self._query_statement)
        if results:
            for row in results:
                logging.info(f'[users.query] result row: {row}')
        else:
            logging.info('[users.query] no result')
        db.close()
        
        return results if results else []

    def query_by(self, col: str, *args, **kwargs) -> List[Dict[str, Any]]:
        db = DatabaseConnector()
        results = db.execute_query(self._query, (args[0]))
        if results:
            for row in results:
                logging.info(f'[users.query_by] result row: {row}')
        else:
            logging.info('[users.query_by] no result')
        db.close()
        
        return results if results else []
