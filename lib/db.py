import re
import pyodbc
import logging
from typing import Any, Dict, List, Optional, Tuple

class DatabaseConnector:
    _instance = None
    connection: Optional[pyodbc.Connection] = None
    cursor: Optional[pyodbc.Cursor] = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance is None:
            del cls._instance

        cls._instance = super(DatabaseConnector, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        server = 'hamidi\\SQLEXPRESS'
        database  = 'car_loan'
        # self.connection_string = f"Driver={{SQL Server}};Server={server};Database={database};UID={username};"  
        # PWD=your_password;
        self.connection_string = f"Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection=yes;"
        self.connect()

    def connect(self):
        """Establish a connection to the SQL Server database."""
        try:
            self.connection = pyodbc.connect(self.connection_string)
            self.cursor = self.connection.cursor()
            logging.info("Database connection established.")
        except pyodbc.Error as e:
            self.handle_error(e)

    def execute_query(self, query: str, params: Optional[List[str]] = None) ->(List[Dict[str, Any]] | None):
        """Execute a query and return the results."""
        
        logging.info(f"query statement : {query} | params: {params}")
        try:
            if (not self.cursor or not self.connection):
                    raise Exception('cursor or connection is not defined')
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

            # If the query is a SELECT statement, fetch the results
            if query.strip().upper().startswith("SELECT"):
                columns = [column[0] for column in self.cursor.description]
                results = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
                logging.info(f'execute query result: {results}')
                return results
            else:
                self.connection.commit()
                return []
        except pyodbc.Error as e:
            self.handle_error(e)

        except Exception as e:
            self.handle_error(e)

    def handle_error(self, error: pyodbc.Error | Exception) -> Tuple[bool, str | None]:
        """Handle database errors."""
        logging.error(f"Database error: {error}")
        error_result = self.handle_sql_error(error)
        raise Exception(error_result)
    
    def handle_sql_error(self, error) -> str | None:
        error_message = str(error)
        error_code = error.args[0]  # Get the SQL error code

        if error_code == '42S22':  # Invalid column name
            invalid_columns = self.extract_invalid_columns(error_message)
            return f"Insert failed: Invalid column names: {', '.join(invalid_columns)}"
        
        elif error_code == '23000':  # Integrity constraint violation
            if "duplicate key" in error_message.lower():
                return "Insert failed: Duplicate key violation."
            elif "foreign key" in error_message.lower():
                return "Insert failed: Foreign key violation."
            elif "CK_NOT_BE_MPT_".lower() in error_message.lower():
                match = re.search(r"column \\'([^']+)\\'", f"{error_message}")
                print('match is ', match)
                if match:
                    column_name = match.group(1)
                    return f"Insert failed: The value for '{column_name}' cannot be empty."
            
        elif "data type" in error_message.lower():
            return "Insert failed: Data type mismatch."
        
        elif "timeout" in error_message.lower():
            return "Insert failed: Query timeout."
        
        elif "syntax" in error_message.lower():
            return "Insert failed: SQL syntax error."
        
        else:
            return f"Insert failed: {error_message}"
        
        return f"{error_message}"


    def extract_invalid_columns(self, error_message):
        invalid_columns = []
        print('Error | function: extract_invalid_columns : ', f"{error_message}")
        if "Invalid column name" in error_message:
            pattern = r"Invalid column name '([^']*)'"
            invalid_columns = re.findall(pattern, error_message)
            return invalid_columns
        return invalid_columns

    def close(self):
        """Close the database connection."""
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None
        if self.connection is not None:
            self.connection.close()
            self.connection = None
        logging.info("Database connection closed.")

    def __del__(self):
        """Destructor to ensure the connection is closed."""
        self.close()
        self._instance = None









# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    db_connector = DatabaseConnector()

    try:
        # Example query
        results = db_connector.execute_query("SELECT * FROM customers")
        if results:
            for row in results:
                print(row)
        else : 
            logging.info('no result')

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db_connector.close()
